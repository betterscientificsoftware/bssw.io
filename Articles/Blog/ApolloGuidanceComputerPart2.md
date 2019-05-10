# Celebrating Apollo's 50th Anniversary: The Oldest Code on GitHub

**Hero Image:**

- <img src='https://raw.githubusercontent.com/betterscientificsoftware/images/Blog_AGCPart2_MargaretHamilton.png' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June, 2019

*Second of a three-part series to commemorate the 50th anniversary of the Moon landings.*

Retro-computing enthusiasts recently uploaded AGC source code for various Apollo missions to
GitHub<sup>[7]</sup>. There is even a *Virtual AGC*<sup>[8]</sup> that executes this code.
In all likelihood, it is the oldest *maintained* code on GitHub. Ironically, its development
began over half a century earlier in the ashes of a guidance software disaster. The loss of a
radar signal combined with a bug in the guidance software of Mariner 1 led to its destruction
shortly after launch. Investigations revealed that during the transcription of hand-written
guidance equations onto computer punch cards, an over-bar to indicate the use of *average*
rather than *instantaneous* velocity went missing. The same bug had flown on two earlier
Ranger missions but loss of radar necessary to trigger it never occurred.

A lunar mission was divided into phases by *velocity change manuevers*. For each manuever,
*there was an app for that*. There was a cooresponding program in the AGC. For time crtical
maneuvers such as lunar landing, rendevouse and docking and re-entry several programs worked
together.

For any particular maneuver, the set of considerations impacting program design and
development were enormous. They included fuel slosh, changing center of mass due to
fuel consumption, main engine throttle and gimbal response times and limits,
sensor drift and measurement uncertainty, avoiding gimbal lock, optimizing use of RCS
propellants, contingency logic for failed (on or off) thrusters, gravity of Sun,
Earth and Moon (all in constant motion) as well as their *lumpy*<sup>[3],[4]</sup>
gravity fields, narrow windows of opportunity as lines of sight to ground communication
stations varied.

In the AGC, there was no drum, tape or disk for secondary storage. There was 2K words of
read-write core mainly for temporary storage and 36K words of read only core (also called
*fixed* or *rope*) core. All programs and data needed to fit into this available memory.

Early development activity, 1961-1965 focused on infrastructure software...

**Program Name** | **Purpose** | **Size (AGC words)**
:--- | :---: | ---:
Executive | Priority driven large/long-running program manager | ~350
Waitlist | Time sequenced small/short-running program manager | ~300
Interpreter | Space guidance domain specific language | ~2200
DSKY I/O | Cockpit Displays and keyboard | ~3500
**Combined Total** | --- | **~6350**

words) all of which were written in AGC assembly language. These programs largely comprised
what we would know today as the AGC *operating system*. By 1965, most of this code had been
written and fully tested. And, it represented only a tiny fraction of the whole software
development effort to come.


Moon/Sun Ephemeris Subroutine: ~200 words (Interpretive code)

The first step in developing these guidance routines was to understand the equations governing
spacecraft motion during certain maneuver objectives and then develop approaches utilizing available
sensors and controls to affect responses within in various constraints such as time, memory, 
fuel usage, propulsive device response characteristics. The complexities were enormous; sensor
drift / failed sensors, failed thrusters, avoiding gimbal lock, the moon’s lumpy gravity field,
fuel slosh, changing center of mass, optimizing use of RCS fuel Narrow windows of opportunity
Maximize safety margins Software errors Human errors (check lists) Communication lapses and blackouts
Allowing for failures & contingencies

A good example of the kind of problem AGC developers needed to solve was finding a way for the AGC
to know the position of the Moon as a function of time. Doing so using a minimum of fixed and
eraseable storage and without consuming too much of the CPU's attention or taking longer than
needed for real-time operation were all design considerations in developing AGC software. 
In this case, after developing and evaluating various methods in MAC Fortran on MIT
mainframe systems, developers settled on an approach using 8th degree polynomial fits to
X, Y and Z positional data predicted from separate and independent solution of the 3-body
(Earth, Sun, Moon) problem. The polynomial coefficents fitting a 2-week period of Moon
position data at the planned time of the mission were then computed and stored in
fixed memory (rope core). This data would be among the approximately 70 kilobytes of data
hand woven into the rope core in the weeks before a mission.






## Maintaining Knowledge of the State Vector At All Times

A critical problem the AGC needed to solve was maintaining accurate knowledge at all times
of spacecraft position and position rates (e.g. *velocity*), orientation (e.g. roll, pitch and
yaw) and orientation rates (*rotational velocity*). This is the *state vector*. The inertial
measurement unit (IMU), is the critical sensor system responsible for measuring linear and
angular accelerations the spacecraft experiences. Integration of the accleration data is
required to obtain velocity and position data.


## Hypothetical Hardware and Revising Requirements 

As crtical as the AGC and its software was, it was only one part of an integrated
collection of guidance hardware
system of displays, controllers, sensors and 

The AGC and its software was only the central component of a larger system. A collection of
sensors, displays, controls and propulsive devices

systems. The whole system forms a complex feedback control system
the stability<sup>[1]</sup> of which is an essential characteristic. Early on in the software development,
the problem was to understand the equations governing spaceflight certain mission objectives
and then develop approaches utilizing available sensors and controls to affect responses in real-time.

A big challenge facing software developers was that all of these components were under
development almost simultaneously. Their interfaces, performance characteristics, size, weight,
and position within the spacecraft, all of which effect things like center of mass, angles,
moments and torques were constantly evolving. In addition, NASA's expectations for what functions
the GN&C system should perform were also evolving motiviated by a desire for increased safety
margins and optimizing propellent usage.

Three key things impacted AGC software development more than any other. The first was the
decision to implement a digital auto-pilot (DAP). The second was the design of the memory
sub-system. The third was the 1967 fire of Apollo 1.


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

[3]: https://en.wikipedia.org/wiki/Gravity_of_Earth "Earth's Lumpy Gravity Field"
[4]: https://en.wikipedia.org/wiki/Gravitation_of_the_Moon "Moon's Lumpy Gravity Field"
[5]: https://www.americanscientist.org/article/moonshot-computing "Great Article on AGC Software"

http://www.klabs.org/history/apollo_11_alarms/eyles_2004/eyles_2004.htm "Tales from Lunar Landing"

https://www.mathworks.com/company/newsletters/articles/fly-me-to-the-moon-then-and-now.html "DAP Design Then and Now with MathWorks"

http://web.mit.edu/digitalapollo/Documents/Chapter6/hoagprogreport.pdf?#page=24 "Hoag Report including DAP Design and Performance"

https://www.mathworks.com/help/simulink/slref/developing-the-apollo-lunar-module-digital-autopilot.html "Simulink Model of DAP"

http://thecomputerboys.com "Early Programmers as Data Entry Personnel - Women's Work"

http://www.ibiblio.org/apollo/hrst/archive/1695.pdf "AGC Software Development Plan"

http://klabs.org/history/history_docs/mit_docs/1711.pdf?#page=12 "Hoag Report: THE HISTORY OF APOLLO ON-BOARD GUIDANCE, NAVIGATION, AND CONTROL"

http://tindallgrams.net "Select Tindall memos"

https://www.ibiblio.org/apollo/hrst/archive/1687.pdf?#page=40 "Example AGC Interpretive Program"

Numerics of Apollo Guidance System

- IMU degredation signature
- eraseable programs
- filter coefficients and instability
- ALU number representations
- scaling among subroutines
- moon position data
- Apollo mission accruacy needs
- 3 or 4 gimbals
