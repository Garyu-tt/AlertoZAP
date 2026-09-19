# BrainFly 0351 ROBUST DIG

Field fix after 0241.

Observed failure: `approached_raw -> dig_failed` while navigation itself was alive.

Fixes:
- live block refresh before digging;
- prefer already-reachable matching blocks;
- Mineflayer `canDigBlock()` reach check;
- vertical separation is included in navigation arrival check;
- bounded reposition before digging;
- raycast-face dig first, one bounded default-face fallback;
- timeout derived from live `bot.digTime()`;
- verify the block became air;
- shared by raw acquisition, wood harvesting, teacher break imitation and den mining;
- protected interactable blocks are never mined by robust-dig.

Tests: 23/23 JS regression tests pass.
Connectome smoke: N=165122, E=10511038, effective_edges=5016094, minecraft_motor_spike_delta=189.

Incremental patch SHA-256:
69c81bda7fcf5ee79d89a3a5eae9a71b6ac69acb7a427efc0f958e3a0e1f93a2

Source-light snapshot SHA-256:
7cf671df9ed14e33c6dd253a96f45ecd10941b5c0531fa77e2034c0c3dd9e72b

The exact 0241->0351 code diff is stored as gzip+base64 in `0241-to-0351-code.patch.gz.b64`.
Restore it with PowerShell:
```powershell
$b64 = Get-Content .\0241-to-0351-code.patch.gz.b64 -Raw
$gz = [Convert]::FromBase64String($b64)
[IO.File]::WriteAllBytes('.\0241-to-0351-code.patch.gz',$gz)
$in=[IO.File]::OpenRead('.\0241-to-0351-code.patch.gz')
$g=New-Object IO.Compression.GzipStream($in,[IO.Compression.CompressionMode]::Decompress)
$out=[IO.File]::Create('.\0241-to-0351-code.patch')
$g.CopyTo($out); $out.Close(); $g.Close(); $in.Close()
```
Then apply from a 0241 source tree with a compatible patch/git tool.
