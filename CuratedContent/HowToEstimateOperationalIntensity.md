# How to estimate operational intensity

The operational intensity introduced in the [Roofline model](https://escholarship.org/uc/item/5tz795vq.pdf) -- operations per byte of DRAM traffic -- is a simple model that can be used to determine what architectures are the best match for a given computational kernel, or conversely, in what ways to optimize a kernel so it performs better on a given architecture. Operational intensity is not typically provided directly by performance tools but can be estimated from other readily available measurements.


<!---
Publish: yes
Categories: performance
Topics: performance
Tags: HPC
Level: 1
Prerequisites: none
Aggregate: none
--->
