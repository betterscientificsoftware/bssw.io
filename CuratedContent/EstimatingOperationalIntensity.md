# Estimating operational intensity

The operational intensity introduced in the [Roofline model](https://escholarship.org/uc/item/5tz795vq.pdf) -- operations per byte of DRAM traffic -- is a simple model that can be used to determine what architectures are the best match for a given computational kernel or,  conversely, in what ways to optimize a kernel so it performs better on a given architecture. Operational intensity is not typically provided directly by performance tools but can be estimated from other readily available measurements.

#### Contributed by [Boyana Norris](https://github.com/brnorris03)

#### Publication date: November 12, 2017

<!---
Publish: yes
Categories: performance
Topics: High-performance computing (HPC)
Tags: paper
Level: 2
Prerequisites: defaults
Aggregate: none
--->
