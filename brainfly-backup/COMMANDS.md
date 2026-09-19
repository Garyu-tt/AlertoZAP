# BrainFly Minecraft command reference — 2026.09.19-0241

Chat prefix: `!brain`

## Help / status
- `!brain help` — short built-in help.
- `!brain infra` / `!brain infrastructure` — world freeze state, navigation backend, active navigation lease, reconnect count, event-loop lag.
- `!brain nav` / `!brain nav status` — navigation backend and current navigation lease.
- `!brain nav cancel` — cancel current navigation immediately.
- `!brain stats` — teaching/behavior/episodic-memory summary.
- `!brain scene` — current perceived scene summary.
- `!brain chains` — top learned episodic transitions.

## Teaching / reinforcement
- `!brain teach` / `!brain teach me` / `!brain shadow` — enter teaching mode with the sender as teacher.
- `!brain auto` / `!brain teach off` / `!brain learn` — return to autonomy and save learned behavior/episodes.
- `!brain follow` — teaching mode + follow/joint attention.
- `!brain show` — remember the block under the teacher crosshair as a seek target.
- `!brain use` — manually mark a USE demonstration; if a teacher target block exists, schedule USE imitation.
- `!brain good` / `!brain yes` — reward recent episode.
- `!brain no` / `!brain bad` — aversive feedback to recent episode.
- `!brain radius N` — teacher observation radius, clamped to 4..96 blocks.
- `!brain event KIND OBJECT [COUNT]` — manually record an episodic event/token.
- `!brain forget demos` — CLEAR behavior + episodic demonstration memory. Destructive.

## Planning / goals / crafting
- `!brain inspect ITEM` — compile/display a plan only; do not execute it.
- `!brain plan ITEM` — compile canonical plan, set goal, and start execution.
- `!brain recipe ITEM` — show best known canonical recipe(s), material binding and crafting-table requirement.
- `!brain make ITEM` — set an item goal and start immediately.
- `!brain goal ITEM` — set a persistent goal and start immediately.
- `!brain goal status` — active goal, attempts, last reason, plan status/node count.
- `!brain goal replan` — rebuild the immutable bounded plan for the active goal.
- `!brain goal stop` / `!brain goal clear` — clear active goal.
- `!brain craft ITEM` — directly invoke recursive item acquisition/crafting for one item.
- `!brain craft status` — safe-crafting backend status and last fault/strategy.
- `!brain craft reset` — reset safe-crafting fault/quarantine and resume a paused goal.

## Overnight autonomous supervisor
- `!brain overnight` / `!brain overnight status` — overnight-autonomy status.
- `!brain overnight on` — enable overnight supervisor and write a checkpoint.
- `!brain overnight off` — disable overnight supervisor; memories remain.
- `!brain overnight checkpoint` — force a memory checkpoint.
- `!brain overnight capabilities` — report available autonomous capabilities.

## Innate Minecraft drive / progression
- `!brain destiny` / `!brain destiny status` — innate progression status.
- `!brain quest` / `!brain quest status` — alias for destiny status.
- `!brain destiny on` — enable innate Minecraft progression drive.
- `!brain destiny off` — disable innate progression drive; learned memory remains.
- `!brain destiny next` / `!brain quest next` — skip current innate objective and select the next one.
- `!brain advancements` / `!brain advancements status` — advancement completion summary.
- `!brain advancements missing [N]` — show up to N unfinished vanilla advancements (default 8, max 20).
- `!brain advancement ID` — show one advancement status and missing criteria.

## Inventory / equipment / interaction
- `!brain inventory` — show first inventory stacks.
- `!brain inventory skills` — learned equip/use/consume mapping counts.
- `!brain equip ITEM [SLOT]` — equip item; SLOT can be inferred or explicit.
- `!brain teach equip ITEM SLOT` — permanently learn equipment mapping, then attempt it. Slots: `head`, `torso`, `legs`, `feet`, `hand`, `off-hand`.
- `!brain eat [ITEM]` — force eating best food or preferred ITEM.
- `!brain useitem ITEM` — use an item from inventory.
- `!brain interact` / `!brain use block` — use the currently targeted block instead of attacking it.

## Spatial memory / home / den
- `!brain map stats` — spatial-memory size, block kinds/samples, trail, home.
- `!brain map nearest BLOCK` — nearest remembered sample of a block within 512 blocks.
- `!brain map block BLOCK` — alias of map-nearest lookup.
- `!brain home` / `!brain home status` — show remembered home/den state.
- `!brain home set` — set current position as home.
- `!brain home go` / `!brain home return` — navigate home.
- `!brain den` / `!brain den build` — request/start den construction.
- `!brain den status` — den progress/status.
- `!brain den stop` — pause den construction.

## Neuromod / experimental psychedelic state
- `!brain trip` — induce default state, intensity 0.6 for 300 s.
- `!brain trip INTENSITY [SECONDS]` — induce specified state; intensity clamped to 0.05..1.
- `!brain trip status` — current neuromod state.
- `!brain trip off` / `!brain trip baseline` / `!brain trip abort` — return physiology to baseline, retain learned state.
- `!brain trip afterglow` — enter afterglow state.
- `!brain trip rollback` — restore pre-trip snapshot.

## Inventory Link Fabric mod
- `/braininv` — open BrainFly's server-side inventory GUI.
- `/braininv BrainFly` — explicit target form.
- Sneak + right click BrainFly — alternate inventory-open interaction if the mod is installed/enabled.

## Recommended autonomous-night start
```
!brain auto
!brain goal stop
!brain destiny on
!brain overnight on
!brain infra
!brain overnight status
!brain destiny
```
