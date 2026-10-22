"""Build the Arsenal-ready ZIP from the contents of mod/.

Usage: python tools/build_zip.py

Files are added in sorted order with a fixed timestamp, so rebuilding
unchanged files gives the same contents.
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "mod"
ZIP = ROOT / "Helldivers-2-Enhanced-Loot-Arrows.zip"
TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def main():
    files = sorted(
        (f for f in MOD.rglob("*") if f.is_file()),
        key=lambda f: f.relative_to(MOD).as_posix(),
    )
    with zipfile.ZipFile(ZIP, "w") as z:
        for f in files:
            info = zipfile.ZipInfo(f.relative_to(MOD).as_posix(), TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, f.read_bytes(), compresslevel=9)
    print(f"Wrote {ZIP.name} ({len(files)} files, {ZIP.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
