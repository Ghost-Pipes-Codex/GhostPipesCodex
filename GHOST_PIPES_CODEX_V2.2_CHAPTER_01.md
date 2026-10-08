# GHOST PIPES CODEX — CHAPTER 01: THE MANIFEST
## Project: Ghost Pipes | Version: v2.2 (compiled single-file edition)

> **Ground Truth Directive:** This document constitutes the absolute physical "Ground Truth" for the Ghost Pipes project. It defines the physical existence, hardware specifications, and analog/digital I/O of all gear across the primary project islands. Physical hardware routing definitions in this chapter must always be prioritized before any software logic, DAW configurations, or MIDI CC mappings.
>
> This is the compiled single-file edition of chapter-01, generated from the per-section source files in `/chapter-01` for tools (GPT, Gemini, etc.) that work best with one document rather than browsing multiple files. The per-section files in `/chapter-01` remain the actively-edited source; this file is regenerated from them each time chapter-01 is updated. If the two ever appear to disagree, the per-section `/chapter-01` files win.
>
> **v2.2 revision note (October 2026):** Supersedes v2.1. Only Section 1.7.III (the plugin/software manifest) and the Open Flags changed, reconciled against the October 2026 Definitive Plugin & Software Update: ownership gaps closed; deployment state recorded (Ableton Live installed on the Dell 7550, third-party plugin deployment not yet begun — ownership is tracked separately from installation/activation); Tritik Krush restored; FOCUS TIME, Scintillate, Retrospect, Gneiss (Free Tier), VRAC+, and Motion: Fractal (Full) resolved; Eventide Blackhole, Phase Fiasco KAZU, the Dan Mayo Everything Bundle, and Audiomodern Loopmix added as owned; UJAM Select 5 contents and MELLOW 2 resolved; hardware-bundled entitlements resolved as owned; Neural DSP Mantra and Darkglass Ultimate removed from the owned/committed lists (not owned); compact recovery map added. Open Flags #10–#13 updated, #14–#15 added. All physical hardware sections (1.1, 1.2, 1.4, 1.5, 1.6, 1.8, 1.9) are unchanged from v2.1.
>
> **v2.1 revision note (carried forward):** Supersedes v2.0. Only change from v2.0: Section 1.7.III (the plugin/VST manifest) has been rebuilt against a newly curated 102-title Plug In Matrix — ownership status corrected, ~35 previously-undocumented titles added, three items promoted from the wishlist to Owned (Baby Audio Atoms, United Plugins Relooper, BEATSURFING VRAC+), and several bundle-origin/naming discrepancies flagged for confirmation. See [[open-flags]] #13. All physical hardware sections (1.1, 1.2, 1.4, 1.5, 1.6, 1.8, 1.9) are unchanged from v2.0.
>
> **v2.0 revision note (carried forward):** v2.0 superseded v1.9. Major structural changes: Acoustic Board (1.3) deleted; Morley ABC pedal and Dunlop expression pedal relocated from the Mothership to the Sideboard; Synth Bay controller lineup and vocal-processing chain overhauled; full plugin manifest rebuilt around a function-based "Ghost Pipes Personality Map" categorization.

---


# 1.1 Physical Instrument Manifest (The Analog Sources)

This section establishes the definitive Physical Hardware "Ground Truth" for all sound-generating sources entering the system before any digital transformation occurs.

## I. Electric & Hybrid Stringed Instruments

### Fender Meteora (Primary Electric)
* **Hardware Type**: Solid-Body Electric Passive Analog Instrument Hardware
* **Physical Electronics**: Dual Fireball Humbuckers with physical S-1™ Coil-Split Switch
* **Physical Tuning**: Standard E-A-D-G-B-E Tuning Configuration
* **Physical I/O**: 1/4" Mono TS Output Hardware Jack
* **Ground Truth Path**: Physical instrument cable running from guitar output to the Morley ABC Pedal Input A **on the Sideboard** (relocated from the Mothership in v2.0 — see [[01.2-mothership-and-sideboard]])
* **Hardware Role**: Primary high-gain and textured industrial lead engine
* **Power Hardware**: N/A (Passive Analog Circuitry)
* **Status**: Owned Physical Asset

### Gretsch Electromatic Hollow Body
* **Hardware Type**: Hollow-Body Electric Passive Analog Instrument Hardware
* **Physical Electronics**: Dual Humbuckers utilizing Filter'Tron style physical architecture
* **Physical Tuning**: Open G (D-G-D-G-B-D) Tuning Configuration
* **Physical I/O**: 1/4" Mono TS Output Hardware Jack
* **Ground Truth Path**: Physical instrument cable running directly to the Morley ABC Pedal Input B **on the Sideboard** (relocated from the Mothership in v2.0 — see [[01.2-mothership-and-sideboard]])
* **Hardware Role**: Supplies harmonic resonance and slide-driven structural textures
* **Power Hardware**: N/A (Passive Analog Circuitry)
* **Status**: Owned Physical Asset

### Gold Tone Dojo-DLX
* **Hardware Type**: Deluxe Resonator Banjo with Magnetic Analog Instrument Hardware
* **Physical Electronics**: Stacked Single Coil Humbucker optimized for a hum-canceling physical stage environment
* **Physical Tactile Controls**: Body-mounted physical Volume Knob hardware
* **Physical Tuning**: Standard G-G-D-G-B-D Tuning Configuration
* **Physical I/O**: 1/4" Mono TS Output Hardware Jack
* **Ground Truth Path**: Physical instrument cable connects directly to the Morley ABC Pedal Input C **on the Sideboard** (relocated from the Mothership in v2.0 — see [[01.2-mothership-and-sideboard]])
* **Physical Hardware Specifications**: Flamed Maple body with physical cutaway, reverse-cone resonator, biscuit bridge, Maple neck, Rosewood fretboard (22 physical frets), and an installed physical Zero Glide Nut. Scale Length: 26-3/8" | Physical Weight: 6.3 lbs.
* **Hardware Role**: High-sustain hybrid engine blending raw acoustic banjo character with an industrial-ready magnetic hardware output
* **Power Hardware**: N/A (Passive Analog Circuitry)
* **Status**: Owned Physical Asset

## II. Acoustic & Mic-Based Sources

### Martin X-Series Special
* **Hardware Type**: Acoustic Guitar featuring Active Acoustic-Electric Hardware
* **Physical Electronics**: Integrated Active Fishman Hardware Preamp System
* **Physical Tuning**: Standard E-A-D-G-B-E Tuning Configuration
* **Physical I/O**: 1/4" Mono TS Output Hardware Jack
* **Ground Truth Path**: 🚩 **OPEN — see [[open-flags]] #1.** The Acoustic Board (formerly Section 1.3) has been removed in v2.0: the Martin's active/powered Fishman preamp doesn't mesh with that section's passive-gain-staged pedal chain (buffer/compressor/modeler built for weaker, unbuffered signal), so running it into that chain risked clipping the early stages. A replacement DI/preamp path has not yet been chosen. **Do not route this instrument through a passive multi-pedal chain built for weaker signals** — a dedicated DI (passive or active) suited to a hot, already-buffered active pickup is the right category of solution, exact hardware TBD.
* **Hardware Role**: Dedicated clean acoustic platform for roots-based textural contrast
* **Power Hardware**: Internal 9V Physical Battery Cell
* **Status**: Owned Physical Asset — signal path pending redesign

### Eastar Melodica / LP Maracas / Meinl Tambourine
* **Hardware Type**: Physical Acoustic Percussive and Wind Instruments
* **Physical Electronics**: N/A (Pure Acoustic Resonance)
* **Physical I/O**: Acoustic sound waves are physically captured via 2 Dual Shure SM57 microphone hardware units
* **Ground Truth Path**: Dedicated physical XLR cables run directly from the microphone bodies to physical Stage Snake Box Inputs 23 and 24
* **Hardware Role**: Primal, tactile, hand-played acoustic percussive elements
* **Power Hardware**: N/A (Fully Passive Acoustic Transduction)
* **Status**: Owned Physical Instruments

## III. Specialized Electronic & Satellite Hardware

### Stylophone Theremin
* **Hardware Type**: Touch-Sensitive Analog Drone Synthesizer Hardware
* **Physical Electronics**: Discrete Analog Pitch and Modulation Oscillator Hardware Circuits
* **Physical Mounting**: Physically mounted on a heavy microphone stand adjacent to the Mothership floor array
* **Physical I/O**: 1/4" Mono TS Output Hardware Jack
* **Ground Truth Path**: A physical instrument cable runs directly to physical Stage Snake Box Input 10, terminating as "Chaos/Synth" at the physical WING console
* **Hardware Role**: Generates volatile, real-time spatial manipulation and analog chaos drone textures
* **Power Hardware**: Dedicated DC Power Supply / Battery Hardware Enclosure
* **Status**: Owned Physical Asset

## IV. Internal Physical Cabling Manifest (The Analog Sources)
* **Component Item**: Local Instrument Connections Cable Bundle
* **Hardware Type**: High-Z Shielded Analog Interface Cables
* **Physical Elements**: 2x 1/4" Mono TS Instrument Cables (Meteora, Gretsch) — 🚩 length TBD, see [[open-flags]] #3. The prior 15–20ft spec was set when the pedalboard sat at the Mothership; now that the Morley ABC pedalboard has relocated to the Sideboard, the actual run length needs re-verification.
* **Ground Truth Path**: Physical lines connect the Fender Meteora and Gretsch guitars directly from their output jacks to the Morley ABC pedal on the Sideboard (see [[01.2-mothership-and-sideboard]]). The Dojo-DLX follows the same pattern to Morley ABC Input C. The Martin's cabling is separately unresolved — see the Martin entry above and [[open-flags]] #1.
* **Hardware Role**: Secure analog signal transmission paths blocking external stage RFI interference
* **Power Hardware**: N/A (Passive Copper Core Conductors)
* **Status**: Owned Physical Assets — length spec pending re-verification


---


# 1.2 The Mothership: Physical Hardware Manifest

This section establishes the definitive Physical Hardware "Ground Truth" for the primary processing island floor footprint.

## I. Command & Utility Hardware

> **v2.0 note:** The Morley ABC Pedal and the Dunlop DVP4 Mini Expression pedal have both relocated to [[#1.2.1 The Sideboard: Physical Hardware Manifest & Signal Chain|The Sideboard]] — see Section 1.2.1.I below. They are no longer part of the Mothership's on-board inventory.

### 29 Pedals EUNA
* **Hardware Type**: Input Buffer and Line Driver Analog Hardware
* **Physical Electronics**: High-Headroom Discrete Class-A Analog Buffer Circuitry
* **Physical I/O**: 1/4" Mono TS Input Jack / 1/4" Mono TS Output Jack
* **Ground Truth Path**: A physical 1/4" TS cable crosses the stage floor gap from the Sideboard-mounted Morley ABC pedal's output, terminating at the EUNA input on the Mothership (previously a short on-board cable when the Morley ABC lived on the Mothership; now a gap-crossing run — see [[open-flags]] #2 for the cable's cabling-manifest registration in [[01.8-bridge]])
* **Hardware Role**: Base signal shaper and input line driver to eliminate cable capacitance loading
* **Power Hardware**: 9VDC / 120mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Pigtronix Tuner
* **Hardware Type**: Chromatic Tuning and System Mute Digital Hardware
* **Physical Electronics**: High-Visibility LED Matrix Tracking Circuitry
* **Physical I/O**: 1/4" Mono TS Input Jack / 1/4" Mono TS Output Jack
* **Ground Truth Path**: Physical cable links the EUNA output directly to the input of the tuner
* **Hardware Role**: Provides precise pitch tracking and acts as a global physical system mute switch
* **Power Hardware**: 9VDC / 100mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Morningstar ML10X #1 (The Mono Forge)
* **Hardware Type**: Reconfigurable Matrix Switcher Hardware with Digital Control and an Analog Path
* **Physical Electronics**: High-Headroom Pure Analog Solid-State Routing Matrix
* **Physical I/O**: 5x Stereo TRS Hardware Jacks (Configured as independent Tip/Ring Split Mono Loops)
* **Ground Truth Path**: Input fed via physical patch cable from the Pigtronix Tuner output; loops breakout via custom insert cables to gain pedals
* **Hardware Role**: Houses the dynamic automation and automated matrix loop switching engine for mono gain stages
* **Power Hardware**: 9VDC / 160mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Morningstar ML10X #2 (The Atmosphere)
* **Hardware Type**: Reconfigurable Matrix Switcher Hardware with Digital Control and an Analog Path
* **Physical Electronics**: Stereo-Linked High-Headroom Analog Routing Matrix
* **Physical I/O**: 5x Stereo TRS Hardware Jacks (Operating in full stereo spatial processing mode)
* **Ground Truth Path**: Physical loop connections send/return to the stereo delay, reverb, and modulation hardware blocks
* **Hardware Role**: Directs automated routing, spatial placement, and ambient texture parallel matrices
* **Power Hardware**: 9VDC / 160mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Boss IR-2
* **Hardware Type**: Amplifier Simulator and Cabinet Impulse Response DSP Hardware
* **Physical Electronics**: High-Resolution 32-bit Floating-Point Digital Signal Processing Hardware
* **Physical I/O**: 1/4" Mono Input, TRS Stereo Return, Mono Send, Dual Mono Output Hardware Jacks
* **Ground Truth Path**: Input jack receives output from ML10X #1; Send and Return jacks intercept the entire ML10X #2 stereo matrix
* **Hardware Role**: Central analog amplifier profile simulator and primary stereo splitter module
* **Power Hardware**: 9VDC / 160mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Morningstar MC6 Pro
* **Hardware Type**: Master Performance MIDI Controller Hardware Engine
* **Physical Electronics**: High-Speed Microprocessor Controller with Dual Color LCD Screen Hardware displays
* **Physical I/O**: 2x 5-Pin DIN MIDI, 4x Omniports (1/4" TRS Multi-Protocol Hardware Jacks), USB-C, 3.5mm MIDI
* **Ground Truth Path**: 5-Pin DIN Out drives the main MIDI line; Omniport 1 connects to expression (now the Dunlop pedal on the Sideboard via a gap-crossing cable — see 1.2.1.I below); Omniport 2 interfaces with the Sideboard
* **Hardware Role**: Command station executing all automated preset changes, matrix shifts, and MIDI clock sync routing
* **Power Hardware**: 9VDC / 500mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### MIDI Solutions Quadra Thru
* **Hardware Type**: Active MIDI Data Distribution Through Box Hardware
* **Physical Electronics**: Optoisolated Active Data Signal Regeneration Circuits
* **Physical I/O**: 1x 5-Pin DIN Input Hardware Port / 4x 5-Pin DIN Output Hardware Ports
* **Ground Truth Path**: Input jack connects via physical 5-pin DIN cable directly to the Morningstar MC6 Pro MIDI OUT jack
* **Hardware Role**: Splits the master controller output into four distinct physical lanes to eliminate data jitter
* **Power Hardware**: Active MIDI-line voltage drawn directly from the host controller circuit
* **Status**: Owned Physical Asset

### AV Access U2EX60 (Mothership Send Node)
* **Hardware Type**: USB-over-Cat6 Local Hardware Extender Transmitter
* **Physical Electronics**: High-Bandwidth Digital Single-Ended Extender Core
* **Physical I/O**: 1x USB Type-B Input Port / 1x RJ45 Ethernet Output Hardware Jack
* **Ground Truth Path**: Receives short physical USB line from the MC6 Pro, outputting across the stage floor via a 25ft Cat6 umbilical trunk
* **Hardware Role**: Bridges long-distance performance data control lines directly to the computer table
* **Power Hardware**: USB Bus Voltage Driven from connected host interface
* **Status**: Owned Physical Asset

### Mothership Saturnworks Bridge
* **Hardware Type**: Passive System Interface Junction Box Hardware
* **Physical Electronics**: Point-to-Point Hand-Wired Shielded Direct Audio Pass-Through Ports
* **Physical I/O**: Multi-Channel 1/4" TRS Audio and Control Pass-Through Hardware Jacks
* **Ground Truth Path**: Input jacks receive the final combined stereo output lines from the Boss IR-2 simulator
* **Hardware Role**: Central strain-relief anchor point matching the master umbilical stage loom connection
* **Power Hardware**: N/A (Fully Passive Shielded Enclosure)
* **Status**: Owned Physical Asset

### Fender Engine Room LVL 12 (x2)
* **Hardware Type**: High-Capacity Isolated Multi-Output DC Power Supply Hardware
* **Physical Electronics**: Independent Toroidal Transformer Isolation Power Regulation Circuits
* **Physical I/O**: 12 Clean Isolated DC Output Hardware Ports per individual chassis unit
* **Ground Truth Path**: Distributes physical DC power lines throughout the entire Mothership command and loop array
* **Hardware Role**: Supplies ripple-free, isolated voltage to protect the high-gain floor audio architecture from mains noise
* **Power Hardware**: 120VAC Mains Input via standard physical IEC connector
* **Status**: Owned Physical Assets

## II. Mono Forge (ML10X #1) Hardware Loop Inventory

### Wampler Ego 76
* **Hardware Type**: Studio-Style Parallel Compressor Analog Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop A-Tip Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Black = Tip)
* **Hardware Role**: Tames aggressive transients and provides parallel dynamic compression for stringed instruments
* **Power Hardware**: 9VDC / 30mA Isolated Power Connection
* **Status**: Owned Physical Asset

### TC Sub 'N' Up Mini
* **Hardware Type**: Monophonic/Polyphonic Sub-Octave DSP Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop A-Ring Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Red = Ring)
* **Hardware Role**: Generates heavy sub-bass tracking to provide aggressive mechanical girth
* **Power Hardware**: 9VDC / 100mA Isolated Power Connection
* **Status**: Owned Physical Asset

### EHX Pico Atomic Cluster
* **Hardware Type**: Spectral Decomposition and Ring-Modulation Glitch DSP Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop B-Tip Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Black = Tip)
* **Hardware Role**: Reduces frequency resolution to generate resonant oscillations directly related to input signal for unstable harmonic degradation and rhythmic glitch textures
* **Power Hardware**: 9VDC / 100mA Isolated Power Connection
* **Status**: Owned Physical Asset

