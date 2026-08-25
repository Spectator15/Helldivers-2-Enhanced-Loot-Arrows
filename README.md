<h1 align="center">Helldivers 2 Enhanced Loot Arrows</h1>

<p align="center">A client-side visual mod for clearer Helldivers 2 loot markers, stronger resource colours, and an optional two-player bunker warning.</p>

---

## What this changes

This is an enhanced modification of the existing [Customizable Cheat Arrows](https://mods.rpghq.org/helldivers-2/176522) mod. It keeps the same general idea: visible arrows and icons above loot so resources are easier to spot at a glance.

The enhanced package changes real marker meshes rather than editing the preview JPGs. Arrows are thicker, important icons are larger, and resource colours are easier to distinguish from a distance.

The most prominent markers are for `Super Credits` and `Medals`, since those are usually the highest-priority pickups.

> [!NOTE]
> This is a visual quality-of-life mod. It does not grant resources, change currency values, alter progression, automate gameplay, modify networking, bypass anti-cheat, or change damage.

## Resource colour guide

| Resource | Colour | Relative size |
| --- | --- | --- |
| Super Credits | Cyan | Largest |
| Medals | Gold | Largest |
| Requisition Slips | Yellow | Standard |
| Common Samples | Green | Standard |
| Rare Samples | Orange | Standard |
| Super Samples | Violet | Standard |

## High and Low marker options

Each supported resource keeps the configurable option style from the original mod.

`High` markers extend into the sky for long-distance visibility. These are the best choice when you want to spot resources from far away.

`Low` markers remain closer to the resource icon. These are less visually tall and may be preferable if you want the screen to feel a little cleaner.

Keep the required `Texture` option enabled. It contains shared visual resources used by the marker options.

> [!IMPORTANT]
> **Texture is required.** Leave the **Texture** option enabled in your mod manager, even if you only enable one resource marker.

## Two-player bunker warning

Helldivers 2 can spawn loot behind two-player bunker/cache doors. When playing solo, those rewards may be visible but inaccessible.

The optional `Two-Player Bunker Warning` option marks the two-player bunker/cache unit itself. It rewrites the small sign mesh into a large blocky `2P` and `X`, making it visually separate from normal loot arrows.

This warning does not change bunker physics, loot, currency, networking, spawning, doors, buttons, or gameplay behaviour. It is only a client-side visual marker.

## Installation

The easiest installation method is to download [HD2 Arsenal from its official website](https://rsnl.gg/) and import the release ZIP there.

1. Download `Helldivers-2-Enhanced-Loot-Arrows.zip` from the [latest GitHub Release](https://github.com/Spectator15/Helldivers-2-Enhanced-Loot-Arrows/releases/latest).
2. Import the ZIP into Arsenal.
3. Keep the required **Texture** option enabled.
4. Choose `High` or `Low` options for the desired resources.
5. Optionally enable **Two-Player Bunker Warning**.
6. Apply or deploy it through Arsenal.

Do not install the repository source folder directly unless you know your mod manager expects an unpacked package. Normal users should use the ZIP attached to the latest release.

## Testing status

The enhanced Common Sample marker was confirmed working in-game.

The complete package was structurally verified using patch parsing and reconstructed Helldivers 2 archives. The verification checked archive integrity, path safety, `manifest.json`, package layout, patch readability, and preservation of binary payloads.

The remaining resource variations and the bunker warning have not all been individually confirmed through gameplay. Game updates may affect compatibility.

## Technical notes

Editable package contents live under `mod/`.

The release ZIP is not committed to the repository tree. It is attached to the GitHub Release as `Helldivers-2-Enhanced-Loot-Arrows.zip`.

Canonical release ZIP SHA-256:

```text
3A1749EDDAD437C1FE8E54A3A2C6536B65DBB27A26CE0A1D28F047CD3EE9754C
```

The two-player bunker target identified during inspection is:

```text
content/env_super_earth/military_base/bunker_cache/bunker_cache
```

The warning patch is:

```text
mod/Bunker Warning/9ba626afa44a3aa3.patch_14
```

## Attribution and permissions

This project is an enhanced modification of the existing [Customizable Cheat Arrows](https://mods.rpghq.org/helldivers-2/176522) mod.

I do not claim ownership of the original mod, preview images, shared texture option, Helldivers 2 assets, or game-derived files included in this package.

This project is unofficial and is not affiliated with Arrowhead Game Studios, Sony Interactive Entertainment, the original mod author, Arsenal, ModHQ, or the HD2 SDK Community Edition project.

No open-source licence is provided because this enhancement contains third-party mod assets and game-derived assets whose original licensing terms have not been verified.

## Disclaimer

Use Helldivers 2 mods at your own discretion. Compatibility can change after game updates, mod manager updates, or changes to the original asset format.

This repository is provided as an unofficial visual mod package for users who already understand the risks of modding Helldivers 2.
