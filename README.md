<div align="center">
  <img alt="boring font logo" src="assets/logo.svg" width="55%">
  <p><sub>You can't optimize what you don't understand.</sub></p>
</div>

---

`cpuperf` aims to prioritize the information that actually matters for performance engineering.

The idea is simple: **understand the hardware before trying to optimize for it.**

## What it does

- Identifies your CPU and architecture.
- Reports available CPU cores and logical processors.
- Explores cache hierarchy and characteristics where available.
- Detects supported instruction-set features where exposed by the system.
- Reports hardware information useful for reasoning about code execution and optimization.

The information available depends on your operating system and hardware.

## Philosophy

Performance engineering starts with understanding the machine.

Rather than treating the CPU as a black box, `cpuperf` aims to make its capabilities easier to inspect and understand. The goal is to build a foundation for informed optimization, one piece of hardware information at a time.

## Design goals

- **No third-party dependencies.**
- **Understandable:** expose hardware information without unnecessary abstractions.
- **Honest:** distinguish detected, inferred, and unavailable information.
- **Portable:** progressively support macOS, Linux, and Windows.
- **Performance-focused:** prioritize information that helps explain how code interacts with hardware.


## Existing tools

Several excellent tools already explore CPU information and hardware topology.

| Tool | Focus |
|---|---|
| [`lscpu`](https://man7.org/linux/man-pages/man1/lscpu.1.html) | CPU architecture, processor counts, caches, and topology on Linux |
| [`cpuinfo`](https://github.com/pytorch/cpuinfo) | Cross-platform CPU, cache, topology, and instruction-set discovery |
| [`hwloc`](https://github.com/open-mpi/hwloc) | Hardware topology, locality, and relationships between computing resources |
| [`py-cpuinfo`](https://github.com/workhorsy/py-cpuinfo) | CPU information exposed through a Python interface |
| [`clinfo`](https://github.com/Oblomov/clinfo) | Information exposed by OpenCL platforms and devices |

These tools solve real problems and are useful references. `cpuperf` is not an attempt to claim that they are inadequate.

However, CPU information is not always presented with performance engineering in mind. 

`cpuperf` aims to prioritize the hardware characteristics that matter when understanding execution behavior and making informed optimization decisions and an opportunity to explore how CPU information can be discovered and interpreted from first principles, using native operating-system interfaces and architecture-specific mechanisms.