### JHS Prestige
* **Hardware Type**: Discrete Clean Boost and Buffer Analog Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop B-Ring Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Red = Ring)
* **Hardware Role**: Serves as an always-on line driver or discrete solo booster to push down-chain gain stages
* **Power Hardware**: 9VDC / 10mA Isolated Power Connection
* **Status**: Owned Physical Asset

### JHS Crayon
* **Hardware Type**: Compact British Console Style Overdrive/Preamp Analog Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop C-Tip Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Black = Tip)
* **Hardware Role**: Supplies a lo-fi overdrive profile, serving as the "Trash Foundation" sonic layer
* **Power Hardware**: 9VDC / 12mA Isolated Power Connection
* **Status**: Owned Physical Asset

### JHS Hard Drive
* **Hardware Type**: Surgical Industrial High-Gain Distortion Analog Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop C-Ring Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Red = Ring)
* **Hardware Role**: Primary heavy high-gain generator for aggressive industrial riff tracking
* **Power Hardware**: 9VDC / 78mA Isolated Power Connection
* **Status**: Owned Physical Asset

### EHX Big Muff Pi 2
* **Hardware Type**: Saturated Harmonics Sustainer Fuzz Analog Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop D-Tip Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Black = Tip)
* **Hardware Role**: Delivers compressed, high-saturation fuzz for shoegaze walls-of-sound
* **Power Hardware**: 9VDC / 5mA Isolated Power Connection
* **Status**: Owned Physical Asset

### Boss OD-200
* **Hardware Type**: MIDI-Hybrid Gain Multi-Circuit Distortion Hardware Processor
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop D-Ring Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Red = Ring)
* **Hardware Role**: Programmatically swaps gain structures via automated performance MIDI recall automation
* **Power Hardware**: 9VDC / 220mA Isolated Power Connection
* **Status**: Owned Physical Asset

### EHX Pico Deep Freeze
* **Hardware Type**: Sound Retainer and Continuous Glitch Sustainer DSP Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #1 Loop E-Tip Breakout Port
* **Ground Truth Path**: Linked via custom physical color-coded breakout insert cable (Black = Tip)
* **Hardware Role**: Freezes active signal audio blocks to build massive under-layer drone pads
* **Power Hardware**: 9VDC / 100mA Isolated Power Connection
* **Status**: Owned Physical Asset

## III. The Atmosphere (ML10X #2) Hardware Inventory

### TC Mimiq Doubler
* **Hardware Type**: Stereo Multi-Tracker Real-Time Double Tracking DSP Hardware Pedal
* **Physical Matrix Insertion**: Morningstar ML10X #2 Loop A Port (True Stereo TRS Connection)
* **Ground Truth Path**: Wired using dedicated physical dual-mono split internal patch routing
* **Hardware Role**: Generates subtle timing offsets to split the mono path into an ultra-wide physical stereo field
* **Power Hardware**: 9VDC / 100mA Isolated Power Connection
* **Status**: Owned Physical Asset

### Strymon Mobius
* **Hardware Type**: High-Resolution Multi-Modulation DSP Hardware Effects Processor
* **Physical Matrix Insertion**: Morningstar ML10X #2 Loop B Port (True Stereo TRS Connection)
* **Ground Truth Path**: Wired using dedicated physical dual-mono split internal patch routing
* **Hardware Role**: Executes high-fidelity phase, flanging, and rotary filtering spatial modulation profiles
* **Power Hardware**: 9VDC / 300mA Isolated Power Connection
* **Status**: Owned Physical Asset

### Red Panda Particle 2
* **Hardware Type**: Granular Delay and Pitch-Shifting DSP Hardware Effects Processor
* **Physical Matrix Insertion**: Morningstar ML10X #2 Loop C Port (True Stereo TRS Connection)
* **Ground Truth Path**: Wired using dedicated physical dual-mono split internal patch routing
* **Hardware Role**: Chops incoming audio blocks into real-time granular fragments and pitch-shifted clouds
* **Power Hardware**: 9VDC / 250mA Isolated Power Connection
* **Status**: Owned Physical Asset

### Boss DD-500
* **Hardware Type**: Advanced Multi-Mode Digital Delay DSP Hardware Studio Processor
* **Physical Matrix Insertion**: Morningstar ML10X #2 Loop D Port (True Stereo TRS Connection)
* **Ground Truth Path**: Wired using dedicated physical dual-mono split internal patch routing
* **Hardware Role**: Manages complex time divisions, rhythmic repeats, and high-precision processing with carryover spillover trails
* **Power Hardware**: 9VDC / 200mA Isolated Power Connection
* **Status**: Owned Physical Asset

### Boss RV-500
* **Hardware Type**: Advanced Dual-Engine Reverberation DSP Hardware Studio Processor
* **Physical Matrix Insertion**: Morningstar ML10X #2 Loop E Port (True Stereo TRS Connection)
* **Ground Truth Path**: Wired using dedicated physical dual-mono split internal patch routing
* **Hardware Role**: Generates deep, localized ambient spaces and non-linear shoegaze reverb decay with custom MIDI CC automation mapping
* **Power Hardware**: 9VDC / 225mA Isolated Power Connection
* **Status**: Owned Physical Asset

## IV. Internal Physical Cabling Manifest (The Command & Processing Array)
* **Component Item**: Localized Internal Patch and Power Cable Management Array
* **Hardware Type**: High-Fidelity Shielded Core Patch Cord Routing Infrastructure
* **Physical Elements**: 10x 1/4" TRS to Dual TS Insert Cables (1ft-2ft, Black=Tip, Red=Ring); 15x 1/4" Mono TS Patch Cables (6in-1ft); 15x DC Barrel Power lines
* **Ground Truth Path**: Routes all inputs, matrix breakouts, interconnect loops, and Fender supply taps within the Mothership base perimeter
* **Hardware Role**: Handles internal board interconnections, power distribution, and matrix signal shielding
* **Power Hardware**: Driven directly from the onboard Fender Engine Room chassis infrastructure
* **Status**: 100% Owned Physical Wiring Inventory

---

# 1.2.1 The Sideboard: Physical Hardware Manifest & Signal Chain

This section establishes the terminal "Floor Station" hardware components, interconnective tissue, and the final physical exit path leading to the Behringer WING rack console. **v2.0: now also the entry point for the Meteora, Gretsch, and Dojo-DLX — see the relocated Morley ABC Pedal below.**

## I. Sideboard Hardware Inventory

### Morley ABC Pedal — relocated from the Mothership in v2.0
* **Hardware Type**: Passive Instrument Selector Analog Hardware Switcher
* **Physical Electronics**: Mechanical True-Bypass Passive Switch Matrix
* **Physical I/O**: 3x 1/4" Mono TS Input Jacks / 1x 1/4" Mono TS Output Jack
* **Ground Truth Path**: Receives physical instrument cables directly from the Meteora (A), Gretsch (B), and Dojo-DLX (C) — these instruments now plug in at the Sideboard first. The switched output then crosses the stage floor gap via a 1/4" TS cable to reach the 29 Pedals EUNA input on the Mothership (see [[01.2-mothership-and-sideboard#29 Pedals EUNA|EUNA entry above]] and the cabling registration in [[01.8-bridge]]). **Note:** this crossing carries an unbuffered high-Z passive-switched instrument signal over a longer run than the pre-v2.0 layout — a shielded, low-capacitance cable is recommended given the distance.
* **Hardware Role**: Master instrument switching router to select the active physical performance asset
* **Power Hardware**: N/A (Fully Passive Mechanical Switching)
* **Status**: Owned Physical Asset

### Dunlop DVP4 Mini Expression — relocated from the Mothership in v2.0
* **Hardware Type**: Continuous Variable Parameter Control Hardware Pedal
* **Physical Electronics**: High-Durability Linear Passive Potentiometer Hardware Component
* **Physical I/O**: 1/4" TRS Expression Output Hardware Jack
* **Ground Truth Path**: TRS cable now crosses the board gap (Techflex-sleeved mini umbilical, same style as the Omniport 2→RC-500 line) to reach Omniport 1 on the Mothership-based MC6 Pro
* **Hardware Role**: Translates physical foot sweeps into MIDI CC expression automation
* **Power Hardware**: N/A (Fully Passive Linear Circuitry)
* **Status**: Owned Physical Asset

### Sideboard Saturnworks Bridge
* **Hardware Type**: Passive Signal Interface and Junction Box Hardware Enclosure
* **Physical Electronics**: Point-to-Point Internal Isolated Multi-TRS Conductors
* **Physical I/O**: Multi-Channel 1/4" TRS Stereo Audio & TRS Control Pass-Through Ports
* **Ground Truth Path**: Receives cross-board physical signals straight out of the master umbilical floor loom
* **Hardware Role**: Incoming strain-relief module protecting the Sideboard terminal processors
* **Power Hardware**: N/A (Fully Passive Structural Interface)
* **Status**: Owned Physical Asset

### Boss SL-2 Slicer
* **Hardware Type**: Rhythmic Audio Chopper and Percussive Splice DSP Hardware Pedal
* **Physical Electronics**: Dual-Engine High-Speed Digital Pattern Chopping Circuitry
* **Physical I/O**: Dual 1/4" TRS Stereo Inputs / Dual 1/4" TRS Stereo Outputs, TRS MIDI Input Hardware Jack
* **Ground Truth Path**: Input lines travel from Sideboard Bridge; output lines connect directly to the Boss RC-500 looper inputs
* **Hardware Role**: Implements complex rhythmic panning, gating, and slicing effects across the master stereo image
* **Power Hardware**: 9VDC / 60mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Boss RC-500
* **Hardware Type**: Master Advanced Dual-Track Performance Looper Hardware Engine
* **Physical Electronics**: Premium 32-bit AD/DA Digital Signal Processing Core Circuitry
* **Physical I/O**: Stereo 1/4" TS Inputs/Outputs, Stereo Balanced XLR Microphone Input, TRS MIDI Ports
* **Ground Truth Path**: Inputs fed via physical patch lines from the Boss SL-2 outputs; outputs connect directly to the Walrus DI inputs
* **Hardware Role**: Master phrase looper and real-time capture node for live sound layering with buffered bypass
* **Power Hardware**: 9VDC / 170mA Isolated DC Power Port
* **Status**: Owned Physical Asset

### Walrus Audio Canvas Stereo
* **Hardware Type**: Passive Stereo Direct Box and Line Isolator Output Hardware Enclosure
* **Physical Electronics**: Custom-Molded Permalloy Physical Audio Isolation Transformers
* **Physical I/O**: Dual 1/4" TS High-Z Inputs / Balanced Dual Stereo XLR Output Hardware Jacks
* **Ground Truth Path**: High-impedance inputs receive TS lines from the RC-500; XLR outputs interface with the Floor Snake
* **Hardware Role**: Balances the final master stereo instrument line and matches impedance for long-distance console routing
* **Power Hardware**: N/A (Fully Passive Transformer Isolation)
* **Status**: Owned Physical Asset — **purchased in v2.0** (previously PENDING PURCHASE)

> **v2.0 note:** Boss EV-30 (Advanced Dual-Expression Passive Parameter Control Pedal) has been removed from the Sideboard inventory entirely, with no replacement.

> **v2.0 note:** Vires Supply (local Sideboard power distribution block) remains PENDING PURCHASE Requisition Target — unchanged.

## II. Physical Signal Chain & Umbilical Logic
1. **Physical Instrument Entry (v2.0 — relocated)**: Input patch lines originating from the Meteora, Gretsch, and Dojo-DLX terminate directly into physical ports A, B, and C of the Morley ABC Pedal, now mounted on the **Sideboard**.
2. **Physical Gap Crossing (v2.0 — new step)**: The Morley ABC's switched output crosses the stage floor gap via a 1/4" TS cable, terminating at the 29 Pedals EUNA input on the **Mothership**.
3. **Physical Hardware Mute**: A physical jumper cable carries the EUNA signal into the input jack of the Pigtronix Tuner, establishing a dedicated master system mute.
4. **Physical Mono Forge Input**: A physical patch line carries the un-muted instrument signal from the tuner directly into the analog input of Morningstar ML10X #1.
5. **Physical Pre-Amp Drive**: A physical patch line routes the automated output configuration of ML10X #1 straight into the main front instrument input jack of the Boss IR-2 simulator.
6. **Physical Effects Loop (Send)**: A physical mono instrument cable routes the Boss IR-2 Send hardware port directly into the main analog input of Morningstar ML10X #2.
7. **Physical Stereo Split**: The analog path encounters the TC Mimiq Doubler within the parallel matrix loop, splitting the physical routing into a distinct spatial hardware stereo field.
8. **Physical Effects Loop (Return)**: A physical TRS stereo patch line routes the final processed ambient mix from ML10X #2 directly back into the Return hardware jack of the Boss IR-2.
9. **Physical Mothership Output**: Discrete physical TS cables carry the stereo outputs of the Boss IR-2 into a specialized Dual-TS to TRS Y-cable connector.
10. **Physical Mothership Bridge**: The consolidated TRS hardware end of the Y-cable docks directly into the physical Mothership Saturnworks Bridge port.
11. **Physical Umbilical Trunk**: Shielded lines and data lines cross the floor gap bundled inside a rugged, Techflex-sleeved hardware umbilical loom to terminate at the Sideboard Saturnworks Bridge.
12. **Physical Sideboard Audio Routing**: Clean stereo paths exit the Sideboard bridge, routing sequentially through the physical pattern engines of the Boss SL-2 Slicer and directly into the input ports of the Boss RC-500 Master Looper.
13. **Physical Terminal Transformation**: Balanced TS cables route the finalized loop performance from the outputs of the RC-500 directly into the high-impedance inputs of the Walrus Canvas Stereo DI box.
14. **Physical Console Connection**: Shielded physical XLR stage cables exit the Walrus Canvas Stereo outputs, entering the floor box of the SACB-24x8x25 Stage Snake to terminate at the rear of the Behringer WING Rack console.

