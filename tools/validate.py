"""Check that the mod package and the committed ZIP are complete and consistent.

Usage: python tools/validate.py
"""

import json
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "mod"
ZIP = ROOT / "Helldivers-2-Enhanced-Loot-Arrows.zip"
PATCH_SUFFIXES = ("", ".gpu_resources", ".stream")

errors = []


def error(message):
    errors.append(message)
    print(f"ERROR: {message}")


def safe_relative(path):
    """True if a manifest path stays inside the mod folder."""
    p = PurePosixPath(path)
    return not p.is_absolute() and ".." not in p.parts and "\\" not in path


def check_image(path, where):
    if not safe_relative(path):
        error(f"{where}: unsafe image path {path!r}")
    elif not (MOD / path).is_file():
        error(f"{where}: image not found: {path}")


def check_include(path, where):
    if not safe_relative(path):
        error(f"{where}: unsafe include path {path!r}")
        return
    folder = MOD / path
    if not folder.is_dir():
        error(f"{where}: include folder not found: {path}")
        return
    files = {f.name for f in folder.iterdir() if f.is_file()}
    bases = {name for name in files if name.split(".")[-1].startswith("patch_")}
    if not bases:
        error(f"{where}: no patch files in {path}")
    expected = {base + suffix for base in bases for suffix in PATCH_SUFFIXES}
    for name in sorted(expected - files):
        error(f"{where}: missing {path}/{name}")
    for name in sorted(files - expected):
        error(f"{where}: unexpected file {path}/{name}")


def check_manifest():
    try:
        manifest = json.loads((MOD / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(f"manifest.json could not be read: {exc}")
        return set(), set()

    for key in ("Version", "Guid", "Name", "Description", "IconPath", "Options"):
        if key not in manifest:
            error(f"manifest.json: missing {key}")

    images = set()
    includes = set()
    if "IconPath" in manifest:
        check_image(manifest["IconPath"], "IconPath")
        images.add(manifest["IconPath"])

    names = [option.get("Name") for option in manifest.get("Options", [])]
    for name in {n for n in names if names.count(n) > 1}:
        error(f"manifest.json: duplicate option name {name!r}")

    for option in manifest.get("Options", []):
        entries = [(option.get("Name"), option)]
        entries += [
            (f"{option.get('Name')} / {sub.get('Name')}", sub)
            for sub in option.get("SubOptions", [])
        ]
        for where, entry in entries:
            if "Image" in entry:
                check_image(entry["Image"], where)
                images.add(entry["Image"])
            for path in entry.get("Include", []):
                check_include(path, where)
                includes.add(path)
        if not option.get("Include") and not option.get("SubOptions"):
            error(f"{option.get('Name')}: option includes nothing")

    return images, includes


def check_unused(images, includes):
    for image in sorted((MOD / "Images").glob("*")):
        rel = image.relative_to(MOD).as_posix()
        if rel not in images:
            error(f"unused image: {rel}")
    patch_folders = {
        f.parent.relative_to(MOD).as_posix()
        for f in MOD.rglob("*")
        if f.is_file() and f.suffix not in (".md", ".json", ".jpg")
    }
    for folder in sorted(patch_folders - includes):
        error(f"patch folder not used by any option: {folder}")


def check_zip():
    if not ZIP.is_file():
        error(f"{ZIP.name} not found. Run: python tools/build_zip.py")
        return
    disk = {
        f.relative_to(MOD).as_posix(): f
        for f in MOD.rglob("*")
        if f.is_file()
    }
    with zipfile.ZipFile(ZIP) as z:
        if z.testzip() is not None:
            error(f"{ZIP.name} is corrupt")
            return
        names = {i.filename for i in z.infolist() if not i.is_dir()}
        for name in sorted(names):
            if not safe_relative(name):
                error(f"{ZIP.name}: unsafe path {name!r}")
        for name in sorted(disk.keys() - names):
            error(f"{ZIP.name} is missing {name}. Run: python tools/build_zip.py")
        for name in sorted(names - disk.keys()):
            error(f"{ZIP.name} has extra file {name}. Run: python tools/build_zip.py")
        for name in sorted(disk.keys() & names):
            if z.read(name) != disk[name].read_bytes():
                error(f"{ZIP.name} is out of date: {name}. Run: python tools/build_zip.py")


def main():
    images, includes = check_manifest()
    check_unused(images, includes)
    check_zip()
    if errors:
        print(f"\n{len(errors)} problem(s) found.")
        return 1
    print(f"OK: manifest, {len(includes)} option folders, {len(images)} images and {ZIP.name} all check out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
