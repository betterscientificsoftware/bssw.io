# The Oldest Code on GitHub
## Part 2 of 3: The Apollo Guidance Computer Software

**Hero Image:**

- <img src='https://raw.githubusercontent.com/betterscientificsoftware/images/Blog_AGCPart2_MargaretHamilton.png' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June, 2019

*Part two of three about the Apollo Guidance Computer commemorating the 50th anniversary of the Moon landing.*

Retro-computing enthusiasts recently uploaded AGC source code for various Apollo missions to
GitHub<sup>[7]</sup>. The code even compiles and runs on the *Virtual AGC*<sup>[8]</sup>. In all
likelihood, it is the oldest *maintained* code on GitHub. Ironically, its development began
over half a century earlier in the ashes of a guidance software disaster. The loss of radar
contact combined with a bug in the backup guidance software of Mariner 1 led to its destruction
only 294 seconds after launch. Investigations revealed that during the transcription of hand-written
guidance equations onto computer punch cards, an over-bar to indicate the use of *average* rather
than *instantaneous* velocity went missing. The same bug was found to have flown, undiscovered,
on two earlier Ranger missions. So much of the initial focus was on developing the AGC hardware
that no one involved at the time had any clue about the monumental software development task that lay
ahead. Developing software for the AGC eventually became the rate-determining factor in delivering
flight ready units.

Flying to the moon and returning safely involved a lot of coasting. A mission was divided into
phases by *velocity changes*. For each velocity change, there was a cooresponding *app* in the
AGC to manage the maneuver. As an example, consider the lunar orbit insertion manuever. In this
phase of the mission, the spacecraft is arriving at and preparing to go into orbit around the
moon. It is approximately 90 miles from the surface moving at 1.625 miles/second. 


Three key things impacted AGC software development more than any other. The first was the
decision to implement a digital auto-pilot (DAP). The second was memory first small then
larger. The third was the 1967 fire of Apollo 1.


## GNC System Architecture

The AGC and its software was only the central component of an integrated collection of sensors,
displays, controls and propulsion systems. The whole system forms a complex feedback control system
the stability<sup>[1]</sup> of which is an essential characteristic. Early on in the software development,
the problem was to understand the equations governing spacecraft motions for certain mission objectives
and then develop approaches utilizing available sensors and controls to affect responses in real-time.

A big challenge facing software developers was that all of these components were under
development almost simultaneously. Their interfaces, performance characteristics, size, weight,
and position within the spacecraft, all of which effects things like center of mass, angles,
moments and torques were constantly evolving. In addition, NASA's expectations for what functions
the GN&C system should perform were also evolving motiviated by a desire for increased safety
margins and optimizing propellent usage.


## Where's the Moon?

https://en.wikipedia.org/wiki/Orbit_of_the_Moon

Knowing accurately the position of the Moon as a function of time over a two-week period
representing the longest possible mission is a typical example of the kind of problems AGC
software developers needed to solve. In addition, doing so with a minimum of fixed and/or
eraseable storage and without consuming too much of the CPU's attention or taking longer
than needed in order to operate in real-time were all design considerations in developing
the code. 

A typical example of the kind of problems AGC software developers needed to solve is the Moon
position problem. That is 

ensuring the
AGC knows the correct position of the Moon with high accuracy at all times and how to do so
using a minimum of storage.

## CI, 1960's Style

Testing resources strained to the limit

## Performance Portabiity, 1960's Style

## Auto-documentation, 1960's Style


MIT Algebraic Compiler language
Used a three line format as suggested by R H Battin 1956 for a 2-dimensional input (the program needed three cards per line
Could do vectors, matrices, ordinary differential equations. True compiler of 650 machine code

What are the highlights?
Any interesting aspects?
A day in the life?

[1]: https://en.wikipedia.org/wiki/Control_theory#Stability
