# BrainFly emergency source backup — 2026.09.19-0241

This branch is an emergency continuation point for BrainFly / BrainWorkbench Minecraft.

It intentionally does **not** contain personal/live mutable state:
- behavior/episodic/spatial/inventory memories
- live config
- logs
- snapshots
- giant connectome binaries / node_modules

The source backup archive is stored as Base64 chunks under `brainfly-backup/`.

To restore on Windows:
1. concatenate the `.b64.partXX` files in order;
2. decode Base64 to `BrainFly-0241-SOURCE-LIGHT.zip`;
3. verify SHA-256 `dc8ed23b1265273f29b83f9a585d09a7d6be40c4f590049db76d9422c580a5cf`;
4. unzip.

`COMMANDS.md` contains the command reference current at 0241.
