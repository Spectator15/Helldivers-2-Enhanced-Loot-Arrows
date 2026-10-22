<h1 align="center">Helldivers 2 Enhanced Loot Arrows</h1>

<p align="center">Bigger, brighter loot markers so you never miss Super Credits, Medals or Samples again.</p>

<p align="center">
  <a href="https://github.com/Spectator15/Helldivers-2-Enhanced-Loot-Arrows/actions/workflows/validate.yml"><img alt="CI" src="https://github.com/Spectator15/Helldivers-2-Enhanced-Loot-Arrows/actions/workflows/validate.yml/badge.svg"></a>
  <img alt="Platform: PC" src="https://img.shields.io/badge/platform-PC-blue">
  <a href="#license-and-disclaimer"><img alt="License: none" src="https://img.shields.io/badge/license-none-lightgrey"></a>
</p>

---

## Quick start

1. Install [HD2 Arsenal](https://rsnl.gg/) if you don't have it.
2. Download [`Helldivers-2-Enhanced-Loot-Arrows.zip`](https://github.com/Spectator15/Helldivers-2-Enhanced-Loot-Arrows/raw/main/Helldivers-2-Enhanced-Loot-Arrows.zip) from the file list at the top of this page.
3. Import the ZIP into Arsenal.
4. Pick `High` or `Low` for each resource you want.
5. Optionally turn on **Two-Player Bunker Warning**.
6. Apply / deploy in Arsenal.

> [!NOTE]
> There are no GitHub Releases. The ZIP lives right in the repo's file list. Click it, then the download button. Don't use the green **Code → Download ZIP** button, because Arsenal won't recognise that layout.

> [!WARNING]
> **Keep the `Texture` option turned on.** Every marker depends on it, even if you only enable one resource.

## Why this exists

I loved the Customizable Cheat Arrows mod, but at a distance the arrows were thin and a lot of the colours looked alike. I wanted Super Credits and Medals to jump out, and every resource to be easy to tell apart at a glance.

I also kept running across the map solo to loot I could see behind two-player bunker doors and couldn't open. So I added a warning that marks those bunkers before you waste the trip.

## Components

| Name | What it does | Credit |
| --- | --- | --- |
| **Texture** *(required)* | Shared textures/materials used by every marker. | [Customizable Cheat Arrows](https://mods.rpghq.org/helldivers-2/176522) (original, unchanged) |
| **Super Credit** | Cyan marker, largest icon. `High` or `Low`. | Original mod, enhanced by Spectator15 |
| **Medal** | Gold marker, largest icon. `High` or `Low`. | Original mod, enhanced by Spectator15 |
| **Requisition Slips** | Yellow marker. `High` or `Low`. | Original mod, enhanced by Spectator15 |
| **Common Sample** | Green marker. `High` or `Low`. | Original mod, enhanced by Spectator15 |
| **Rare Sample** | Orange marker. `High` or `Low`. | Original mod, enhanced by Spectator15 |
| **Super Sample** | Violet marker. `High` or `Low`. | Original mod, enhanced by Spectator15 |
| **Two-Player Bunker Warning** *(optional)* | Big blocky `2P` + `X` sign on two-player bunker/cache units. | Spectator15 |

**High vs Low:** `High` arrows shoot up into the sky, which is best for spotting loot from far away. `Low` arrows sit just under the icon, so the screen stays cleaner.

## What it does

- Makes marker arrows thicker and icons larger.
- Gives each resource its own strong colour.
- Makes Super Credits and Medals the biggest markers, since they matter most.
- Keeps markers visible from further away.
- Optionally flags two-player bunkers so solo players can skip them.
- It's visual only. It does **not** grant resources, change values or progression, automate anything, touch networking or anti-cheat, or change damage.

<details>
<summary><b>How it works</b></summary>

- Edits the real in-game marker meshes (the `.gpu_resources` payloads), not the preview JPGs.
- Keeps the original mod's target units and option folders. Marker vertices are scaled directly.
- Tall arrows are widened without getting much taller. Small icons are enlarged so their shape holds up at distance.
- Marker vertex colours are recoloured for stronger separation.
- LOD/culling bounds are expanded on patched markers. Final LOD thresholds are set to `0.0` where the LOD structure was clear.
- **Bunker warning:** the small, non-interactive sign mesh on the bunker cache unit is rewritten into a large `2P` + `X` billboard. The bunker body, physics, doors, buttons, loot, spawning and networking are untouched.

</details>

<details>
<summary><b>Known limitations</b></summary>

- The bunker warning marks the bunker unit itself, not the loot behind the door. This is on purpose, so normal loot isn't hidden by mistake.
- If the game hasn't loaded a distant bunker yet, the warning can't show until it does.
- Game updates or Arsenal updates may break compatibility.

</details>

<details>
<summary><b>Testing status</b></summary>

- The Common Sample marker is confirmed working in-game.
- The full package was structurally checked: archive integrity, path safety, `manifest.json`, layout and patch readability.
- The other resource markers and the bunker warning haven't each been play-tested individually yet.

</details>

<details>
<summary><b>Technical reference</b></summary>

- **Supported platform:** PC, via HD2 Arsenal.
- **Two-player bunker target unit:** `0x5e04d526646ff79f` (`content/env_super_earth/military_base/bunker_cache/bunker_cache`)
- **Bunker warning patch:** `mod/Bunker Warning/9ba626afa44a3aa3.patch_14`
- **ZIP integrity:** CI checks that every file in the ZIP matches `mod/` byte-for-byte. All game patch files are the same as in the original v1.0.0 build.

</details>

## Development

- Everything that ships lives in [`mod/`](mod): `manifest.json`, the patch files, preview images and [`CHANGES.md`](mod/CHANGES.md).
- After changing anything in `mod/`, rebuild the ZIP: `python tools/build_zip.py`
- Check everything: `python tools/validate.py`. CI runs this on every push. It checks that `manifest.json` is valid, every option points to a complete patch set, every image exists, nothing is unused, and the ZIP matches `mod/`.

## License and disclaimer

- Made by **Spectator15**. Based on [Customizable Cheat Arrows](https://mods.rpghq.org/helldivers-2/176522). I don't own the original mod, its preview images, its shared texture, or any Helldivers 2 assets.
- **No open-source license.** This package includes third-party mod assets and game-derived files whose licensing hasn't been verified.
- Unofficial. Not affiliated with Arrowhead Game Studios, Sony Interactive Entertainment, the original mod author, Arsenal, ModHQ or the HD2 SDK Community Edition project.
- Mod at your own risk. Updates to the game or mod manager can break things.