> Note: steps 1–2 above are new in v2.0, adding a second gap-crossing (the raw switched instrument signal) alongside the pre-existing crossing at step 11 (the final processed stereo mix via the main umbilical trunk).


---


# 1.4 The Killing Floor: Physical Hardware Manifest & Stage Topology

This section establishes the definitive conflict-free Physical Hardware "Ground Truth" for the entire main performance floor space.

## I. The Nerve Center: The Floor Snake
* **Seismic Audio SACB-24x8x25**: 24-Channel Low-Profile XLR PCB Stage Snake Box **Hardware** unit. It features a 25-foot heavy-duty shielded multi-core **Physical** trunk line running across the performance surface to hook directly into the rear input preamps of the **Hardware** Behringer WING Rack Digital Engine.

## II. Standalone Hardware Inventory

### SOLOMON MiCS LoFreq (Kick Drum - External)
* **Hardware Type**: Low-Frequency Dynamic Acoustic Transducer Sub-Microphone Hardware
* **Physical Electronics**: Large-Diaphragm Heavy-Coil Dynamic Transduction Circuit
* **Physical I/O**: Integrated Balance Mono XLR Output Hardware Port
* **Ground Truth Path**: Direct **Physical** XLR cable connection routing from front external drum head axis to Stage Snake Box Input 1
* **Hardware Role**: Captures visceral low-end sub frequencies and fundamental pressure waves from the acoustic kick drum
* **Power Hardware**: N/A (Fully Passive Dynamic Coil Transduction)
* **Status**: PENDING PURCHASE Requisition Target

### Shure BETA 91A (Kick Drum - Internal)
* **Hardware Type**: Half-Cardioid Boundary Condenser Microphone Hardware
* **Physical Electronics**: High-Headroom Integrated Preamplifier and Boundary Condenser Capsule
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Direct **Physical** XLR cable connection routing from the internal drum shell interior to Stage Snake Box Input 2
* **Hardware Role**: Captures sharp mechanical transient attack and high-frequency beater click inside the kick drum
* **Power Hardware**: 48V Phantom Power delivered via WING console hardware rails
* **Status**: PENDING PURCHASE Requisition Target

### Audix F9 (Hi-Hat)
* **Hardware Type**: Small-Diaphragm Pre-Polarized Condenser Microphone Hardware
* **Physical Electronics**: Low-Mass Condenser Capsule Element with Cardioid Polar Pattern
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Rugged **Physical** XLR microphone line routing from high-hat stand axis straight to Stage Snake Box Input 3
* **Hardware Role**: Isolates crisp mechanical metal sizzle and complex high-frequency stick definitions
* **Power Hardware**: 48V Phantom Power delivered via WING console hardware rails
* **Status**: PENDING PURCHASE Requisition Target

### Audix F9 (Overhead L)
* **Hardware Type**: Small-Diaphragm Pre-Polarized Condenser Microphone Hardware
* **Physical Electronics**: Low-Mass Condenser Capsule matched for stereo cymbal tracking
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Matched stereo-paired **Physical** XLR line routing from left overhead cymbal axis to Stage Snake Box Input 4
* **Hardware Role**: Captures wide-field acoustic cymbal resonance, transient air, and overall drum kit spatial depth
* **Power Hardware**: 48V Phantom Power delivered via WING console hardware rails
* **Status**: PENDING PURCHASE Requisition Target

### Audix F9 (Overhead R)
* **Hardware Type**: Small-Diaphragm Pre-Polarized Condenser Microphone Hardware
* **Physical Electronics**: Low-Mass Condenser Capsule matched for stereo cymbal tracking
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Matched stereo-paired **Physical** XLR line routing from right overhead cymbal axis to Stage Snake Box Input 5
* **Hardware Role**: Completes the stereo field overhead capture to provide accurate stereo image panning
* **Power Hardware**: 48V Phantom Power delivered via WING console hardware rails
* **Status**: PENDING PURCHASE Requisition Target

### Audix F2 (Tom 1)
* **Hardware Type**: Dynamic Instrument Percussion Microphone Hardware
* **Physical Electronics**: Low-Mass Moving Coil Element featuring Hypercardioid isolation
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Secure **Physical** XLR microphone line routing from Rack Tom mount to Stage Snake Box Input 6
* **Hardware Role**: Captures fundamental midrange body and punchy decay behaviors from Tom 1
* **Power Hardware**: N/A (Fully Passive Dynamic Circuitry)
* **Status**: PENDING PURCHASE Requisition Target

### Audix F2 (Tom 2)
* **Hardware Type**: Dynamic Instrument Percussion Microphone Hardware
* **Physical Electronics**: Low-Mass Moving Coil Element featuring Hypercardioid isolation
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Secure **Physical** XLR microphone line routing from Floor Tom frame to Stage Snake Box Input 7
* **Hardware Role**: Captures fundamental low-mid punch and resonant sustain from Tom 2
* **Power Hardware**: N/A (Fully Passive Dynamic Circuitry)
* **Status**: PENDING PURCHASE Requisition Target

### Audix F5 (Bottom Snare)
* **Hardware Type**: Snare Drum Dynamic Instrument Microphone Hardware
* **Physical Electronics**: High-SPL Moving Coil Capsule with Hypercardioid off-axis rejection
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Shielded **Physical** XLR microphone line routing from lower snare rim stand to Stage Snake Box Input 8
* **Hardware Role**: Tracks volatile physical rattle textures and snappy wire responses from the snare bottom snares
* **Power Hardware**: N/A (Fully Passive Dynamic Circuitry)
* **Status**: PENDING PURCHASE Requisition Target

### Shure BETA 57 (Top Snare)
* **Hardware Type**: High-Output Dynamic Instrument Microphone Hardware
* **Physical Electronics**: Premium Neodymium Magnet Moving Coil Element for clean transient isolation
* **Physical I/O**: Integrated Balanced Mono XLR Output Hardware Port
* **Ground Truth Path**: High-grade **Physical** XLR cable connection routing from top snare rim cluster straight to Stage Snake Box Input 9
* **Hardware Role**: Core tracking module for crisp wood rim-shots, transient crack, and basic snare body weight
* **Power Hardware**: N/A (Fully Passive Dynamic Circuitry)
* **Status**: PENDING PURCHASE Requisition Target

### Stylophone Theremin Node
* **Hardware Type**: Space-Control Satellite Instrument Audio Feed
* **Physical Electronics**: Local Variable Frequency Heterodyning Oscillator Output Core
* **Physical I/O**: 1/4" Mono TS Output Hardware Line
* **Ground Truth Path**: Intercepted at the stand mount via a **Physical** 1/4" Mono TS to XLR breakout cable routing straight to Stage Snake Box Input 10
* **Hardware Role**: Delivers raw satellite performance noise data directly to the FOH mixing block
* **Power Hardware**: Powered via local standalone cell grid battery infrastructure
* **Status**: 100% Owned Physical Asset Node

### Snake Inputs 11/12 — 🚩 OPEN / UNASSIGNED (see [[open-flags]] #5)
* **v2.0 note**: Formerly "DSM Simplifier Acoustic Feed (Left/Right)," fed from the Acoustic Board (deleted in v2.0 — see [[01.1-physical-instrument-manifest]] Martin entry). These inputs are held open and unassigned pending the Martin's replacement DI routing decision. Do not reassign until that's resolved.

### Walrus Canvas Stereo DI Feed (Left)
* **Hardware Type**: Master Isolated Line-Level Balanced System Interconnect Path
* **Physical Electronics**: Permalloy Isolation Transformer Shielded Core
* **Physical I/O**: Balanced Male XLR Hardware Chassis Output Port
* **Ground Truth Path**: Direct **Physical** balanced XLR cable connection routing from Output L of the Sideboard array straight to Stage Snake Box Input 13
* **Hardware Role**: Forwards left-channel master processed guitar rig audio safely to the WING engine rails with zero hum
* **Power Hardware**: Fully passive line-isolated core transformer architecture
* **Status**: PENDING PURCHASE Requisition Target

### Walrus Canvas Stereo DI Feed (Right)
* **Hardware Type**: Master Isolated Line-Level Balanced System Interconnect Path
* **Physical Electronics**: Permalloy Isolation Transformer Shielded Core
* **Physical I/O**: Balanced Male XLR Hardware Chassis Output Port
* **Ground Truth Path**: Direct **Physical** balanced XLR cable connection routing from Output R of the Sideboard array straight to Stage Snake Box Input 14
* **Hardware Role**: Forwards right-channel master processed guitar rig audio safely to the WING engine rails with zero hum
* **Power Hardware**: Fully passive line-isolated core transformer architecture
* **Status**: PENDING PURCHASE Requisition Target

### Snake Input 15 — 🚩 OPEN / UNASSIGNED (see [[open-flags]] #6)
* **v2.0 note**: Formerly the Roland SPD-One Kick (heavy-duty electronic trigger percussion pad), which has been removed from inventory entirely. This input defaults to the same open/unassigned convention as Inputs 17–22 unless a replacement kick trigger is chosen.

### Phone Receiver Microphone
* **Hardware Type**: Lo-Fi Carbon-Capsule Vocal Transducer Performance Microphone Hardware
* **Physical Electronics**: Rewired High-Impedance Carbon Capsule Element modified for live stage applications
* **Physical I/O**: Custom hardwired physical Mono XLR Male Output tail connection
* **Ground Truth Path**: Heavy-grade **Physical** XLR microphone cable routing from stand location straight to Stage Snake Box Input 16
* **Hardware Role**: Core vocal transducer for harsh, distorted, rusted industrial vocal delivery
* **Power Hardware**: Passive Dynamic/Carbon element tracking (No phantom power permitted)
* **Status**: Owned Physical Asset

### Snake Inputs 17 – 22
Open **Physical** hardware lines reserved with unassigned status to allow for future stage infrastructure expansion.

### Shure SM57 (Percussion L)
* **Hardware Type**: Professional Cardioid Dynamic Instrument Microphone Hardware
* **Physical Electronics**: Mid-Heavy Cardioid Dynamic Moving Coil Capsule
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Heavy-grade **Physical** XLR microphone cable routing from auxiliary percussion stand to Stage Snake Box Input 23
* **Hardware Role**: Captures transient left-axis field information for acoustic maracas, tambourines, and metal scraping
* **Power Hardware**: N/A (Fully Passive Dynamic Circuitry)
* **Status**: PENDING PURCHASE Requisition Target

### Shure SM57 (Percussion R)
* **Hardware Type**: Professional Cardioid Dynamic Instrument Microphone Hardware
* **Physical Electronics**: Mid-Heavy Cardioid Dynamic Moving Coil Capsule
* **Physical I/O**: Standard Mono XLR Output Hardware Connector
* **Ground Truth Path**: Heavy-grade **Physical** XLR microphone cable routing from auxiliary percussion stand to Stage Snake Box Input 24
* **Hardware Role**: Captures transient right-axis field information for acoustic maracas, tambourines, and metal scraping
* **Power Hardware**: N/A (Fully Passive Dynamic Circuitry)
* **Status**: PENDING PURCHASE Requisition Target


---


# 1.5 The Anchor (The Rack Mount Infrastructure)

This section defines the central processing hardware rack core and its structural layout. **Confirmed unchanged in v2.0** — every item remains a Pending Purchase Requisition Target, rail layout unchanged.

## I. Physical Infrastructure & Hardware

### Gator GRC-BASE-10
* **Hardware Type**: 10U Slant-Top Heavy Duty Mobile Flight Case Enclosure Hardware
* **Physical Construction**: Rotomolded Polyethylene structural housing shell with heavy steel rail hardware
* **Physical I/O**: Front, Rear, and Top access point physical utility hatches
* **Ground Truth Path**: Houses all master mixing, cooling, and power hardware modules locked securely to its steel rails
* **Hardware Role**: Structural outer protection container shell and flight transport chassis anchor
* **Power Hardware**: N/A (Passive Mechanical Housing)
* **Status**: PENDING PURCHASE Requisition Target

### Seismic Audio SACB-24x8x25 Stage Snake Trunk
* **Hardware Type**: 24-Channel Low-Profile XLR PCB Analog Multi-Core Trunk Line Hardware
* **Physical Construction**: Heavy-Duty Shielded Copper Core multi-conductor trunk
* **Physical I/O**: 24 XLR Female Inputs, 8 XLR Male Outputs, 25-Foot length parameter
* **Ground Truth Path**: Multi-core trunk routes across the performance surface to plug directly into the rear panels of the WING console
* **Hardware Role**: Primary analog audio collection artery bridging the entire stage floor directly to preamplification
* **Power Hardware**: N/A (Fully Passive Conductive Core)
* **Status**: PENDING PURCHASE Requisition Target

### Behringer WING Rack
* **Hardware Type**: Core Advanced Digital Audio Mixer and FOH/IEM Routing Engine Hardware
* **Physical Electronics**: 40-bit Floating Point Internal Audio Calculation Core Hardware Engine
* **Physical I/O**: 24 Midas PRO Microphone Preamps, 8 Balanced XLR Line Outputs, StageConnect Link, USB Audio Port
* **Ground Truth Path**: Mounted securely in spaces U4-U7; receives input from the primary stage snake and USB extenders
* **Hardware Role**: System brain managing master audio matrices, input preamp gain stages, and IEM monitor mixing
* **Power Hardware**: Internal 100-240VAC Universal Switching Transformer Power Supply
* **Status**: PENDING PURCHASE Requisition Target

### Furman PL-PLUS C
* **Hardware Type**: Advanced Linear AC Power Conditioner and Surge Suppressor Hardware
* **Physical Electronics**: Linear Filtering Technology (LiFT) and Series Multi-Stage Protection AC Hardware Circuitry
* **Physical I/O**: 9 Rear Voltage-Isolated AC Outlets, Front Panel Digital Voltmeter display
* **Ground Truth Path**: Mounted securely in space U3 to feed clean voltage to all active rack modules
* **Hardware Role**: Master power suppression and central AC line purification distributor
* **Power Hardware**: 120VAC / 15A Maximum capacity input infrastructure
* **Status**: PENDING PURCHASE Requisition Target

