# Ghost Pipes Codex — Chapter 01: The Manifest (v2.2)

> **Ground Truth Directive:** This set of documents constitutes the absolute physical "Ground Truth" for the Ghost Pipes project. It defines the physical existence, hardware specifications, and analog/digital I/O of all gear across the primary project islands. Physical hardware routing definitions in these documents must always be prioritized before any software logic, DAW configurations, or MIDI CC mappings.

This chapter was split from a single monolithic file (`GHOST_PIPES_CODEX_V1.9_CHAPTER_01.md`) into one file per section, for Obsidian linking and cleaner GitHub diffs. Link between them with `[[wikilinks]]` as the vault grows.

## Section index
- [[01.1-physical-instrument-manifest]] — The Analog Sources (strings, acoustic/mic sources, specialized electronics)
- [[01.2-mothership-and-sideboard]] — The Mothership + The Sideboard (floor processing island, signal chain)
- **1.3 The Acoustic Board — DELETED in v2.0.** The Martin X-Series' active/powered Fishman preamp doesn't mesh with this section's passive-gain-staged pedal chain (buffer/compressor/modeler built for weaker signal). See the Martin entry in [[01.1-physical-instrument-manifest]] and [[open-flags]] #1 for the still-unresolved replacement routing.
- [[01.4-killing-floor]] — Stage topology, standalone hardware, snake inputs
- [[01.5-anchor-rack]] — Rack mount infrastructure
- [[01.6-synth-bay]] — Desktop synth station
- [[01.7-workstation]] — "The Commodore" — physical nodes, wiring, full plugin manifest
- [[01.8-bridge]] — Global data routing, DIN highway, omniport network, stage snake mapping, master cabling manifest
- [[01.9-neural-ripple-concerns]] — Consolidated failure modes & operational ripple effects
- [[open-flags]] — Running list of unresolved decisions and unconfirmed assumptions across all sections

## Revision note
**v2.2 (October 2026)** supersedes v2.1. Only [[01.7-workstation]] Section III (plugin/software manifest) and [[open-flags]] changed: reconciled against the October 2026 Definitive Plugin & Software Update — ownership gaps closed, deployment state recorded (Ableton installed; third-party plugin deployment not yet begun), Tritik Krush restored, Neural DSP Mantra / Darkglass Ultimate removed from owned/committed lists, wishlist cleaned up, recovery map added. All physical hardware sections are unchanged.

**v2.1** rebuilt the 1.7.III plugin manifest against the curated Plug In Matrix (102 titles).

**v2.0** supersedes v1.9. Major structural changes: Acoustic Board (1.3) deleted; Morley ABC pedal and Dunlop expression pedal relocated from the Mothership to the Sideboard; Synth Bay controller lineup and vocal-processing chain overhauled; full plugin manifest rebuilt around a function-based "Ghost Pipes Personality Map" categorization. See [[open-flags]] for everything still unresolved.
