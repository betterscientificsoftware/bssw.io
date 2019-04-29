# When 100 FLOPS/Watt Was a Giant Leap

**Hero Image:**

- <a href='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_agc_part1/Blog_AGCPart1_profile_fullres.jpg'><img src='https://raw.githubusercontent.com/betterscientificsoftware/images/blog_agc_part1/Blog_AGCPart1_profile.jpg' /></a>

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: May 10, 2019

*Part 1 of 3 in the series* The Apollo Guidance Computer Hardware, *a retrospective on the Apollo Guidance Computer commemorating the 50th anniversary of the Moon landing.*

<br> 

This year, July 20 will mark the 50th anniversary of the 1969 Apollo 11 Moon landing.<sup>[1]</sup> Between 1958 and 1965, both Russian and American space programs attempted a total of over 36 unmanned Moon missions.<sup>[2]</sup> Of the 6 that succeeded, none were survivable soft landings. Just crashing into the Moon proved exceedingly difficult. Developing a guidance, navigation, and control (GNC) system for Apollo<sup>[3],[9]</sup> was an enormous challenge. At its heart was a revolutionary new computer: the Apollo Guidance Computer (AGC).<sup>[4],[5],[6]</sup>

In commemoration of that historical achievement, this is the first of three articles about the AGC. Part 1 describes the hardware. Part 2 will describe the software and part 3 its application in Moon missions. In the years since AGC's development, jargon may have changed, but the HPC community will recognize many common themes such as flops/watt power constraints, checkpoint and restart strategies, and the need for performance portability.

### The AGC Architecture: A Giant Leap in FLOPS<sup>a</sup> per W, Kg, m<sup>3</sup> 

Apollo needed a computer orders of magnitude better than those typical of the era: lower power, lighter weight, smaller size, greater reliability, and ability to operate in the extreme environmental conditions of space flight. In mid-1961, NASA accorded MIT/Draper Labs “sole source” status to design the AGC and soon after selected Raytheon to manufacture the hardware.<sup>[6]</sup> Both organizations had been involved in development of the Polaris missile GNC system.<sup>[22]</sup>

<br> 

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0429_computer_875_464.png' class='page' />[The AGC (left) with its Display and Keyboard Interface (DSKY - right)]

<br> 

The AGC was the first computer to use integrated circuits. It was constructed entirely from dual-packaged, 3-input NOR gate flat-packs produced by Fairchild Semiconductor<sup>[23]</sup> in an area that would eventually become known as Silicon Valley.<sup>[43],[44]</sup> At its peak, the effort consumed over 60% of all ICs produced in the country. The AGC used a total of 5,600 NOR gates, operated at 1.024 MHz with a 16-bit word, and had 34 basic instructions each micro-coded into a 12-step sequence. It had 4 central registers plus 15 special-purpose registers.<sup>[19]</sup> The table below compares key AGC performance metrics with an early model of the IBM 360. Both systems were released in 1966, the same year initial designs of the first massively parallel computer, ILLIAC IV,<sup>[30]</sup> were completed. Costing nearly $5 billion to develop, 20% of the entire Apollo budget, the IBM 360 was a big gamble and even bigger success for IBM.<sup>[48]</sup> We also include a row for comparison with IBM’s newest AC922<sup>[45]</sup> based systems (Summit<sup>[28]</sup> / Sierra<sup>[42]</sup>).

System | #units | Kb | Flops (F) | (Watts) F/W | (Kg) F/Kg|(m<sup>3</sup>) F/m<sup>3</sup>
:--- | ---: | ---: | ---: | ---: | ---: | ---:
AGC Block II<sup>[14]</sup> |42 | 76 | 14,245 | (55)<br>259.0 | (32)<br>445 | (00.03)<br>50000
IBM 360-20<sup>[10],[11]</sup> | 7,400 | 32 | 3,011 | (5000)<br>0.6 | (600) 5 | (30.00)<br>100
IBM AC922<br>(Summit<sup>[28],[29],[42]</sup>) | 2 | 1E12 | 14E16| (97E5)<br>14E9 | (31E4)<br>45E10 | (930)<br>15E13

<sup>a</sup>FLOP = single precision multiply + add

### Rope Core: A New Type of NVM

The AGC utilized two types of core memory<sup>[17]</sup>: erasable memory using coincident current cores and fixed (read-only) memory using rope cores,<sup>[18]</sup> technology specifically designed for and unique to the AGC. Both were nonvolatile, providing extra protection against data loss during faults. The advantages of rope core were superlative robustness and significantly higher density because a single core stored 24 bits.<sup>[16]</sup> On the other hand, rope core took weeks of painstaking labor to hand-weave<sup>[15]</sup> thin wires through (logical ‘1’) or around (logical ‘0’) arrays of cores. Bugs were costly to correct and often were just worked around with additional steps in astronaut checklists or even by revising mission parameters. Raytheon was never able to fully automate this crucial manufacturing step. Instead, the company hired an army of experienced textile workers from the New England area, all women. Remarkably, weaving and its place in computing date back more than 150 years *earlier* to the Jacquard loom.<sup>[40],[46]</sup> Present day operating system terms such *core dump* or *core image* are derived from this early memory technology.

<br> 

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0429_RaytheonWorker_875_803.jpg' class='page' />[A worker weaves copper wires through an array of cores for the AGC (Photo courtesy of Raytheon Company)]