### T6 Airflow System
* **Hardware Type**: Rack Enclosure Active Thermal Management Fan Array Hardware
* **Physical Construction**: Steel 1U tray housing dual high-speed ball bearing cooling fans
* **Physical I/O**: Backlit Smart LCD Thermal Controller interface on the front face panel
* **Ground Truth Path**: Bolt-locked into U1 to pull rising warm air out from the enclosed case volume
* **Hardware Role**: Controls temperature variations to safeguard active computing engines from overheating
* **Power Hardware**: 120VAC/DC Power Adapter block connection
* **Status**: PENDING PURCHASE Requisition Target

### 1U Vented Router Shelf
* **Hardware Type**: Rigid Steel Rack Component Shelf Hardware
* **Physical Construction**: Perforated heavy-gauge steel structural support panel
* **Physical I/O**: N/A (Passive Component Tray)
* **Ground Truth Path**: Mounted securely in space U2 to hold the wireless network system
* **Hardware Role**: Secure stage placement tray for data transmission gear while maintaining airflow ventilation gaps
* **Power Hardware**: N/A (Passive Structural Tray)
* **Status**: PENDING PURCHASE Requisition Target

### 3U Vented Blank Panels
* **Hardware Type**: Protective Steel Front-Facing Enclosure Panels Hardware
* **Physical Construction**: High-Airflow Slotted Metal Space Covers
* **Physical I/O**: N/A (Passive Blocking Shield)
* **Ground Truth Path**: Bolt-locked into spaces U8-U10 to seal off open front rack spacing volume
* **Hardware Role**: Safeguards internal wiring arrays and preserves internal negative air pressure loops
* **Power Hardware**: N/A (Passive Protective Structural Element)
* **Status**: PENDING PURCHASE Requisition Target

## II. Internal Physical Cabling Manifest (The Rack Enclosure)
* **Component Item**: Localized Internal Rack Interconnect Harness
* **Hardware Type**: Ultra-Shielded High-Density Patch Cable Component Inventory
* **Physical Elements**: 12x XLR Male-to-Female Heavy Duty Patch Cables (1ft-3ft length specifications) and 3x IEC AC Power Leads
* **Ground Truth Path**: Links the rear outputs of the WING engine directly to local panels, and connects mains to the Furman supply
* **Hardware Role**: Direct audio patch routing and primary hardware AC distribution
* **Power Hardware**: Driven directly out of the onboard centralized Furman PL-PLUS C terminal block
* **Status**: PENDING PURCHASE Requisition Target

## III. Physical Front & Rear Rails Configuration
* **U1 Positioning**: T6 Airflow System Fan Unit | Core active exhaust cooling module
* **U2 Positioning**: 1U Vented Router Shelf Hardware | Holds local network components; provides thermal buffer spacing
* **U3 Positioning**: Furman PL-PLUS C Conditioning Module | Distributes filtered AC power across the grid
* **U4 – U7 Positioning**: Behringer WING Rack Chassis Frame | Performs all multi-channel mixing and digital bus routing
* **U8 – U10 Positioning**: 3U Vented Blank Panels & Rear Storage Shelf | Front protective structural plate / Back-side snake cable garage bay


---


# 1.6 The Synth Bay

This section establishes the terminal desktop synth station hardware components, infrastructure frames, and localized multi-channel matrix audio routing paths.

## I. Physical Infrastructure & Power

### On-Stage SR5 Synth Rack
* **Hardware Type**: Secondary Heavy Steel Ergonomic Desktop Support Stand Hardware
* **Physical Construction**: Multi-Tier Fixed Angle Structural Steel Frame
* **Ground Truth Path**: Securely bolted to the main synthesizer table surface to house local instrument chassis modules
* **Hardware Role**: Eradicates desk clutter and provides physical angle tracking for finger-drumming execution
* **Power Hardware**: N/A (Passive Structural Frame System)
* **Status**: Owned Physical Asset

### Gator GR-6S ATA Shallow 6U
* **Hardware Type**: Heavy Duty High-Impact Flight Enclosure Case Hardware
* **Physical Construction**: Lightweight Rotomolded Polyethylene case with heavy steel rack rails
* **Ground Truth Path**: Situated on the lower table tier to encapsulate the local power, transformers, and data hubs
* **Hardware Role**: Encloses delicate sub-modules against accidental impacts or fluid spills
* **Power Hardware**: N/A (Passive Protective Shell System)
* **Status**: PENDING PURCHASE Requisition Target

### On-Stage KS7350 Folding-Z
* **Hardware Type**: Heavy-Duty Keyboard Support Frame Stand Hardware
* **Physical Construction**: High-Capacity Welded Square Steel Tube Z-Frame
* **Ground Truth Path**: Positioned as the foundational base anchor supporting the master controller keyboards
* **Hardware Role**: Structural platform optimized for high-impact performance stability
* **Power Hardware**: N/A (Passive Structural Stand System)
* **Status**: PENDING PURCHASE Requisition Target

### Juice Goose JG Junior
* **Hardware Type**: Rack-Mounted AC Power Distribution and Filtration Module Hardware
* **Physical Electronics**: Basic RFI/EMI Suppression and High-Voltage Varistor Surge Protection Circuitry
* **Physical I/O**: 6 Rear-Facing Filtered AC Output Hardware Outlets
* **Ground Truth Path**: Mounted in the local 6U flight case to distribute clean voltage across the synthesizer array
* **Hardware Role**: Filters local power lines to prevent digital noise spikes from contaminating audio circuits
* **Power Hardware**: 120VAC / 15A Maximum capacity input line infrastructure
* **Status**: PENDING PURCHASE Requisition Target

### Desk Clamp Power Strip
* **Hardware Type**: Multi-Output Mechanical Peripheral Power Distributor Hardware
* **Physical Construction**: High-Impact Fireproof Shell with integrated table clamping hardware screw
* **Physical I/O**: 3x Filtered AC Outlets, Dual Smart USB Charging Ports
* **Ground Truth Path**: Fixed firmly to the desktop edge rail to supply instantaneous power access to portable instruments
* **Hardware Role**: Direct power access node serving local USB and battery-powered gear
* **Power Hardware**: 120VAC Input / 40W Maximum Integrated Smart Fast-Charging Core
* **Status**: PENDING PURCHASE Requisition Target

### ART T8 — 🚩 status changed to CONDITIONAL in v2.0
* **Hardware Type**: 8-Channel Passive High-Performance Audio Isolation Transformer Hardware
* **Physical Electronics**: 8 pairs of high-fidelity 1:1 physical audio isolation transformers
* **Physical I/O**: 8x 1/4" TRS Balance Inputs / 8x 1/4" TRS Balanced Output Hardware Jacks
* **Ground Truth Path**: Intercepts unbalanced instrument outputs, passing isolated lines forward to the SC16-I input block
* **Hardware Role**: Severs physical ground links to eradicate high-pitched digital USB squeal and hum across the loop
* **Power Hardware**: N/A (Fully Passive Magnetic Transformer Circuitry)
* **Status**: **CONDITIONAL** — not a committed purchase. Isolation transformers like this are typically a reactive fix for ground-loop hum/USB switching noise rather than a guaranteed requirement. Test the signal chain without it first once the Synth Bay is hooked up; add only if hum/squeal noise actually appears at the SC16-I.

## II. Physical Analog-Output Hardware (Generators & Processors)

### Roland P-6
* **Hardware Type**: Creative Digital Sampler and Granular Processing Sound Design Hardware
* **Physical Electronics**: Integrated DSP Sampling Core with onboard microphone hardware
* **Physical I/O**: 3.5mm Stereo Mix Input/Output, 5-Pin TRS MIDI I/O, USB-C Data Port
* **Ground Truth Path**: Audio outputs route through an inline 3.5mm isolator into the local transformer array
* **Hardware Role**: Primary granular shredder, vocal micro-sampler, and mechanical rhythmic anchor mapped to MIDI Channel 04 responding to CC 74 (Filter Cutoff), CC 71 (Resonance), CC 7 (Volume), CC 10 (Pan), and CC 87 (Lo-Fi Switch)
* **Power Hardware**: Local Internal Lithium-Ion Rechargeable Battery / 5VDC via USB hub connection
* **Status**: Owned Physical Asset

### Teenage Engineering EP-40 Riddim
* **Hardware Type**: Fast-Transient Digital Micro-Sampler and Percussion Hardware Engine
* **Physical Electronics**: Micro-Digital Sampling Processor with tactile mechanical switch buttons
* **Physical I/O**: 3.5mm Sync In/Out, 3.5mm Stereo Mix In/Out, USB-C Data Port
* **Ground Truth Path**: Output jack routes via an inline 3.5mm isolator directly into the local transformer matrix
* **Hardware Role**: Fires volatile industrial drums, lo-fi percussive hits, and fast transient sample sequences
* **Power Hardware**: Internal Battery Cells / 5VDC via USB hub distribution line
* **Status**: Owned Physical Asset

### Telepathic Instruments ORC-1
* **Hardware Type**: Chord-Generating Polyphonic Digital Synthesizer Hardware Engine
* **Physical Electronics**: Onboard Chord Logic Algorithm and Industry-Leading Voice-Leading Technology Digital Synthesizer Engine
* **Physical I/O**: 3.5mm Stereo Output Jack, 3.5mm TRS MIDI Out, USB-C Data Port
* **Ground Truth Path**: Output routes via a specialized 1/4" TRS breakout straight into the local isolation matrix
* **Hardware Role**: Supplies fundamental harmonic progressions, unstable synth leads, and deep analog-modeled sub-bass tones via three synth engines and Voicing Dials™
* **Power Hardware**: Local Rechargeable Internal Battery / 5VDC via USB bus power distribution
* **Status**: Owned Physical Asset

### Korg KAOSS Pad 3+ (KP3+)
* **Hardware Type**: Real-Time Dynamic X-Y Pad Audio Effects Processor Hardware
* **Physical Electronics**: Touch-Reactive Coordinate Sensor and Multi-Algorithm DSP Effector Core
* **Physical I/O**: Dual RCA Stereo Inputs/Outputs, 1/4" Microphone Input, USB-B Data Port
* **Ground Truth Path**: Inputs/outputs breakout via custom RCA cables into local isolation transformer loops
* **Hardware Role**: Handles real-time spatial filtering, manual repeat catching, and tactile audio destruction
* **Power Hardware**: 12VDC External Hardware Transformer Adapter Block
* **Status**: Owned Physical Asset

> **v2.0 note:** Boss VE-22 (Advanced Vocal Multi-Effect Processor and Preamp) has been **removed** from the Synth Bay entirely. Vocal/gain processing has moved to software — BLEASS Vox (owned) and Neural DSP Mantra (committed pending purchase) — see [[01.7-workstation]]. SC16-I Inputs 9–10 are now open/unassigned as a result.

## III. Physical Digital Hardware (Zero-Audio Controllers)

### Arturia KeyLab MkII 61 — replaces the Arturia KeyLab Essentials 49 in v2.0
* **Hardware Type**: 61-Key Semi-Weighted Full-Size Keyboard MIDI Controller Hardware
* **Physical Electronics**: Velocity-Sensitive Keybed Core with integrated encoder and fader arrays
* **Physical I/O**: USB Type-B Port, 1/4" Sustain/Expression Switch Hardware Jack
* **Ground Truth Path**: Connects via a short physical USB Type-B to Type-A line straight into the Acasis table hub
* **Hardware Role**: Master keyboard controller driving non-physical VST synths inside the computer node. Now hosts the Moog Expression Pedal (see Section IV below) in place of the retired KeyLab Essentials 49.
* **Power Hardware**: 9VDC External Adapter / ~500mA or direct USB bus power voltage tracking
* **Status**: Owned Physical Asset

### Novation Launchkey 25 mk4
* **Hardware Type**: 25-Note Compact Keyboard MIDI Controller Hardware
* **Physical Electronics**: Synth-Action Keybed coupled with 16 velocity-sensitive RGB pad triggers
* **Physical I/O**: USB Type-C Data Port
* **Ground Truth Path**: Short physical USB Type-C to Type-A cord hooks straight into the Acasis data hub
* **Hardware Role**: Dedicated local keyboard used to manipulate real-time laptop bass patches and parameters
* **Power Hardware**: 5VDC via USB Bus Power (100% data hub powered infrastructure)
* **Status**: Owned Physical Asset

