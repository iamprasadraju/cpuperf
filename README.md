# cpuperf

Inspect CPU to understand its capabilities and make better performance decisions.

`cpuperf` is a lightweight, dependency-free tool for exploring CPU hardware characteristics relevant to performance engineering.

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

