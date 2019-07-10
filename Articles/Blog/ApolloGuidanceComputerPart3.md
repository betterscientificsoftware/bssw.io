# Pre-Reference Version: Celebrating Apollo's 50th Anniversary: User Stories from Space 

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0719_Apollo3.jpg' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: July 15, 2019

*Third of a three-part series to commemorate the 50th anniversary of the Moon landings.*

In the Apollo program, the *end-users* were first and foremost the astronauts who had to fly the
spacecraft the AGC controlled. These people had widely
varying perspectives about how much and what kind of control the computer should have.
Wally Schirra was perhaps the most automation-resistant of the bunch. So much so, he planned to
manually fly the re-entry of Apollo 7. When delays put them dangerously behind
on checklist items, at the last minute he had no choice but to switch to automated re-entry. With
the AGC in control, Apollo 7 splashed down safely, on schedule and within 2 miles of their intended
target. After the mission, Schirra couldn't stop singing the praises of the AGC. He felt it had saved their lives,
giving the crew the extra time they needed to finish stowing equipment, strapping in and preparing
for the ferocity of re-entry.

This is the third of three articles about the AGC. In parts 1 and 2, we described the
hardware<sup>[1]</sup> and software.<sup>[2]</sup> Here, in part 3, we focus on *applications*;
that is experiences in the use of the AGC in actual Apollo missions.

### There are no user stories without verbs and nouns
It is impossible to write about how Apollo astronauts flew to the moon without using `verb`s and
`noun`s. Unlike Kubrik's Apollo era film, *2001: A Space Odyssey*, where the crew held conversations
with their HAL computer, Apollo crews interacted directly with the AGC through EL displays
and a keypad called the DSKY (pronounced *disskee*).<sup>[16],[17]</sup> Verb codes specified an action to take.
Noun codes specified the data upon which the action was taken.<sup>[6]</sup> For example, to
display current velocity, the astronauts would perform the following keystrokes, `Verb`, `0`, `6`,
`Noun`, `6`, `0`, `Enter`. The verb code `06` means to display some data in decimal. The noun code
`60` means the data for velocity. The keystrokes, `Verb`, `3`, `7`, `Noun`, `0`, `1`, `Enter`
meant to begin a pre-launch major mode program to align the Inertial Measurement Unit (IMU). More on that
later from an experience on Apollo 8.