### The Executive: An Operating System with Checkpoint/Restart Services
The AGC used a priority-driven, collaborative, multitasking operating system called the Executive.<sup>[26]</sup> Priority-based job scheduling was revolutionary for its time. The Executive could detect a variety of hardware and software faults and had restart utilities to recover. But, only the most critical programs were restart enabled.<sup>[25]</sup> This involved careful design with periodic updates of waypoints and saves of redundant copies of essential state throughout program execution. Restart support consumed resources and complicated testing. In 1968, an internal NASA report<sup>[25]</sup> raised significant doubts about its value. In Part 3 of this series, we’ll describe why it would later be proven invaluable during the Apollo 11 landing.

### The Interpreter: A Domain-Specific Language
The Executive and other system functions were all implemented in AGC native assembly code<sup>[49]</sup>. However, solving complex, 3D spatial navigation problems with this simple instruction set was tedious, error prone, and memory consuming. Early on, engineers designed a higher-level language, called the *Interpreter*,<sup>[26]</sup> to support the complex software required for GNC operations. Operands were scalar, vector, and matrix data types in single, double, and even triple precision. Instructions included vector and matrix arithmetic functions, transcendental functions, float normalization functions and other miscellaneous control-flow functions. It was still a form of assembly language. But, it operated at a much higher level of abstraction easing development, improving overall reliability and helping  reduce memory requirements.

### Multiple Spacecraft Configurations: A Performance Portability Challenge
Apollo wasn't just a single spacecraft. It was two: the Command and Service Module (CSM) and the Lunar Module (LM). Each had its own AGC and was further divided into two stages. Depending on the phase of a mission, the vehicles were joined together in various configurations with dramatically different operating characteristics. Developing a single program, the Digital Auto Pilot (DAP),<sup>[7]</sup> to provide effective GNC for any configuration, even off-nominal cases, presented what amounts to a significant performance portability problem. In Part 2 of this series we'll discuss some of the solutions.

<br> 

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0429_CSM_and_LM_875_493.png' class='page' />[Early NASA artist's rendition of Apollo Spacecraft. Command and Service Module (left) Lunar Module Ascent and Descent Stages (right)]

<br>

The AGC may not have been extreme in scale but it was extreme in reliability. Of the 42 Block II systems delivered and an aggregate of 11,000 hours of vibration and thermal testing plus 32,500 hours of normal operation, only 4 hardware faults were observed,<sup>[41]</sup> and none of these occurred in actual Moon missions. Little did AGC hardware engineers know that writing the software would present even greater challenges, ultimately becoming the rate-determining factor in delivering flight-ready units.

### Author Bio

Mark Miller is a computer scientist supporting the
[WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
He also contributes to [VisIt](https://wci.llnl.gov/simulation/computer-codes/visit),
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo),
[HDF5](https://www.hdfgroup.org) and
[IDEAS-ECP](https://ideas-productivity.org/ideas-ecp/).

[1]: https://www.nasa.gov/mission_pages/apollo/missions/apollo11.html
[2]: https://en.wikipedia.org/wiki/Moon_landing
[3]: https://en.wikipedia.org/wiki/Apollo_PGNCS
[4]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf
[5]: https://en.wikipedia.org/wiki/Apollo_Guidance_Computer
[6]: https://youtu.be/YIBhPsyYCiM
[7]: https://pdfs.semanticscholar.org/0d44/2a1b41da2ccbffeda8aa2e1a7c2417ac71e0.pdf
[9]: https://www.ibiblio.org/apollo/hrst/archive/1713.pdf
[10]: https://en.wikipedia.org/wiki/IBM_System/360_Model_20
[11]: http://www.bitsavers.org/pdf/ibm/360/fe/GC22-6820-12_System_360_Installation_Manual_Physical_Planning.pdf
[14]: https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf
[15]: https://youtu.be/P12r8DKHsak
[16]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf
[17]: https://en.wikipedia.org/wiki/Magnetic-core_memory
[18]: https://en.wikipedia.org/wiki/Core_rope_memory
[19]: https://youtu.be/xx7Lfh5SKUQ
[22]: https://www.computerhistory.org/revolution/real-time-computing/6/128/529
[23]: https://en.wikipedia.org/wiki/Fairchild_Semiconductor
[25]: https://www.ibiblio.org/apollo/hrst/archive/1033.pdf
[26]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf
[28]: https://www.ornl.gov/news/ornl-launches-summit-supercomputer
[29]: https://www.top500.org/green500/list/2018/11/
[30]: https://en.wikipedia.org/wiki/ILLIAC_IV
[40]: https://en.wikipedia.org/wiki/Jacquard_loom#Importance_in_computing
[41]: https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf
[42]: https://hpc.llnl.gov/hardware/platforms/sierra
[43]: https://www.computerworld.com/article/2525898/app-development/nasa-s-apollo-technology-has-changed-history.html
[44]: https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips
[45]: https://www.ibm.com/us-en/marketplace/power-systems-ac922
[46]: http://www.computersciencelab.com/ComputerHistory/HistoryPt2.htm
[47]: https://youtu.be/P12r8DKHsak?t=35
[48]: https://www.telegraph.co.uk/technology/news/10719418/IBMs-5bn-gamble-revolutionary-computer-turns-50.html
[49]: https://www.ibiblio.org/apollo/assembly_language_manual.html

<!---
Image copyright source info…
  Two are public domain...
      * https://commons.wikimedia.org/wiki/File:NASA_spacecraft_comparison.jpg
      * https://en.wikipedia.org/wiki/Apollo_Guidance_Computer#/media/File:Agc_view.jpg
  The Raytheon image I received approval email from Raytheon customer relations
--->

<!---
Publish: preview
Categories: performance
Topics: high-performance computing, performance portability
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
