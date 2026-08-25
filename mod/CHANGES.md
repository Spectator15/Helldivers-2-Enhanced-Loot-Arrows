# Helldivers 2 Enhanced Loot Arrows

## What changed

- Enlarged and thickened the existing in-game marker meshes, not the preview JPGs.
- Recolored marker vertex colors for stronger resource separation:
  Super Credits cyan, Medals gold, Requisition yellow, Common Samples green, Rare Samples orange, Super Samples violet.
- Made Super Credit and Medal marker icons the largest among the resource markers.
- Expanded understood LOD/culling bounds on patched marker units and set final LOD thresholds to 0.0 where the existing LOD group structure was clear.
- Added a separate two-player bunker warning patch for `content/env_super_earth/military_base/bunker_cache/bunker_cache`.

## Modified assets

- Existing option patches under `Credit`, `Medal`, `Requisition`, and `Sample` were edited in-place in this enhanced build.
- New patch: `Bunker Warning/9ba626afa44a3aa3.patch_14`.
- Bunker target unit: `0x5e04d526646ff79f` / `content/env_super_earth/military_base/bunker_cache/bunker_cache`.
- Shared texture/material option from the original mod is preserved.

## How the improved arrows work

The original mod replaces/extends real unit mesh data for loot resources. This build keeps those same target unit IDs and option folders, then scales the marker vertices directly in the `.gpu_resources` payloads. Tall arrows are widened without making them much taller; compact icons are enlarged so the silhouette survives at distance.

## How the bunker warning works

The real two-player bunker/cache unit was found in game archives as `content/env_super_earth/military_base/bunker_cache/bunker_cache`. Its small non-interactive sign mesh is rewritten into a large blocky `2P` plus an `X` billboard. The bunker body, physics, state machine, resources, pickups, currency values, networking, and gameplay behavior are not modified.

## Limitations

- This was verified by parsing the supplied mod patches and reconstructed Helldivers 2 archives with the HD2 SDK Community Edition file-format logic. Blender itself is not installed in this environment, so no Blender viewport/gameplay test was possible here.
- The warning marks the unique bunker cache unit, not the individual loot behind the door. That is intentional to avoid hiding normal loot incorrectly.
- If the game culls an entire POI or never spawns/streams a distant bunker unit client-side, a marker attached to that unit cannot render before the unit exists locally.

## Installation

Install this ZIP with the same Helldivers 2 mod manager/workflow used for the original Customizable Cheat Arrows mod. Keep the required `Texture` option enabled. Enable the resource marker options you want, plus `Two-Player Bunker Warning`.

## Build notes

- Loot unit patches changed: 30
- Marker vertices adjusted: 291511
- LOD groups/bounds touched: 106
- Bunker sign meshes rewritten: [(8, 88, 132), (7, 88, 132), (6, 88, 132)]