### Native Instruments Maschine — new in v2.0
* **Hardware Type**: Pad-Based Sampler/Sequencer MIDI Controller Hardware (Mk3 hardware assumed — 🚩 exact model TBD, see [[open-flags]] #9)
* **Physical I/O**: USB Data Port
* **Ground Truth Path**: Hooked using a physical USB cable running straight into an active port on the Acasis data concentration hub (port assignment not yet stage-verified)
* **Hardware Role**: Pad-based sampling and sequencing controller
* **Power Hardware**: 5VDC via USB Bus Power
* **Status**: Owned Physical Asset

### Expressive E Touché SE — new in v2.0
* **Hardware Type**: MPE Multi-Touch Performance Controller Hardware
* **Physical I/O**: USB-C Data Port
* **Ground Truth Path**: Hooked using a physical USB-C cable running straight into an active port on the Acasis data concentration hub (port assignment not yet stage-verified)
* **Hardware Role**: Expressive multi-touch MPE performance control
* **Power Hardware**: 5VDC via USB Bus Power
* **Status**: Owned Physical Asset

### Novation Launch Control XL Mk3 — new in v2.0
* **Hardware Type**: DAW/Mixer Control Surface Hardware (faders/knobs) (🚩 exact model TBD — Jeremy referenced "Control XL 3," see [[open-flags]] #9)
* **Physical I/O**: USB Data Port
* **Ground Truth Path**: Tethered using a short physical USB Type-C to Type-A cable running straight into an active port on the Acasis data concentration hub
* **Hardware Role**: DAW/mixer control surface
* **Power Hardware**: 5VDC via USB Bus Power
* **Status**: Owned Physical Asset

> **v2.0 note:** Novation Launchpad X and Akai MPK mini have both been **removed** from the Synth Bay controller lineup.

## IV. Physical Expression & Peripheral Hardware

### Moog Expression Pedal
* **Hardware Type**: Linear Continuous Parameter Sweep Control Hardware Pedal
* **Physical Electronics**: Passive Potentiometer with an integrated variable attenuation trim knob
* **Physical I/O**: Integrated 1/4" TRS Hardwired Outbound Cable Tail
* **Ground Truth Path**: Hardwired TRS jack plugs directly into the expression input port of the **KeyLab MkII 61** keyboard (updated in v2.0 — previously the KeyLab Essentials 49)
* **Hardware Role**: Modulates VST filter sweeps and macro values through manual foot movement
* **Power Hardware**: N/A (Fully Passive Linear Resistance Circuit)
* **Status**: Owned Physical Asset

### Behringer P2
* **Hardware Type**: Ultra-Compact Personal IEM In-Ear Monitor Amplifier Hardware
* **Physical Electronics**: Active Low-Noise Stereo/Mono Headphone Drive Output Circuitry
* **Physical I/O**: XLR/TRS Combo Locking Input, 3.5mm Stereo Headphone Output Hardware Jack
* **Ground Truth Path**: Balanced input receives physical lines split off from the SC16-O output channels
* **Hardware Role**: Local high-fidelity ear monitoring module tracking master stage click lines
* **Power Hardware**: 2x AAA Alkaline Battery cells providing local independent active power
* **Status**: PENDING PURCHASE Requisition Target

### XLR Inline Attenuator Pad
* **Hardware Type**: Balanced Passive Signal Level Management Hardware Module
* **Physical Construction**: Internal Fixed Resistive Attenuation Network offering a fixed -20dB drop
* **Physical I/O**: Standard XLR Female Input / Standard XLR Male Output Hardware Ends
* **Ground Truth Path**: Inserted inline between the SC16-O analog output port and the input of the Behringer P2 amp
* **Hardware Role**: Drops hot balanced console output levels to safeguard delicate headphone amp inputs from clipping
* **Power Hardware**: N/A (Fully Passive Precision Resistor Network)
* **Status**: PENDING PURCHASE Requisition Target

## V. The Physical Matrix: Synth Bay Audio Routing (SC16-I & SC16-O)
* **Inputs 01 - 08 Destination**: Handles P-6, EP-40, ORC-1, and KP3+ analog generators via short physical 1/4" TRS lines arriving directly from the output side of the ART T8 isolation transformers (if installed — see the Conditional ART T8 note in Section I above).
* **Inputs 09 - 10 Destination**: 🚩 **OPEN / UNASSIGNED (v2.0)** — formerly captured the Boss VE-22 voice processor directly via balanced XLR, bypassing the T8. VE-22 removed; vocal processing moved to software (BLEASS Vox + Neural DSP Mantra — see [[01.7-workstation]]).
* **Outputs 01 - 04 Destination**: Feeds back into local sampler and KP3+ line entry ports utilizing physical XLR-Female to RCA/3.5mm custom hardware breakout cords.
* **Outputs 05 - 06 Destination**: Drives the personal Behringer P2 ear system via a physical balanced XLR path passing through the Inline Attenuator hardware link. (v2.0: the prior "VE-22 monitor" destination has been dropped along with the VE-22 itself.)

## VI. Internal Physical Cabling Manifest (The Synth Node)
* **Component Item**: Localized Table-Top Audio and Isolation Loom Array
* **Hardware Type**: Special-Application Shielded Audio Breakout and Filtering Cable Stock
* **Physical Elements**: 2x 3.5mm to Dual 1/4" TS lines (6ft); 2x 3.5mm inline ground isolators; 2x RCA to 1/4" TS lines (6ft); 1x RCA inline isolator; 1x 1/4" TRS to Dual TS breakout line (6ft)
* **Ground Truth Path**: Interfaces the local physical chassis of the P-6, EP-40, ORC-1, and KP3+ directly with the local isolation transformer array (if installed — see ART T8 Conditional status)
* **Hardware Role**: Eliminates high-frequency USB ground noise spikes and forwards analog channels cleanly
* **Power Hardware**: Fully passive component lines interacting with hub power grids
* **Status**: 100% Owned Physical Cabling Component Infrastructure


---


# 1.7 The Workstation ("The Commodore")

This section establishes the definitive physical hardware infrastructure, data concentration nodes, power regulation paths, and virtual digital assets of the primary workstation. **Physical Nodes & Power confirmed unchanged in v2.2 — this revision only updates Section III, the plugin manifest.**

## I. Physical Workstation Nodes & Hardware Power Mapping

### Dell Precision 7550
* **Hardware Type**: Central Host Performance Workstation Mobile Processing Node
* **Physical Specifications**: Intel i7-10875H (8-Core) CPU, 32GB DDR4 RAM, NVIDIA Quadro T2000 GPU, 512GB NVMe SSD Storage
* **Physical I/O**: Dual Thunderbolt Ports, HDMI Output, 3x USB Type-A Ports
* **Ground Truth Path**: Stationed centrally on the Command Table; physical power block runs down to the isolated Furman floor conditioner
* **Hardware Role**: Master computing node running the live audio sequencer host, virtual synths, and automation scripts
* **Power Hardware**: 180W/240W External Heavy Duty Power Brick running off 120VAC lines
* **Status**: Owned Physical Asset

### Acasis 16-Port High-Speed Hub
* **Hardware Type**: Data Concentration and Multi-Channel USB 3.2 Gen 2 Interface Hub Hardware
* **Physical Construction**: Solid aluminum industrial rail chassis with independent physical power toggle switches
* **Physical I/O**: 16x USB Type-A Downstream Ports / 1x USB Type-B Master Host Port
* **Ground Truth Path**: Mounted to the upper table frame tier to receive all localized controller and sampler lines
* **Hardware Role**: Eliminates terminal data fragmentation and consolidates 100% of local MIDI control data
* **Power Hardware**: Dedicated External 12VDC / 96W (8A) High-Current Switching Power Supply
* **Status**: Owned Physical Asset

### U2EX60 Extender Receiver (Data Node)
* **Hardware Type**: USB-over-Cat6 Long-Distance Hardware Digital Decoding Receiver
* **Physical Electronics**: Single-Ended Data Extension Core Decoder Circuitry
* **Physical I/O**: 1x RJ45 Shielded Input Jack / 4x USB Type-A Output Female Hardware Ports
* **Ground Truth Path**: Receives long-run Cat6 line from the stage floor, outputting via physical USB link into the Acasis host hub
* **Hardware Role**: Decodes remote floor performance data control lines with zero conversion lag
* **Power Hardware**: 5VDC Power Supply Adapter block routing straight into the local Desk Clamp Strip
* **Status**: Owned Physical Asset

### U2EX60 Extender Receiver (Audio Node)
* **Hardware Type**: USB-over-Cat6 Long-Distance Hardware Digital Decoding Receiver
* **Physical Electronics**: High-Bandwidth Digital Audio Stream Extension Decoder Circuitry
* **Physical I/O**: 1x RJ45 Shielded Input Jack / 1x USB Type-A Output Female Hardware Port
* **Ground Truth Path**: Mounts securely inside the 8U/10U Rack rails to deliver master digital audio to the WING card
* **Hardware Role**: Receives high-speed multi-channel digital audio data streaming off the workstation node
* **Power Hardware**: 5VDC Power Supply Adapter block routing straight into the local Desk Clamp Strip
* **Status**: PENDING PURCHASE Requisition Target

### Kootek 5-Fan Cooling Pad
* **Hardware Type**: Laptop Active Thermal Management Elevation Tray Hardware
* **Physical Construction**: Heavy-duty structural mesh screen frame embedding 5 active cooling fans
* **Physical I/O**: Dual-USB Type-A Pass-Through Connector Ports
* **Ground Truth Path**: Keeps the Dell Precision 7550 chassis frame cool to prevent background CPU cycles from choking audio streams
* **Hardware Role**: Suppresses thermal CPU throttling risks during high-track-count live audio processing
* **Power Hardware**: 5VDC bus power drawn via physical USB line directly from the active Acasis Hub
* **Status**: Owned Physical Asset

### Furman PL-8 C
* **Hardware Type**: Master Stage Floor AC Power Distribution and Filtration Array Hardware
* **Physical Electronics**: Advanced Noise Attenuation and High-Capacity Surge Suppression Core
* **Physical I/O**: 8 Rear Panel Isolated AC Outlets / Front Panel Pull-Out LED Utility Lights
* **Ground Truth Path**: Secured flat on the stage floor beneath the computer table to handle main power lines safely
* **Hardware Role**: Central AC mains isolation node keeping high-voltage power bricks separated from clean audio coils
* **Power Hardware**: 120VAC / 15A Maximum capacity input line infrastructure
* **Status**: PENDING PURCHASE Requisition Target

### Desk Clamp Power Strip (Workstation Unit)
* **Hardware Type**: Multi-Output Structural Peripheral Power Distributor Hardware
* **Physical Construction**: Impact-Resistant Enclosure with integrated manual table-clamping screw assembly
* **Physical I/O**: 3x Clean AC Outlets, Dual Smart USB Charging Ports
* **Ground Truth Path**: Fastened firmly to the workstation desk edge rail to handle table sub-modules
* **Hardware Role**: Localized power source management for cooling pads and data extender receivers
* **Power Hardware**: 120VAC Mains Input / 40W Maximum Integrated Smart Fast-Charging Core
* **Status**: PENDING PURCHASE Requisition Target

## II. The Physical Neural Net: Data & Control Wiring — updated in v2.0

* **MIDI Control Line Pipeline**: The physical Morningstar MC6 Pro floor unit outputs data via physical USB into a local extender transmitter. A 25ft rugged, shielded Cat6 Ethernet cable runs across the physical stage floor to reach the U2EX60 Receiver at the table, terminating into a physical port on the Acasis hub.
* **USB Audio Line Pipeline**: A physical USB/Thunderbolt cable outputs digital audio from the Dell Precision 7550 into a table extender transmitter. A 25ft rugged, shielded Cat6 line routes across the floor space to hit the receiver inside the 8U/10U Rack, terminating via physical USB Type-B straight into the Behringer WING's digital card.
* **Roland P-6 / TE EP-40 Data Hooks**: Docked using physical short USB Type-C to Type-A cables straight into active ports on the Acasis table hub to facilitate internal battery tracking and sample data transfers.
* **Arturia KeyLab MkII 61 Data Hook**: Hooked using a physical USB Type-B to Type-A cable running straight into an active port on the Acasis data concentration hub. *(v2.0: replaces the prior "Arturia KeyLab / Akai Mini" line — the Akai MPK mini has been removed from the rig.)*
* **Novation Launchkey / Novation Launch Control XL Mk3 Data Hooks**: Tethered using short physical USB Type-C to Type-A cables running straight into active ports on the Acasis data concentration hub. *(v2.0: replaces the prior "Novation Launchkey / Launchpad" line — the Launchpad X has been removed from the rig.)*
* **Native Instruments Maschine Data Hook**: Hooked using a physical USB cable running straight into an active port on the Acasis data concentration hub. *(v2.0: new)*
* **Expressive E Touché SE Data Hook**: Hooked using a physical USB-C cable running straight into an active port on the Acasis data concentration hub. *(v2.0: new)*

## III. The Digital Arsenal (Software & Plugin Manifest)

This section registers the non-physical software assets running on the **Physical Workstation** processor core. The operating system is locked to Windows 11 Pro. The system power plan is set to "Ultimate Performance" with "USB Selective Suspend" disabled to safeguard against physical hardware link disconnections.

**v2.2 note (October 2026):** Reconciled against the October 2026 Definitive Plugin & Software Update (ownership audit). Ownership gaps from v2.1 are closed, the "downloaded / pending" group is resolved into the functional categories below, Tritik Krush is restored, Neural DSP Mantra and Darkglass Ultimate are removed from the owned/committed lists (not owned — see [[open-flags]] #14), and the wishlist is cleaned up. Entries marked *new in v2.2* carry only what the audit records (maker, provenance, and a role where the audit gave one); fuller descriptions get filled in as they are verified. Categories are unchanged from the "Ghost Pipes Personality Map" function-based framing, with a few added for newly documented items.

**v2.1 note (carried forward):** Rebuilt against Jeremy's curated Plug In Matrix (102 titles). Each entry carries a **location/provenance tag** — see the legend below.

### Deployment State & Status Model (v2.2)

**Current state of The Commodore: Ableton Live 12 Suite is installed. Third-party plugin deployment has not yet begun.** Unless an entry explicitly says otherwise, every owned third-party plugin in this manifest is **NOT YET INSTALLED** on the Dell Precision 7550.

Ownership is not installation. Software is tracked in six separate states, and one never implies another:

1. **Owned / Acquired**
2. **Installed** on the Dell Precision 7550
3. **Activated / Authorized**
4. **Selected** for the live-performance installation
5. **Wishlist / Candidate**
6. **Recovery / Access method**

Do not infer installation from: ownership, a Plugin Boutique library entry, an installer in Downloads, a vendor account entitlement, a license/serial, or a receipt email. The eventual 7550 deployment is **curated** — it is not "install everything owned."

**Tag legend:**
* `[PIB]` — Plugin Boutique library
* `[DRIVE]` — downloaded/installer held locally; **not an install state** (see [[open-flags]] #15)
* `[HARDWARE TIED]` — entitlement received through the owned and registered Arturia / Native Instruments / Novation hardware ecosystem (ownership resolved; the exact originating device is not tracked unless needed for license recovery)
* `[FREE]` — intentionally acquired free plugin
* `[DIRECT]` — direct vendor purchase (Gumroad, Lemon Squeezy, vendor store)

*(Native Access 2 and the UJAM Setup installer are excluded from this manifest — they are plugin manager/installer apps, not plugins. A recovery map for these ecosystems is at the end of this section. No license keys, serials, or account details are recorded in the Codex.)*

### DAW / Core Environment (Owned)

* **Ableton Live 12 Suite** `[DRIVE]` — Core Host Software DAW — **installed on the 7550**. Built-in devices of note: Convolution Reverb Pro, Hybrid Reverb, Echo, Resonators, Corpus, Spectral Resonator, Spectral Time, Shifter, Grain Delay, Drum Buss, Saturator, Roar, Operator, Wavetable, Analog, Drift, Collision, Tension, Sampler, Simpler, plus the full Max for Live ecosystem
* **Bitwig Studio 8-Track** `[PIB]` — secondary DAW/host — owned, not Ghost Pipes core; does not displace Ableton as the Ghost Pipes platform
* **Waveform Free** — secondary DAW/host — owned, not Ghost Pipes core; does not displace Ableton — new in v2.2

### Synths / Sound Sources (Owned)

* **Native Instruments Komplete 15 Select** `[HARDWARE TIED]` — Kontakt Player ecosystem, Massive X Player content, Play Series instruments, Factory Library content — bundled with Novation Launchkey 25 mk4
* **Native Instruments Spotlight Collection** `[DRIVE]` — (India, Cuba, West Africa, East Asia, Middle East, etc.) — Role: human/world performers — direct NI purchase confirmed
* **Native Instruments "The Gentleman"** `[HARDWARE TIED]` — vintage piano / intimate acoustic source — hardware-bundled entitlement; ownership resolved in v2.2
* **Native Instruments Roux** `[PIB]` — New Orleans bounce instrument; human ensemble / regional character
* **Native Instruments FM8** `[PIB]` — FM synthesis / digital textures
* **Native Instruments Reaktor Synthesizer Bundle** `[PIB]` — modular synthesis environment 🚩 specific included synths/role TBD, see [[open-flags]] #13
* **Arturia Analog Lab Pro** `[HARDWARE TIED]` — vintage synth workstation — bundled with Arturia KeyLab MkII 61 (confirmed by Jeremy: the Pro edition, distinct from the base "Analog Lab V" Arturia's public bundle page lists)
* **Arturia Analog Lab Play** — new in v2.2
* **GForce Heritage Synths** `[HARDWARE TIED]` — classic analog character — hardware-bundled entitlement (Arturia/NI/Novation ecosystem); ownership resolved in v2.2
* **GForce AXXESS** `[PIB]` — analog mono synth character — also confirmed as part of the Novation Launchkey mk4 bundle
* **Moog Mariana** `[PIB]` — virtual dual-oscillator analog bass modeling synthesizer
* **Soundiron Crystal** `[DRIVE]` — granular cinematic texture generator — confirmed on NI/NKS order
* **Heavyocity Symphonic Destruction** — cinematic/acoustic source — new in v2.2
* **Crow Hill Pocket Strings** `[FREE]` — strings library, The Crow Hill Company — $0 acquisition confirmed
* **AudioThing Organetta** `[PIB]` — character keyboard (vintage reed organ emulation)
* **AudioThing Noises** `[PIB]` — texture/noise source
* **Thenatan Tape Piano 1** `[PIB]` — lo-fi piano source
* **Evolve Alloy Lite** `[PIB]` — ownership confirmed via the Plugin Boutique library; maker/full role description still unconfirmed 🚩 see [[open-flags]] #11
* **UVI Model D** `[HARDWARE TIED]` — high-fidelity concert grand piano emulation — hardware-bundled entitlement; ownership resolved in v2.2
* **Novation Play** `[HARDWARE TIED]` — digital groovebox / software sequencing engine — confirmed bundled with Novation Launchkey 25 mk4
* **Ample Guitar M Lite** `[PIB]` — sampled acoustic guitar instrument (free/Lite tier)
* **FOUNDATIONS | Emotive Choir** `[PIB]` — choir/vocal sample library
* **FOUNDATIONS | Piano** `[PIB]` — piano sample library
* **LoFi Piano** `[PIB]` — lo-fi piano instrument, pairs with Thenatan Tape Piano 1
* **MSoundFactoryPlayer** `[PIB]` — modular/sample-based synth player 🚩 exact role TBD, see [[open-flags]] #13
* **Newfangled Audio Pendulate** `[PIB]` — rhythmic modulation synthesizer
* **Surge XT** `[PIB]` — open-source subtractive/wavetable synth
* **Surrealistic MG-1 Plus Synthesizer** `[PIB]` — vintage analog-style synth emulation
* **TAL-U-NO-62** `[PIB]` — Juno-60-style analog synth emulation
* **Zebralette 3** — new in v2.2
* **Baby Audio Atoms** `[PIB]` — physical modeling synthesizer tracking a mass-spring network for glassy textures — owned (moved from Master Wishlist in v2.1)

### Experimental / Distinctive Instruments (Owned) — new category in v2.2

Part of the distinctive Ghost Pipes software center (see Curation Guidance below). See also Baby Audio Atoms, Newfangled Audio Pendulate, AudioThing Noises, and AudioThing Organetta above.

* **Phase Fiasco KAZU** — owned; purchased September 30, 2026 (moved from Master Wishlist) — new in v2.2
* **Phase Fiasco Annulus** `[DIRECT]` — owned; provenance resolved by direct Lemon Squeezy receipt. Functional territory from prior investigation: polyphonic physical-modeling resonator/effect/instrument — wording kept conservative, not independently verified
* **Klevgrand Tomofon** — new in v2.2
* **Glitchmachines PolyGAS** — new in v2.2
* **W.A. Production Imperfect** — new in v2.2
* **Chippo** `[FREE]` — free simple chiptune/retro-digital instrument and internal pattern generator. Not documented as outputting MIDI — unverified
* **Pathfinder** `[FREE]` — Audio Tech Hub; free/open-source sample-based instrument/sequencer (not a cello/string instrument)
* **Bloom Palette Object** — new in v2.2
* **Bloom Vocal Aether** — new in v2.2
* **Bloom Bass Impulse** — new in v2.2
* **Bloom Drum Break** — new in v2.2

### Drums / Rhythm Personalities (Owned)

**UJAM Select 5** (ownership confirmed in the UJAM App → My Products; all five show as available to Install and **not activated**): Virtual Drummer BRUTE, Finisher FLUXX, Virtual Bassist ROWDY 2, Beatmaker BERSERK, Groovemate LATIGO. Additional UJAM products owned outside Select 5 are listed below, including MELLOW 2 (separate Plugin Boutique purchase). Recovery: UJAM App → sign in → My Products → install/activate.

* **UJAM HEAVY 2** `[PIB]` — hard rock drummer
* **UJAM Virtual Drummer BRUTE (VD BRUTE)** `[DRIVE]` — grunge/post-punk drummer — Select 5
* **UJAM Beatmaker BERSERK (BM BERSERK)** `[DRIVE]` — aggressive electronic percussion — Select 5
* **UJAM Groovemate LATIGO** `[DRIVE]` — organic percussion — Select 5
* **UJAM SOLID 2** — new in v2.2
* **UJAM Beatmaker VICE** — new in v2.2
* **Klevgrand Slammer** `[HARDWARE TIED]` — multi-sampled drum software optimized for aggressive acoustic instrument tracking — confirmed bundled with Novation Launchkey 25 mk4
* **Marco Polo Drums** `[PIB]` — character/cinematic groove drummer
* **Lineage Percussion** `[DRIVE]` — percussion library/instrument 🚩 maker and exact role unconfirmed, see [[open-flags]] #13
* **Drumbo Jr.** `[DRIVE]` — drum tool 🚩 maker and exact role unconfirmed, see [[open-flags]] #13
* **Dan Mayo Everything Bundle** `[DIRECT]` — owned; purchased September 30, 2026 (moved from Master Wishlist). Treat as soundware/content rather than a plugin count. Recovery: Dan Mayo web download portal via the entitlement email titled "Your packs are ready"; a fresh link can be requested when needed — new in v2.2
(NI Spotlight world percussion covered above under Synths / Sound Sources)

**Rhythmic / finishing FX** (not drummers):

* **UJAM Finisher FLUXX** `[DRIVE]` — Select 5; rhythmic finishing effect — do not classify as a drummer

*(UJAM BM NEMESIS and UJAM BM VOID were considered but are not purchased — not part of the owned inventory.)*

### Bass Personalities (Owned) — split out in v2.2

Bass personalities, not drums — kept separate from the Drums / Rhythm bucket.

* **UJAM Virtual Bassist ROWDY 2** `[DRIVE]` — Select 5; bassist personality (exact style TBD)
* **UJAM Virtual Bassist MELLOW 2** `[PIB]` — bassist personality — separate Plugin Boutique purchase, **not** part of Select 5
* **UJAM Virtual Bassist DANDY** — new in v2.2

### Ghost / Transformation (Owned)

* **Soundtoys Crystallizer** `[PIB]` — ghost/spectral performer. Banjo → ghost harmonics, acoustic guitar → crystalline overtones, vocals → phantom layers, synths → evolving echoes, drums → reverse/glass percussion. Jeremy's highest-priority purchase for the Ghost Pipes concept
* **FOCUS TIME** `[FREE]` — Touch The Universe Productions (VST3; KVR Developer Challenge free release) — **core Ghost Pipes tool, audio software** (the earlier "productivity app" exclusion was wrong). Experimental sample-based instrument and curve-driven time/pitch/texture mangler
* **Gneiss Free Tier** `[FREE]` — Hvoya Audio — morphing nonlinear multi-stage filter/resonator/chaos processor (not a conventional synth)
* **Retrospect** `[FREE]` — Conceptual Machines — rolling-buffer, curve-controlled time-warp effect (freeze, stretch, reverse, stutter within a beat); VST3/AU/CLAP/LV2
* **Scintillate** `[FREE]` — Sweet Audio in collaboration with Signalsmith Audio — free spectral reverb ("Sparkle Engine"); identified by Jeremy as the KVR Developer Challenge 2026 winner
* **Glitchmachines Fracture** — new in v2.2
* **Glitchmachines Hysteresis** — new in v2.2
* **TugMoveEffect** `[DIRECT]` — 2Rule / Tuğrul Akyüz; Gumroad purchase confirmed
* **TugGlicento V3** `[DIRECT]` — 2Rule / Tuğrul Akyüz; Gumroad purchase confirmed
* **TugPhonon** `[DIRECT]` — 2Rule / Tuğrul Akyüz; Gumroad purchase confirmed

**FOCUS TIME — detail.** Load a sample, draw movement on a tempo-synced timeline, and apply the same curve gesture across twelve stackable engines: Warp, Stretch (Paulstretch-style, 2x–500x), Formant, Repeat, Tape, Delay, Scrape, Vowel, Freq Shift, Spring, LFO, and Harmonic (16-partial additive resonator). Master Filter and Volume curves plus a global Spread/Motion macro. Routing: Series, Parallel (automatic Haas de-phasing), Bed + Series, and **Loop Sends** (tabs act as wet sends around a shared loop — especially useful for drum-loop manipulation). MIDI play or Standalone Play; presets recall sample paths. **Ghost Pipes role (★★★★★ core):** a major physical-world/sample transformation instrument, not a utility — Tascam X8 field recordings, contact/geophone-type recordings, acoustic instrument captures, percussion, environmental textures, and loops that need to become playable/evolving instruments.

**Gneiss — detail.** Resonant prefilters, Moog-style ladder stage, nonlinear/chaotic Break behavior, morphing parameter field, RAND/MUTATE, MIDI CC mapping, MIDI-note cutoff/resonator control, and a customizable USER performance page (from the supplied manual). **Ghost Pipes role:** expressive continuous-control processing — especially suited to Touché-style mapping, percussion, and physical-world source material.

**Scintillate — detail.** Sparkles are generated inside the spectrum of a conventional reverb; spawn and decay move from subtle spectral highlights through fluttering walls of sound and reverse-like effects. Lower density lets only the loudest sparkles through, giving a spectral-gate behavior. **Ghost Pipes role:** spectral/spatial transformation of instruments, vocals, percussion, and captured physical-world material.

**Retrospect — Ghost Pipes role:** live buffer/time manipulation and rhythmic transformation.

### Physical World / Resonance (Owned)

* **AudioThing Fog Convolver 2** `[PIB]` — physical world builder / resonance-environment IR processor. Pairs with Crystallizer to give the "ghosts" a physical body to live inside (e.g. Banjo → Fog Convolver [wood body IR] → Crystallizer → Phantom Rooms)

### Effects / Sound Design (Owned)

* **Valhalla Supermassive** `[DRIVE]` — massive atmospheric spaces
* **Valhalla Space Modulator** `[DRIVE]` — modulated movement
* **Valhalla Freq Echo** `[DRIVE]` — experimental echo
* **AudioThing Things Bundle** `[PIB]` — Texture (atmosphere/reverb), Motor (modulation), Crusher (destruction), Flip EQ (tone shaping), Bubbles (multi-effect), Voice (compression/voice processing), Fold (distortion)
* **AudioThing Speakers** `[PIB]` — physical coloration / cabinet character
* **Output FX Bundle** `[PIB]` — Portal, Movement, Thermal, and other FX instruments/effects — modern sound transformation
* **Serato Hex FX** `[PIB]` — multi-effect plugin
* **Kilohearts Essentials** `[PIB]` — free multi-effect bundle
* **Blue Cat's Freeware Plug-ins Pack II (Bundle)** `[PIB]` — freeware utility/FX bundle
* **Baby Audio Magic Switch** `[PIB]` — "vibe"/character utility effect
* **BEATSURFING VRAC+** `[PIB]` — performance/sequencing effect — owned. The product is **VRAC+**; no separate "VRAC" entry is carried unless evidence of a separate entitlement appears
* **Haze** (Lunacy) `[PIB]` — maker resolved in v2.2; function not recorded by the audit 🚩 see [[open-flags]] #13
* **Safari Audio Time Machine** `[DIRECT]` — direct Safari Audio purchase confirmed — new in v2.2
* **Double Freak** `[FREE]` — Safari Pedals; function not recorded by the audit — new in v2.2

### General FX / Collections (Owned) — new category in v2.2

* **Guitar Rig 7 LE** — new in v2.2
* **UJAM NEO / Finisher** — where represented by the confirmed Plugin Boutique library — new in v2.2
* **Xynth Audio LePhonk** — new in v2.2
* **United Plugins Bassment Core** — new in v2.2
* **W.A. Production / MeldaProduction / United Plugins gift bundle** — new in v2.2

### Saturation / Character (Owned)

* **XLN Audio RC-20 Retro Color** `[PIB]` — tape/vintage degradation
* **Black Box Analog Design HG-2** `[PIB]` — (also distributed via Plugin Alliance — same product, one entry) — analog harmonic enhancement
* **Ampex® ATR-102 Mastering Tape Recorder** `[PIB]` — (Universal Audio) — tape mastering character
* **Wave Arts Tube Saturator Vintage** `[PIB]` — tube-saturation freeware — maker resolved in v2.2
* **Tritik Krush** `[FREE]` — bitcrusher/distortion (per the v2.0 manifest); owned/acquired free, **RESTORED in v2.2** — the v2.1 "dropped" decision is superseded by Jeremy's explicit October decision. Not yet installed on the 7550; local installer archived; developer: Tritik
* **Moogerfooger MF-109S Saturator** — new in v2.2
* **Minimal Audio Saturator** — new in v2.2
* **Baby Audio Parallel Aggressor** — new in v2.2
* **Arturia Drive Mod** — new in v2.2

### Dynamics / Mixing (Owned)

* **Empirical Labs EL8 Distressor Compressor** `[HARDWARE TIED]` — (Universal Audio) — character compression — hardware-bundled entitlement; ownership resolved in v2.2
* **IK Multimedia Black 76** `[PIB]` — FET compression
* **Oxford Inflator** `[PIB]` — (Sonnox) — loudness / density
* **Sonible learn:EQ** `[PIB]` — intelligent EQ
* **LVC-Audio ClipShifter** `[PIB]` — clip-gain/dynamics utility
* **EQ Academy** `[PIB]` — EQ training/utility tool
* **HoRNet MagnusLite** `[PIB]` — loudness/limiting utility
* **iZotope Ozone EQ** `[PIB]` — free mastering EQ module
* **Limiter No6** `[PIB]` — freeware mastering limiter
* **UAD LA-2A Tube Compressor** — new in v2.2
* **iZotope Neutron 4 Elements** — new in v2.2
* **iZotope Ozone 11 Elements** — new in v2.2
* **Endorphin.es Golden Master** — new in v2.2
* **Mastering The Mix RESO** — new in v2.2
* **Pulsar W495** — new in v2.2
* **Excite Audio Lifeline Console** — Full/Lite entitlements represented in the library — new in v2.2
* **Excite Audio Lifeline Expanse** — Full/Lite entitlements represented in the library — new in v2.2
* **StereoSavage 2 Elements** — new in v2.2
* **Audified NITHON** — new in v2.2

### Reverb / Space (Owned)

* **10 Phantom Rooms MR Bundle** `[DRIVE]` — (Native Instruments) — cinematic environments
* **Eventide Blackhole** `[PIB]` — impossible space reverb — owned (confirmed Plugin Boutique purchase; moved from Master Wishlist in v2.2)
* **Klevgrand R0verb** `[HARDWARE TIED]` — creative multi-delay reverb — confirmed bundled with Novation Launchkey 25 mk4
* **ZAK Sound Deep Waters** `[PIB]` — ambient reverb
* **Audified ToneKnob Stargazer** `[PIB]` — character reverb
* **Smartelectronix Ambience** `[PIB]` — freeware reverb
* **Exponential Audio R4 Reverb** — new in v2.2
* **KSHMR Reverb** — new in v2.2

### Vocal Processing (Owned)

* **BLEASS Vox** `[PIB]` — vocal transformation. Now the primary vocal chain following the removal of the Boss VE-22 hardware unit (see [[01.6-synth-bay]]) — Owned
* **Waves Silk Vocal** — new in v2.2
* **Antares Auto-Tune Access** — new in v2.2
* **Soundtoys MicroShift** — new in v2.2

*Neural DSP Mantra is **not owned** (removed from the committed-purchase list in v2.2) — see "Not Confirmed Owned" below and [[open-flags]] #14. MNTRA Instruments FLTRS-LE (Filters, below) and relevant AudioThing / Output processors also serve vocal work.*

### Filters / Modulation / Motion (Owned)

* **Denise Audio Motion Filter** `[PIB]` — moving filter
* **ALM / Busy Circuits MFX Modulations** `[PIB]` — modulation source
* **Minimal Audio Hybrid Filter** `[PIB]` — creative filtering
* **Minimal Audio Formant** `[PIB]` — formant filter, pairs with Hybrid Filter
* **Excite Audio Motion: Fractal** (**Full version**) `[PIB]` — granular movement — originally owned as Lite; upgraded to Full (tier resolved in v2.2)
* **Excite Audio Motion: Dimension** — new in v2.2
* **AudioThing Filterjam** `[PIB]` — filter-focused effect
* **MNTRA Instruments FLTRS-LE** `[PIB]` — filter plugin (Lite edition)

*(See also Gneiss Free Tier under Ghost / Transformation, and Valhalla Space Modulator / Freq Echo under Effects / Sound Design.)*

### Distortion / Drive (Owned)

* **DriveLE** `[PIB]` — (Plugin Boutique)
* **Gorilla Drive** `[PIB]` — (Safari Audio)
* **Disto-blast** `[PIB]` — (Audio Blast) — high-gain digital distortion and aggressive sonic clipping
* **Venomode Mesa Lite** `[PIB]` — amp-style distortion (Lite tier)

### Loop / Sample Tools (Owned)

* **Loopcloud** `[HARDWARE TIED]` — cloud-based sample manager and rhythmic loop sequencer — hardware-bundled entitlement; ownership resolved in v2.2
* **Audiomodern OPX** `[HARDWARE TIED]` — sampler / sound source — hardware-bundled entitlement; ownership resolved in v2.2
* **Audiomodern Loopmix** `[PIB]` — loop/sample playback tool — confirmed on Plugin Boutique invoice
* **Loopmasters Daft Funk 3** `[PIB]` — house instrument
* **Ueberschall Downtempo Beats** `[PIB]` — groove source
* **United Plugins Relooper** `[PIB]` — rhythmic loop/glitch tool — owned (moved from Master Wishlist in v2.1)

*(FOCUS TIME is also a loop/sample manipulation tool — see Ghost / Transformation.)*

### MIDI / Composition / Performance (Owned) — new category in v2.2

* **Scaler 2** — new in v2.2
* **InstaChord 2** — new in v2.2
* **InstaScale** — new in v2.2
* **W.A. Production Chords** — new in v2.2
* **BEATSURFING Beatfader** — new in v2.2
* **W.A. Production Audio AI Tools** — new in v2.2
* **Excite Audio VISION 4D** — new in v2.2

Additional sequencing/generative behavior already exists in FOCUS TIME, Pathfinder, Chippo, and Ableton / Max for Live. Consider this existing depth before purchasing further MIDI-composition tools (e.g. InstaComposer 3, Loop Engine 3).

### Soundware / Expansions / Content (Owned) — new category in v2.2

Content and expansions — tracked as soundware, not as independent plugin instruments, unless an item actually contains a separate plugin:

* Baby Audio Cinematica | Atoms Expansion
* Excite Audio Expanse Lite | Lifeline Expansion
* Future Retro Synthwave — Loopmasters
* Gravitation Atmospheric Soundscapes 3 — Loopmasters
* Quantum Summer — Savant Audio Labs / Producer Loops
* Sychronicity — Producer Loops
* Serum Expansion Pack: Hype
* MNTRA Sound Sculpture Bundle
* Safari Soul Drums Sample Pack
* (Dan Mayo Everything Bundle content — see Drums / Rhythm Personalities; Loopmasters Daft Funk 3 and Ueberschall Downtempo Beats — see Loop / Sample Tools)

### Curation Guidance (v2.2)

The October audit shows Ghost Pipes has no meaningful gaps in ordinary plugin categories. The distinctive software center is:

> **captured physical sound → playable/sample transformation → nonlinear/spectral/time manipulation → strange spatialization**

Key tools in that chain: FOCUS TIME, Gneiss, Scintillate, Retrospect, Motion: Fractal Full, VRAC+, KAZU, Annulus, Atoms, Tomofon, Crystallizer, Output Portal, Fog Convolver 2, Eventide Blackhole, the NI 10 Phantom Rooms MR Bundle, and Ableton's native spectral/resonator/convolution tools.

**Purchasing rule going forward:** new software must answer — *can this create a meaningful interaction, performance behavior, or sonic result the current Ghost Pipes library cannot reasonably produce?* "Another good synth / reverb / distortion / drum machine" is not sufficient. Favor unique interaction models, physical/acoustic transformation, expressive controller mapping, live reliability, deterministic recall, and low performance-time cognitive load. Front-load complexity into programming.

### Recovery / Access Map (v2.2)

For workstation rebuilds and license recovery. **The live rig must never depend on internet access to these services during performance.** No keys, serials, or credentials are recorded here.

| Ecosystem | Recovery / access |
|---|---|
| Ableton | Ableton account / installer / authorization |
| Arturia | Arturia Software Center / registered Arturia account |
| Native Instruments | Native Access / registered NI account |
| Novation-bundled software | Registered Novation account / bundled-software entitlement path |
| UJAM | UJAM App → sign in → My Products → install/activate |
| Plugin Boutique | Account → My Products → serial/download/vendor authorization instructions |
| Dan Mayo | Web download portal via original entitlement email; regenerate link when needed |
| Crow Hill | Crow Hill App → account → Pocket Strings |
| 2Rule / TUG | Gumroad Library/account |
| Phase Fiasco | Lemon Squeezy receipt/order entitlement |
| Safari Audio | Safari Audio user area + serial/license where applicable |
| Valhalla free plugins | Archived installers and/or official Valhalla free-plugin downloads |
| Tritik Krush | Archived installer and Tritik source |
| Gneiss | Archived Free Tier package; Hvoya Audio |
| FOCUS TIME | Archived VST3/download + factory bank; Touch The Universe Productions |
| Scintillate | Sweet Audio source |
| Retrospect | Conceptual Machines source / archived free download |
| Other intentional free plugins | Local installer archive plus verified developer/source metadata |

### Not Confirmed Owned (v2.2)

Do **not** promote these into the owned inventory without new purchase/account evidence — and do not infer ownership from prior discussion, sale pricing, marketing emails, cart activity, or wishlist status. Appearing here does not by itself mean an item is on the wishlist.

* **Neural DSP Mantra** — previously logged as "Pending Purchase, committed"; **not owned** (see [[open-flags]] #14)
* **Neural DSP Darkglass Ultimate** — previously logged as "Pending Purchase, committed"; **not owned**
* Eventide **H3000 Factory Mk II** — *(Blackhole is confirmed owned; H3000 Factory Mk II is not)*
* Expressive E **Noisy 2**
* Expressive E **Soliste**
* Glitchmachines **Palindrome 2**
* Glitchmachines **Tactic 2**
* Safari Pedals **MEAW Chain**
* **Serato Sample**
* MNTRA **El Jaguar**
* W.A. Production **InstaComposer 3**
* W.A. Production **Loop Engine 3**

### Master Wishlist (Considering / Not Yet Purchased)

Per Jeremy's "most up to date wantlist" (superseding all prior wishlist entries). **v2.2: Eventide Blackhole moved to Owned above — removed from this list.** (Baby Audio Atoms, United Plugins Relooper, and BEATSURFING VRAC+ moved in v2.1; KAZU, the Dan Mayo Everything Bundle, the Motion: Fractal Full upgrade, Glitchmachines Fracture/Hysteresis, and Tritik Krush are likewise owned and do not belong on any candidate list.)

1. Soundtoys Little AlterBoy — vocal pitch/character processor
2. MNTRA Instruments El Jaguar — world/ethnic instrument *(a different company from Neural DSP — coincidental name similarity to "Mantra," kept as a distinct item; not owned)*
3. Eventide H3000 Factory Mk II — classic Eventide transformation *(not owned)*
4. Baby Audio Complete Bundle — 🚩 now that Atoms is independently owned, confirm whether this still stands as-is or should be re-scoped, see [[open-flags]] #13
5. Expressive E Noisy 2 — feedback-loaded soft clipper
6. AudioThing Magical Toy Keyboard
7. AudioThing Toy Bars
8. AudioThing Wood
9. Devious Machines Infiltrator 2
10. Aberrant DSP Complete Bundle
11. Cableguys ShaperBox 3 Bundle

*Dropped from the wishlist in v2.0 (not on the current wantlist): FM8 (turned out to already be owned, not dropped after all), Serum Expansion Pack: Hype, UJAM BM Nemesis, UJAM BM Void, Madrona Labs Kaivo, Minimal Audio Rift, Detroit Drums, and the standalone Baby Audio Atoms / Transit 2 entries (folded into the Complete Bundle, then Atoms separately confirmed owned in v2.1 — see above).*

*Neural DSP Mantra and Neural DSP Darkglass Ultimate were previously tracked as committed purchases. As of v2.2 they are **not owned** and appear under "Not Confirmed Owned" above; whether either remains a planned purchase is not recorded.*


---


# 1.8 The Bridge: Physical Data Routing & Global Umbilicals

This section establishes the definitive physical "Ground Truth" for all long-run stage umbilicals, structural data pipelines, and the floor-mounted MIDI network to enforce conflict-free stage operations.

## I. Global Data Umbilicals & Infrastructure Nodes

### AV Access U2EX60 (Data Pipeline Node)
* **Hardware Type**: USB-over-Cat6 Long-Distance Hardware Data Extender
* **Physical I/O**: USB Type-B Input (Transmitter side) / Shielded RJ45 In-Out Ports / Quad USB Type-A Ports (Receiver side)
* **Ground Truth Path**: A short physical USB cable runs from the MC6 Pro into the local transmitter. A 25ft rugged, shielded Cat6 Ethernet cable runs across the physical stage floor to the receiver at the table, docking directly into the active Acasis hub
* **Hardware Role**: Master physical data trunk line bridging the floor controller straight to the workstation hub
* **Power Hardware**: 5VDC External Power Adapter module connected to the local table Desk Clamp Power Strip
* **Status**: Owned Physical Asset

### AV Access U2EX60 (Audio Pipeline Node)
* **Hardware Type**: USB-over-Cat6 Long-Distance Multi-Channel Digital Audio Extender
* **Physical I/O**: USB Type-B Input (Transmitter side) / Shielded RJ45 In-Out Ports / USB Type-A Output (Receiver side)
* **Ground Truth Path**: A physical USB cable carries audio out from the Dell Precision 7550 into the table transmitter. A 25ft rugged, shielded Cat6 Ethernet line runs across the stage floor into the receiver mounted inside the 8U/10U Rack rails, plugging straight into the WING's USB input card
* **Hardware Role**: High-bandwidth data highway delivering multi-track digital audio streams to the main mixer
* **Power Hardware**: 5VDC External Power Adapter module connected to the local table Desk Clamp Power Strip
* **Status**: PENDING PURCHASE Requisition Target

### Behringer SC-U StageConnect
* **Hardware Type**: Ultra-Low Latency Multi-Channel High-Speed Digital Audio Bridge Hardware
* **Physical I/O**: Master StageConnect XLR Port / USB Type-B Master Host Port / Stereo 1/4" Balanced Line Outputs
* **Ground Truth Path**: A single physical XLR cable connects the StageConnect port directly to the master port on the back of the WING Rack mixer. A short physical USB cable links the host port directly to a port on the Dell Precision 7550
* **Hardware Role**: Low-latency high-density injection pipeline processing multi-channel synthesizer audio streams
* **Power Hardware**: External DC Hardware Transformer or active USB host bus power tracking
* **Status**: Owned Physical Asset

## II. The Mothership Hardware Distribution (The DIN Highway)
Driven out of the active **Hardware** MIDI Solutions Quadra Thru box to establish clean data flow across the primary floor island.

* **Master Ground Truth Path**: A physical 5-pin DIN cable routes from the Morningstar MC6 Pro MIDI OUT hardware jack directly into the MIDI IN hardware jack of the Quadra Thru box.
* **Physical Hardware Lane 1 (The Routing Matrix)**: A physical 5-pin DIN cable routes from Output 1 of the Quadra Thru box into the Morningstar ML10X #1 MIDI IN port. A second physical 5-pin DIN cable loops from the ML10X #1 MIDI THRU port straight into the Morningstar ML10X #2 MIDI IN port. Focus: Automates matrix loop switching across both units.
* **Physical Hardware Lane 2 (The Delay/Modulation Block)**: A physical 5-pin DIN cable links Output 2 of the Quadra Thru box into the Boss DD-500 MIDI IN port. Separate physical 5-pin DIN lines chain sequentially from the Boss DD-500 THRU port into the Boss RV-500 MIDI IN, and out from the RV-500 THRU port straight into the Strymon Mobius MIDI IN port. Focus: Delivers master clock data and structural preset changes.
* **Physical Hardware Lane 3 (The Gain Block)**: A physical 5-pin DIN cable routes from Output 3 of the Quadra Thru box straight into the Boss OD-200 MIDI IN port. Focus: Automates drive models and gain adjustments.
* **Physical Hardware Lane 4 (The Glitch Block)**: A physical 5-pin DIN-to-1/4" TRS (Type A) specialized adapter cable routes from Output 4 of the Quadra Thru box directly into the Red Panda Particle 2 1/4" TRS MIDI IN port. Focus: Passes expression scaling values and time divisions.

## III. The Sideboard & Expression Hardware (The Omniport Network)
Crosses the structural floor frame gap driven out of the Morningstar MC6 Pro Omniport hardware array.

* **Makerspace Baseline**: The four 1/4" TRS Omniports are independently programmed to manage direct analog expression or custom TRS MIDI formatting parameters.
* **Ground Truth Path 3A** — updated in v2.0: A physical 1/4" TRS patch cord routes from the Dunlop Mini Expression pedal — now mounted on the **Sideboard** — crossing the board gap (Techflex-sleeved mini umbilical, same style as Path 3B below) into Omniport 1 of the MC6 Pro housing on the Mothership. Focus: Direct manual parameter foot sweep tracking.
* **Ground Truth Path 3B**: A physical 1/4" TRS cable (packed cleanly inside a Techflex-sleeved mini umbilical loom crossing the board gap) routes from Omniport 2 of the MC6 Pro directly into the Boss RC-500 MIDI IN port. Focus: Playback start/stop synchronization.
* **Ground Truth Path 3C**: A secondary physical 1/4" TRS patch cord chains from the Boss RC-500 MIDI THRU port straight into the Boss SL-2 Slicer MIDI IN port. Focus: Strict rhythmic chopper pattern synchronization.

## IV. The Global Audio Umbilicals (Stage Snake Mapping)
This defines the absolute conflict-free physical map of the primary multi-conductor stage snake running straight to the console rails.

* **Master Trunk Parameters**: The heavy Seismic Audio SACB-24x8x25 stage box rests flat on the stage surface. Its 25ft thick multi-conductor core trunk runs across the floor to secure straight into the rear preamps of the WING Rack console inside the flight case rails.
* **Snake Input 01**: **Physical** XLR cable routing from the SOLOMON MiCS LoFreq (Kick Drum - External) **Hardware** transducer
* **Snake Input 02**: **Physical** XLR cable routing from the Shure BETA 91A (Kick Drum - Internal) **Hardware** boundary condenser
* **Snake Input 03**: **Physical** XLR cable routing from the Audix F9 (Hi-Hat) **Hardware** condenser microphone
* **Snake Input 04**: **Physical** XLR cable routing from the Audix F9 (Overhead L) **Hardware** condenser microphone
* **Snake Input 05**: **Physical** XLR cable routing from the Audix F9 (Overhead R) **Hardware** condenser microphone
* **Snake Input 06**: **Physical** XLR cable routing from the Audix F2 (Tom 1) **Hardware** dynamic microphone
* **Snake Input 07**: **Physical** XLR cable routing from the Audix F2 (Tom 2) **Hardware** dynamic microphone
* **Snake Input 08**: **Physical** XLR cable routing from the Audix F5 (Bottom Snare) **Hardware** dynamic microphone
* **Snake Input 09**: **Physical** XLR cable routing from the Shure BETA 57 (Top Snare) **Hardware** dynamic microphone
* **Snake Input 10**: **Physical** 1/4" Mono TS to XLR breakout cable routing from the Stylophone Theremin **Hardware** analog output
* **Snake Inputs 11 – 12**: 🚩 **OPEN / UNASSIGNED (v2.0)** — see [[open-flags]] #5. Formerly the DSM Simplifier Acoustic Feed (L/R) from the now-deleted Acoustic Board; held open pending the Martin X-Series' replacement DI routing decision.
* **Snake Input 13**: Balanced **Physical** XLR line connection routing from Output L of the Walrus Canvas Stereo DI **Hardware** enclosure on the Sideboard
* **Snake Input 14**: Balanced **Physical** XLR line connection routing from Output R of the Walrus Canvas Stereo DI **Hardware** enclosure on the Sideboard
* **Snake Input 15**: 🚩 **OPEN / UNASSIGNED (v2.0)** — see [[open-flags]] #6. Formerly the Roland SPD-One Kick, removed from inventory entirely.
* **Snake Input 16**: **Physical** XLR cable routing from the modified Phone Receiver Microphone **Hardware** vocal transducer
* **Snake Inputs 17 – 22**: Open **Physical** hardware lines reserved with unassigned status to allow for future stage infrastructure expansion
* **Snake Input 23**: **Physical** XLR cable routing from the Shure SM57 (Percussion L) **Hardware** dynamic microphone
* **Snake Input 24**: **Physical** XLR cable routing from the Shure SM57 (Percussion R) **Hardware** dynamic microphone

## V. Section 1.8 Master Cabling Manifest (The External Bridges)
* **24x8 XLR Low-Profile Stage Snake**: 1x Seismic Audio SACB-24x8x25 hardware trunk (25ft) | Connects all floor nodes directly to the 8U/10U Rack engine
* **Cat6 Ethernet Cable (Rugged/Shielded)**: 2x Shielded Cat6 lines (25ft) | Carries long-run data streams for the U2EX60 MIDI and WING audio pipelines across the floor
* **5-Pin DIN MIDI Cable**: 6x Standard DIN lines (1ft-3ft) | Interconnects the MC6 Pro, Quadra Thru, and floor processors across the Mothership
* **5-Pin DIN to 1/4" TRS (Type A) Adapter**: 1x Custom adapter line (1ft-2ft) | Connects Quadra Thru Lane 4 directly to the Red Panda Particle 2 loop entry port
* **1/4" TRS Control Cable**: 3x Balanced lines (2ft-4ft) | Specialized inter-board analog control routing links
* **USB Type-B to Type-A Cable**: 1x Shielded data line (3ft-6ft) | Feeds the physical MC6 Pro controller directly into the local table transmitter extender
* **XLR Male to Female Stage Cable**: 2x Shielded mic lines (15ft) | Connects standalone vocal and chaos microphones from stands to the main Snake Box ports
* **Morley ABC–to–EUNA Cable** — new in v2.0: 1x 1/4" TS gap-crossing cable (Sideboard → Mothership), carries the switched raw instrument signal from the relocated Morley ABC pedal to the 29 Pedals EUNA input. See [[01.2-mothership-and-sideboard]] for context — an unbuffered high-Z signal over a longer run than the pre-v2.0 layout, so a shielded, low-capacitance cable is recommended.


---


# Neural Ripple Concerns: v2.0 Consolidated Failure Modes

* **Gain Staging (Dojo-DLX Factor)**: Calibrate ML10X #1 input levels specifically for high-voltage magnetic **Hardware** components to prevent overloading the discrete analog routing core.
* **Umbilical EMI Risk**: High-fidelity **Physical** shielded cabling is mandatory across all 25ft runs to prevent cross-talk between high-speed data lines and high-gain audio blocks. **v2.0: this now also applies to the new Morley-ABC-to-EUNA gap-crossing cable** (see [[01.8-bridge]]), which carries an unbuffered high-Z instrument signal over a longer run than before.
* **The Manual Swap Bottleneck**: Completely resolved via the **Physical** deployment of the Morley ABC Pedal to swap analog input instruments dynamically without hot-swapping patch cords. *(Still valid in v2.0 — the pedal relocated to the Sideboard but its function is unchanged.)*
* **Stage Bleed**: Aggressive **Hardware** gating and strict **Physical** microphone null placement are mandatory to protect lo-fi vocal elements from acoustic drum kit reflections.

### Operational Ripple Effects
* **Roland P-6 Loop Dependency**: Unmuting WING **Hardware** rack buses that route to the P-6 analog inputs requires immediate **Physical** hardware bypass (`[MFX] + [LO-FI]`) to kill potential digital feedback loops.
* **Electromagnetic Crosstalk** — reworded in v2.0: **If the ART T8 is installed** (its status is now Conditional — see [[01.6-synth-bay]], only added if hum/squeal actually appears at the SC16-I), the Dell 7550's **Physical** power transformer block must reside exclusively on the isolated floor power distribution array to eliminate 60Hz induction hum across the ART T8's nearby analog transformer coils.
* **Preamp Tolerances**: Static **Physical** patch lines connecting consumer-level gear to the SC16-I input block require software gain offsets ($+6\text{ dB}$ to $+12\text{ dB}$) inside the digital mixer to align line levels with balanced industrial **Hardware** specifications.
* **Stage Snake Resolution Lock** — reworded in v2.0: Channels **01–09** remain a contiguous, clear block for the acoustic drum microphone array. Channels **11–14** remain a reserved **Physical** midrange block for Sideboard/DI line feeds — **Inputs 13–14** carry the Walrus Canvas Stereo DI feed, while **Inputs 11–12 are currently open/unassigned** pending the Martin X-Series' replacement DI routing decision (the Acoustic Board that formerly fed 11/12 was deleted in v2.0 — see [[01.1-physical-instrument-manifest]] and [[open-flags]] #1). This block should be treated as reserved-but-not-fully-resolved until that decision lands, rather than "permanently resolved."

---

*(v2.0 removal note: the prior "Active Piezo Overdrive" bullet — which called for auditing gain staging at the LR Baggs Session interface — has been removed. That hardware no longer exists; it was part of the deleted Acoustic Board, see [[01.1-physical-instrument-manifest]] and [[open-flags]] #1.)*


---


# 🚩 Open Flags — Chapter 01 (v2.2)

Running list of unresolved decisions and unconfirmed assumptions. Ask Claude for this list anytime — "what are the flags."

1. **Martin X-Series acoustic routing** — [[01.3-acoustic-board|The Acoustic Board]] is deleted; the Martin needs a new DI/preamp path suited to its active/powered Fishman pickup. **UNRESOLVED — no hardware chosen yet.** See [[01.1-physical-instrument-manifest]].
2. ~~Morley-ABC-to-EUNA cable~~ — RESOLVED. Registered in [[01.8-bridge]] Section V as a new 1/4" TS gap-crossing line.
3. **1.1 internal cable length** — the Meteora/Gretsch instrument cable length spec may be stale now that the Morley ABC pedalboard sits at the Sideboard rather than the Mothership. **STILL OPEN.** See [[01.1-physical-instrument-manifest]].
4. ~~1.8 Path 3A wording~~ — RESOLVED. Reworded to note it crosses the board gap.
5. **Snake Inputs 11/12** — kept open/unassigned pending the Martin's replacement DI routing (Flag #1). Do not reassign yet.
6. **Snake Input 15** — Roland SPD-One Kick removed from inventory; input is open/unassigned. Still open whether a replacement kick trigger gets chosen later.
7. ~~1.8 Stage Snake Mapping sync~~ — RESOLVED. Synced with 1.4.
8. ~~SC16-I Inputs 9–10~~ — RESOLVED. Vocal/gain processing moved to software (BLEASS Vox + Neural DSP Mantra).
9. **New Synth Bay controller specs** — KeyLab MkII 61, Native Instruments Maschine, Expressive E Touché SE, and Novation Launch Control XL Mk3 were added using known public product specs, but exact model numbers and Acasis hub port assignments are assumptions, not stage-verified. Specifically: (a) exact Maschine model — "Mk3" hardware assumed; (b) exact Novation unit — "Launch Control XL Mk3" assumed. See [[01.6-synth-bay]].
10. ~~**Unidentified downloaded plugins**~~ — RESOLVED (October 2026 audit). Jeremy confirmed the local-download plugins were intentionally acquired free plugins; ownership is not an open question merely because installation hasn't begun. Identified and filed in [[01.7-workstation]]: Annulus (Phase Fiasco; Lemon Squeezy receipt), Chippo (free chiptune/retro-digital instrument and pattern generator), Crow Hill Pocket Strings (The Crow Hill Company; $0), Double Freak (Safari Pedals; free), Gneiss (Hvoya Audio; **Free Tier**), Pathfinder (Audio Tech Hub; sample-based instrument/sequencer), Retrospect (Conceptual Machines; rolling-buffer time-warp), Scintillate (Sweet Audio + Signalsmith Audio; spectral reverb / Sparkle Engine), FOCUS TIME (Touch The Universe Productions; audio software), TugMoveEffect / TugGlicento V3 / TugPhonon (2Rule / Tuğrul Akyüz; Gumroad purchases), and Tritik Krush (restored — see #13). *(Remaining gap: Double Freak's function is not recorded — see #13.)*
11. **Evolve Alloy Lite** — *narrowed.* ~~UJAM Mellow 2~~ — RESOLVED: UJAM Virtual Bassist MELLOW 2, owned, separate Plugin Boutique purchase (not part of Select 5), filed under Bass Personalities. Alloy Lite — ownership is confirmed via the Plugin Boutique library; only the **maker and exact functional role remain unconfirmed** (low priority — verify only if the manifest needs a more exact description).
12. **TODO — Post-install deployment verification on the Dell 7550.** *(Purpose rewritten October 2026.)* Current state: **Ableton Live is installed; third-party plugin installation has not begun**, so there is no pre-existing plugin environment to scan — do not run an exploratory "mystery plugin" scan. After a **curated** installation (not "install everything owned"), connect the machine via the Claude desktop app and grant access to the VST3/CLAP install folders (typically `C:\Program Files\Common Files\VST3`, `C:\Program Files\Common Files\CLAP`, plus vendor-specific folders), then verify against [[01.7-workstation]]: owned + intentionally installed; owned + intentionally not installed; installed + activated; installed + documented in the Codex; missing dependencies/content; and unexpected/undocumented installations. This is inference from filenames, not a guaranteed source of truth (no visibility into license/activation status) — worth a manual glance at ambiguous results. The curated install list itself is not yet defined.
13. **v2.1 plugin manifest rebuild** (raised while folding in the curated Plug In Matrix, 102 titles; updated against the October 2026 audit):
    * ~~Arturia Analog Lab Pro~~ — RESOLVED. Jeremy confirmed this is genuinely the Pro edition (owned separately/upgraded), distinct from the base "Analog Lab V" that Arturia's public KeyLab MkII bundle page lists.
    * ~~Tritik Krush~~ — ~~RESOLVED. Confirmed dropped — no longer part of the owned inventory. Removed from [[01.7-workstation]].~~ **SUPERSEDED (October 2026): RESTORED.** Jeremy's explicit decision overrides the v2.1 "dropped" resolution; owned/acquired free, back in the manifest, not yet installed.
    * ~~Baby Audio Atoms, United Plugins Relooper, BEATSURFING VRAC+~~ — RESOLVED. Jeremy confirmed all three were intentional purchases; the moves from Master Wishlist to Owned in [[01.7-workstation]] stand as-is. VRAC+ is the correct product name — no separate "VRAC" item.
    * ~~Hardware-bundle origin unconfirmed~~ for GForce Heritage Synths, UVI Model D, Audiomodern OPX, Loopcloud, UAD Empirical Labs EL8 Distressor, and NI "The Gentleman" — RESOLVED (October 2026): all owned as hardware-bundled entitlements tied to the owned and registered Arturia / Native Instruments / Novation hardware ecosystem. Which exact device supplied each license is deliberately not reconstructed unless needed for license recovery.
    * ~~NI "The Gentleman"~~ — RESOLVED (see above): owned, hardware-bundled entitlement.
    * **Baby Audio Complete Bundle** (still on the Master Wishlist) — now that Atoms is confirmed independently owned, worth confirming whether the Complete Bundle wishlist entry still makes sense as-is or should be re-scoped.
    * ~~"Focus Time"~~ — RESOLVED (October 2026). It *is* audio software: **FOCUS TIME** by Touch The Universe Productions, a free experimental sample instrument / curve-driven time-pitch-texture mangler (VST3), now tracked as a core Ghost Pipes tool. The productivity-app speculation is retired.
    * ~~Excite Audio Motion: Fractal tier~~ — RESOLVED: **Full** version owned (originally Lite; upgraded).
    * ~~UJAM Select 5 contents / ROWDY 2 / FLUXX~~ — RESOLVED: Virtual Drummer BRUTE, Finisher FLUXX, Virtual Bassist ROWDY 2, Beatmaker BERSERK, Groovemate LATIGO. ROWDY 2 is a bassist and FLUXX a finisher — neither is a drummer. All five are available to install and not activated.
    * ~~Newly owned / provenance resolved~~ — RESOLVED: Eventide Blackhole, Phase Fiasco KAZU, Dan Mayo Everything Bundle, Audiomodern Loopmix, Annulus, Pocket Strings, TUG products, Safari Audio Time Machine, Haze (maker: Lunacy), Gneiss Free Tier, Retrospect, Scintillate, Bitwig Studio 8-Track (secondary DAW, not GP core).
    * **Still unconfirmed maker or exact role:** Lineage Percussion, Drumbo Jr., MSoundFactoryPlayer, Reaktor Synthesizer Bundle (which specific instruments), Haze (function), Double Freak (function), and the descriptions of the many entries marked *new in v2.2* in [[01.7-workstation]], which carry only what the audit recorded.
    See [[01.7-workstation]] Section III for where each of these landed in the manifest.
14. 🚩 **Vocal chain references to Neural DSP Mantra** — Jeremy confirmed (October 2026) that **Neural DSP Mantra and Darkglass Ultimate are not owned**; both were removed from the committed-purchase lists in [[01.7-workstation]] and filed under "Not Confirmed Owned." [[01.6-synth-bay]] (the Boss VE-22 removal note and the SC16-I Inputs 09–10 entry) and resolved flag #8 above still describe Mantra as part of the software vocal chain. **Not rewritten here** (hardware section left untouched) — those lines need a decision: the vocal chain is currently BLEASS Vox (owned) only, and it is not recorded whether Mantra or another tool is still planned.
15. 🚩 **Meaning of the `[DRIVE]` tag** — v2.1 defined `[DRIVE]` as a "local C: drive install." The October audit establishes that no third-party plugin is installed on the 7550 yet, so v2.2 redefines `[DRIVE]` as "downloaded/installer held locally; **not an install state**." Confirm this matches how the tag was originally meant (e.g. whether it referred to a different machine's drive), and whether the tag should be retired in favor of the status model in [[01.7-workstation]] Section III.

TEST LINE — the workflow should remove this and restore the file.
