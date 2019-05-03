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
on two earlier Ranger missions.

## AGC Architecture and Peripherals

The AGC had unique *periperhals* not at all similar to our external displays, usb drives or
wireless mice.

## Management of a Big Software Project

So much of the initial focus was on developing the AGC hardware
that no one involved at the time had any clue about the monumental software development task that lay
ahead. Developing software for the AGC eventually became the rate-determining factor in delivering
flight ready units.

## Digital Auto Pilots (DAPs)

## Testing 


# Hardware Approach to Software

Neither NASA nor MIT had any experience managing large software projects. They had plenty with
hardware. As issues developing the software mounted, the decision was made to impose
hardware-like development processes and oversight.

Flying to the moon and returning safely involved a lot of coasting. A mission was divided into
phases by *velocity changes*. For each manuever, there was a cooresponding program to handle it.
In addition, time crtical maneuvers such as lunar landing, rendevouse and docking and re-entry
required special groups of programs working together. For every phase of the mission, there was
an *app* for that. But, whole programs utilized smaller sub-routines that performed highly
specialized operations.

Computing the position of the Moon as a function of time is a typical example of the kind of
problem AGC software developers faced. Doing so using a minimum of fixed and
eraseable storage and without consuming too much of the CPU's attention or taking longer than
needed for real-time operation were all design considerations in developing AGC software. 
In this case, after developing and evaluating various methods in MAC Fortran on MIT
mainframe systems, developers settled on an approach using 3, 8th degree polynomial
fits to positional data predicted from separate and independent solution of the 3-body
(Earth, Sun, Moon) problem. The polynomial coefficents fitting a 2-week period of Moon
position data at the anticipated time of the mission were then computed and stored in
fixed memory (rope core). This data would be among the approximately 70 kilobytes of data
hand woven into the rope core in the weeks before a mission.

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


## CI, 1960's Style

Testing resources strained to the limit

## Performance Portabiity, 1960's Style

One piece of code to provide *optimal* control over two radically different spacecraft.
Although the computing hardware was identical, the propulsion and sensor systems they
interfaced with and the spacecraft themselves were radically different.

What if thinking?

performance in two different computing enviornments.
Sound familiar? Developing the Apollo Digital Autopilot (DAP) represented a significant
performance portability challenge for 1960's era developers. Although the AGC in both

 Though the computer itself


two identical computers embedded in dramatically different spacecraft

## Auto-documentation, 1960's Style


MIT Algebraic Compiler language
Used a three line format as suggested by R H Battin 1956 for a 2-dimensional input (the program needed three cards per line
Could do vectors, matrices, ordinary differential equations. True compiler of 650 machine code

What are the highlights?
Any interesting aspects?
A day in the life?

[1]: https://en.wikipedia.org/wiki/Control_theory#Stability
[2]: https://www.ibiblio.org/apollo/Documents/SGA_Memo11_620716.pdf "Software Development Activities Summary Memo 1962"

http://www.klabs.org/history/apollo_11_alarms/eyles_2004/eyles_2004.htm "Tales from Lunar Landing"

https://www.mathworks.com/company/newsletters/articles/fly-me-to-the-moon-then-and-now.html "DAP Design Then and Now with MathWorks"

http://web.mit.edu/digitalapollo/Documents/Chapter6/hoagprogreport.pdf?#page=24 "Hoag Report including DAP Design and Performance"

https://www.mathworks.com/help/simulink/slref/developing-the-apollo-lunar-module-digital-autopilot.html "Simulink Model of DAP"

http://thecomputerboys.com "Early Programmers as Data Entry Personnel"

http://www.ibiblio.org/apollo/hrst/archive/1695.pdf "AGC Software Development Plan"