![Apollo DSKY in Command-Service Module (CSM)](https://github.com/betterscientificsoftware/images/raw/master/Blog_0719_agc_dsky.png)

Data displayed to or entered by the astronauts via the DSKY was handled in English units and
converted to/from the Metric system for internal guidance computations. The astronauts sometimes
referred to the AGC as the fourth crew-member. After hundreds of hours training in simulators, they
had AGC *code-speak* memorized and could probably operate it blind-folded. Nonetheless, operating
the DSKY in the thickly gloved hands of a spacesuit, quickly and accurately under the time pressures of critical flight
maneuvers, was not easy. Dave Scott explained that in the lunar module, the computer's *Proceed*
button, the main engine *Shutdown* button, and the *Abort* button were in such close proximity<sup>[3]</sup>,
it would have been very easy for users to hit the wrong button at the wrong time. All the astronauts
had to *...think very hard...* to avoid making such a mistake. This is a surprising vulnerability
to have existed given the amount of human-computer interface design effort that went into the whole
GN&C system.

### What an elementary school girl knew about the AGC that Apollo 8 didn't 
While practicing guidance alignments with the space sextant on the return leg of Apollo 8,
the crew accidentally keyed in a command to start a pre-flight program, `P01`, instead of star
identifier `01` from the AGC's star catalog. This corrupted key guidance parameters in erasable
memory. It took NASA and MIT nine long hours to radio up a fix to the problem. Fortunately, this
incident occurred during a segment of the flight where there were no time-critical maneuvers scheduled.
Little did the crew know that an elementary aged school girl had helped to find this problem and a
program change to fix it had been proposed in the months prior to their flight.

One user nobody had planned for was Margaret Hamilton's daughter, Lauren.
Once while playing astronaut during a visit with her mother at work, Lauren managed to key in
DSKY commands causing an AGC simulator to crash. The simulator was running an in-flight program
and Lauren had keyed in a command to select and run a pre-flight program. Alarmed, Hamilton's
first thought was *what if an astronaut did that in flight?* She investigated the cause and
proposed a program change to prevent such mistakes. However, NASA believed the astronauts were
so well trained they would never make such a mistake and rejected the program change. After the
accidental entry on Apollo 8, the program change was approved and implemented.

### Flashing the AGC with EMPs 
EMPs are Erasable Memory Programs;<sup>[5]</sup> that is, programs stored in erasable rather
than fixed AGC memory. While often used for special purpose ground testing of the AGC, EMPs
were considered too risky because of the last minute changes they enabled.
However, they were used with increasing regularity in later Apollo missions to work in
functionality that had been fully developed but nonetheless couldn't make the typical four
month lead time for rope core manufacture. An early success of EMPs happened on Apollo 9,
an Earth orbital mission to test the lunar module descent and ascent engines and CSM/LM
rendezvous. A key capability the astronauts wanted was to have the AGC maintain the CSM nose
always pointing "down" toward the Earth as it orbited. This meant the CSM needed to rotate in
sync with its orbital position. A program to support this had been developed and tested in
simulators earlier but was not part of Apollo 9's rope core flight program. Once in orbit, the
astronauts entered a few dozen DSKY keystrokes to upload the EMP and it worked exactly how they
wanted it to work.

### Overcooking the barbecue
*Passive Thermal Control (PTC)* or *Barbecue Mode*, is likely the most temperamental maneuver in
the Apollo program. The goal is to spin the spacecraft rotating on its long axis at one to three
revolutions per hour to even out solar heating. The challenge is to get the spacecraft *barbecuing*
such that it can coast for long periods without falling into a bad *wobble*. A wobble can cause
IMU sensor drift, risk of gimbal lock and overuse of RCS propellants. Unless the axis of rotation
is perfectly aligned with a *principle* axis, coasting rotations can be unstable leading to
wobble.<sup>[18],[19],[20]</sup> Rotational behavior and subsequent control is further complicated
when a majority of the spacecraft's mass is fluid such as propellents even if in baffled tanks.

Ultimately, the challenge in this maneuver is getting the angular momentum vector of the barbecue
roll to align well with a principle axis. The more out of alignment these two axes were, the more
wobble and subsequent RCS control to counter the wobble the AGC would have to exert. On Apollo 10,
the recurring RCS jet firings and subsequent spacecraft bending noises ere so problematic, the
astronauts were unable to sleep. NASA asked MIT for a solution.

There are multiple ways to go about getting the spacecraft into the desired roll. One is to seek
a desired angular momentum and simply apply the torque necessary to maintain it. That was the
algorithm MIT had coded into the AGC. That approach creates the need to regularly fire RCS jets
to maintain the torque. But, as MIT thought about the problem, another way to get the spacecraft
into the barbecue roll was to start from zero initial conditions and apply a series of tiny, 
impulsive torques accelerating the rotation to the desired roll rate and then letting the
spacecraft coast thereafter. This latter approach is more likely to result in better alignment
of the barbecue roll with a principle axis. Instead of using the AGC, the astronauts used their
manual hand controllers at minimum impulse. Over a period of 10-20 minutes, they slowly
accelerated the roll with a series of short bursts of the RCS jets. It worked perfectly and
the astronauts got their much needed sleep.

### Cycle stealing gone awry; restart to the rescue
GN&C sensors such as the IMU and radar used the technique of *cycling stealing*<sup>[11]</sup> to update their state in AGC
erasable memory. In cycle stealing, normal program execution is briefly paused. The program counter
temporarily stops incrementing while data from external hardware is routed over the bus to the
computer's erasable memory. In normal operation, delays caused by cycle stealing were insignificant
occurring perhaps dozens of times per second. However, in Apollo 11 there was a phasing problem in the
rendezvous radar circuitry causing cycles to be stolen at their maximum allowed rate of 12,800 times per
second. The resulting delays in essential guidance and control programs meant the computer occasionally
did not have sufficient resources to complete all work within its pre-defined *duty cycle* triggering
program alarms.<sup>[8]</sup>

As Armstrong and Aldrin streaked across the lunar horizon and dropped to the surface, their
DSKY flashed a program alarm, momentarily stopped operating and blanked out. The AGC effectively rebooted.
All running programs were cleared and those that were restart protected were restarted in priority
order according to a pre-programmed set of restart rules. Restart took only a few seconds and had been
designed into the AGC from the very beginning. Remarkably, an internal NASA report<sup>[10]</sup> had
raised significant doubts about its value only months prior to the Apollo 11 mission. As Apollo 11
approached the lunar surface for landing, changing major mode programs from `P64` to `P66`, the
computational load on the AGC lessened and the program alarms abated. 

![Jack Garman's Cheat Sheet of AGC Program Alarms](https://github.com/betterscientificsoftware/images/raw/master/Blog_0719_agc_garman_cheat_sheet.png)

Why wasn't the landing aborted? Turns out it was...in simulations with the Apollo 12 backup crew just
weeks prior to Apollo 11's launch.<sup>[9]</sup> Flight controllers in those simulations were excoriated
for calling an abort then because the circumstances didn't warrant it. At NASA's behest, MIT performed
an audit of all program alarms the AGC could trigger. A 26 year old Jack Garman compiled a cheat sheet,
pictured above, which he consulted during the Apollo 11 landing to give the "go" decision to flight
controllers to continue the landing, a process that took 30 long seconds in which time the LEM dropped
over a mile in altitude and traveled 10 miles downrange.

### "Try SCE to aux"
Less than 30 seconds into the launch of Apollo 12, with the Saturn booster accelerating them 
towards space with 7 million pounds of thrust, much to the surprise of the crew, the AGC
went on the fritz. The DSKY went blank and then the whole cabin lit up with caution and
warning lights and buzzers. Pete Conrad reported "we just lost the whole platform". In
mission control...the same story. All the telemetry went on the fritz. Screens went blank
with gibberish. Nonetheless, John Aarons recognized something familiar in that gibberish.
In simulations years prior to Apollo 12, Aarons had experienced a similar situation
which produced the same screens of gibberish telemetry. He remembered the solution then was to
switch the CSM Signal Conditioning Equipment (SCE) to Auxiliary. Aaron's had mission control radio
up to the crew "Try SCE to Aux." Miraculously, the AGC and all the displays in mission
control came back to life and Apollo 12 safely continued into orbit.

Apollo 12 had been hit by lightning. Fortunately, the AGC was only *monitoring* the Saturn
booster during the launch, not actually controlling it. A second computer, the Launch Vehicle Digital
Computer (LVDC) designed and manufactured by IBM, was controlling the vehicle into Earth orbit.
It performed flawlessly and Apollo 12 went on to perform a pin-point landing
within a short lunar stroll of Surveyor III. To achieve this landing accuracy, AGC software was
enhanced to incorporate tracking telemetry from multiple ground stations simultaneously.

![Left: John Aarons at Mission Control. Right: Pete Conrad of Apollo 12 at Surveyor III with LM Intrepid in the background](https://github.com/betterscientificsoftware/images/raw/master/Blog_0719_agc_apollo_12_and_aarons.png)

### What-if thinking
Early on, MIT engineers adopted a *what-if* approach to software development trying to account
for every possible contingency. For Apollo 9, MIT software developers needed to create a major
mode program that allowed the crew to test the lunar module descent engine while remaining docked
with the CSM, a configuration not ordinarily used or needed for any other Apollo mission. It was
considered the safest configuration for the first ever test of the lunar module.

Instead of removing that code from future flight programs, MIT asked what if we might need that
in a future mission?  The crew of Apollo 13 would benefit from this what-if thinking. The guidance
code that was developed for that configuration remained in the flight program for later Apollo
missions and is what enabled the crew of Apollo 13 to use the LM descent engine for the first two
burns that 1) put them on a free return trajectory and 2) accelerated their return to bring
them home 24 hours sooner. A third burn was also needed but because the AGC had been shut down
to conserve power, a second computer, the Abort Guidance System (AGS), was used. In the third burn,
a guidance technique using the Sun and both end-points of the Earth's terminator was used.
This is something at least one member of the crew, Jim Lovell, had practiced on a prior mission
on Apollo 8.

### A quarter million mile tech support call
During Apollo 14, the *Abort* button in the LEM was found to be faulty. It was occasionally
closing a circuit indicating to the AGC that the *Abort* button had been pushed. This of course
would be disastrous if it occurred during a landing attempt. MIT needed to quickly devise a
procedure the crew could use to allow the landing to proceed without risk of it being inadvertently
aborted due to the faulty switch. Apollo 14 waited, orbiting the moon and delaying their landing
for four long hours as MIT poured over AGC source code looking for a solution that required as few
keystrokes as possible but provided assurance the faulty *Abort* switch would be ignored by the
computer. The fix involved over-writing certain *flag bits* in AGC erasable memory at key points
during the descent.<sup>[15]</sup> Each over-write involved a sequence of verb and noun keystrokes to enter the
desired memory address and mask word to fool the computer into believing one condition or another
was either true or false. Apollo 14 went on to the most accurate landing of all missions, just
175 feet from its target.

### Computing and spaceflight
Computing was an absolutely essential tool for the Apollo program.
Each Apollo lunar landing mission included four on-board guidance computers. There was on AGC in each of the the CSM and LM.
There was also the Launch Vehicle Digital Computer (LVDC) that provided guidance for the Saturn rocket's
first three stages during launch and the Abort Guidance System (AGS) on the LM which served as a backup
to the AGC in case a lunar landing needed to be aborted. Below, we capture some of the key design features
of each of these computers

Computer | Manufacturer | Word (bits) /<br>Memory (Kb) | Clock (Mhz) /<br> Flops (Kf) | Weight (kg) /<br> Power (W) | Notes
---|---|---|---|---|---
LVDC<sup>[13]</sup>|IBM|14, 28.5 |2.048, 3 |33, 137 | triple-redundant logic w/voting
AGS<sup>[12]</sup>|TRW|18, 4.6|??, 12.5|15, 90 | Used in Apollo 9, 10, 11 & 13
AGC|Raytheon|16, 76 | 1.024, 14.5 | 32, 55 | 

But the role computing played in the Apollo program was not confined to autonomous
guidance for the spacecraft in actual missions. Computing and simulation was used by every major
sub-contractor, in every phase of development and in every vehicle and almost every sub-system. Computing was a
key facilitator in providing realistic simulators of the CSM and LM to train Apollo crews. In NASA's
Real-Time Computing Complex (RTCC) alone 5 IBM 360/75s were in use 24/7 during every mission. The RTCC
supported ground tracking and computation of orbits, trajectories, rendezvous solutions, abort
contingencies, weather forecasting and more. NASA would not have met President Kennedy's challenge of landing
people on the moon before 1970 without the major role computers and computing and simulation played. The
Apollo program simultaneously drove innovations in computing and benefited from them.<sup>[14]</sup>

### Author bio

Mark Miller is a computer scientist supporting the
[WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
Among other things, he contributes to
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit),
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo),
[HDF5](https://www.hdfgroup.org) and
[IDEAS-ECP](https://ideas-productivity.org/ideas-ecp/).


[Part 1](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap) | [Part 2](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-the-oldest-code-on-github) | Part 3

[1]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap "AGC Blog Part 1 {}"
[2]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-the-oldest-code-on-github "AGC Blog Part 2 {}"
[3]: https://youtu.be/hCywOf0Czgg?t=1841 "Presentation by Dave Scott about the AGC {}"
[4]: https://www.ibiblio.org/apollo/hrst/archive/1033.pdf "AGC Restart System Design {}"
[5]: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19720025984.pdf "Erasable Memory Programs {}"
[6]: https://www.ibiblio.org/apollo/A17_VN_Checklist.png "Verbs and Nouns Cheat Sheet {}"
[7]: https://youtu.be/22adjMrYl0E?t=20 "Demonstrating DSKY during Apollo 11 {}"
[8]: https://www.doneyles.com/LM/Tales.html "Done Eyles definitive description of Apollo 11 program alarms {}"
[9]: https://www.airspacemag.com/daily-planet/troubleshooting-101-1201-actually-and-1202-too-111339271/ "Program alarms simulation {}"
[10]: https://www.ibiblio.org/apollo/hrst/archive/1033.pdf "AGC Restart System Design {}"
[11]: https://en.wikipedia.org/wiki/Cycle_stealing "Description of Cycle Stealing {}"
[12]: https://www.ibiblio.org/apollo/yaAGS.html "Description of AGS {}"
[13]: https://www.ibiblio.org/apollo/LVDC.html "Description of LVDC {}"
[14]: https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips "AGC and the First Si Chips {}"
[15]: https://youtu.be/wSSmNUl9Snw "Video describing Apollo 14 fix {}"
[16]: https://youtu.be/cPxaGrcimMQ?t=612 "AGC Restoration {}"
[17]: https://youtu.be/fjAeBJrsj5Q "CG Simulation of Apollo CSM and DSKY during re-entry {}"
[18]: https://en.wikipedia.org/wiki/Rigid_body_dynamics#Rotation_in_three_dimensions "Rotation Dynamics of a Rigid Body {}"
[19]: http://farside.ph.utexas.edu/teaching/336k/Newtonhtml/node61.html "Rigid Body Rotation {}"
[20]: https://youtu.be/BPMjcN-sBJ4 "Demonstration of Free Body Rotation in Micro-Gravity {}"

<!---
Image source info

https://en.wikipedia.org/wiki/Apollo_Guidance_Computer#/media/File:Dsky.jpg

https://wehackthemoon.com/bios/jack-garman - indicates image is courtesy of NASA cheat sheet

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


