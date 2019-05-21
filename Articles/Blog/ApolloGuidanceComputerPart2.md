# Celebrating Apollo's 50th Anniversary: The Oldest Code on GitHub

**Hero Image:**

- <img src='https://raw.githubusercontent.com/betterscientificsoftware/images/Blog_AGCPart2_MargaretHamilton.png' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June, 2019

*Second of a three-part series to commemorate the 50th anniversary of the Moon landings.*

Retro-computing enthusiasts recently uploaded AGC source code for various Apollo
missions to GitHub. There is even a *Virtual AGC* that can run this code. In all
likelihood, it is the oldest *active* code on GitHub. Remarkably, its development
began over half a century ago in the ashes of a guidance software disaster.

The loss of radar contact triggered a bug in the guidance software of Mariner 1 and
led to its destruction shortly after launch. Accounts vary but one explanation<sup>[20]</sup>
was that the bug had been introduced in the transcription of hand-written guidance equations
into a software specification for the contractor. An over-bar to indicate the use
of *average* rather than *instantaneous* velocity went missing. The contractor had
implemented the guidance software to specification. The specification was wrong.
The same bug had flown on two earlier Ranger missions but loss of radar necessary
to trigger it never occurred.

That failure remained a painful reminder to one software engineer in particular,
John Norton, a guidance software expert at TRW who was partly responsible for Mariner 1
and was later hired by NASA to review AGC code for quality. He dedicated himself to
becoming a human static analyzer, often manually reverse engineering AGC code he was
asked to review to reveal the equations it had been programmed to solve.

# Background 

(Put this at end)
The whole GNC system for all Apollo missions cost ~$600 million<sup>[24]</sup> ($5
billion in 2019 dollars) total spread over 10 years. The software effort alone was
about 10% of that or ~$60 million<sup>[23]</sup> ($0.5 Billion in 2019 dollars) the
majority of it occurring over the last 5 years with a peak of 350 FTEs.

> Before the first lunar landing, more than 1400 man-years of software engineering effort
> had been expended, with a peak manpower level of 350 engineers reached in 1968.

By comparison, the Exascale Computing Project 2020 budget is projected to
be $809 Million including hardware and software.

Project | 1965 $$$ | 2019 $$$ | Publications & Theses 
---|---|---|---
Apollo GNC Total | $600M | $5B | XXX
Apollo GNC Software | $60M | $0.5B | XXX
ECP Total | | |
ECP Software | | |

# Co-Design in the Extreme
When development of the Apollo GN&C system began, very few specific requirements were
known. The specific steps involved a fligh to the Moon and the vehicle(s) to be used
were total unknowns.

> "NASA had established a need for the machine and had determined its general tasks, and
> MIT received a contract based on only a short, very general requirements statement.
> Requirements started changing immediately and continued to change throughout the program."

MIT knew guidance would need to be accurate to 1 part in 100,000 and a digital rather than
analog computer would be required.

The AGC would be the centerpiece controlling a complex collection of sensors, controllers,
cockpit displays, thusters and engines. A big challenge facing software developers was that
all of these components were under development almost simultaneously. Their interfaces,
performance characteristics, size, weight,
and position within the spacecraft, all of which effect things like center of mass, angles,
moments and torques were constantly evolving. In addition, NASA's expectations for what functions
the GN&C system should perform were also evolving motiviated by a desire for increased safety
margins, mission flexibility and optimizing propellent usage.

It would be more than a year *after* MIT had been contracted to develop Apollo's GN&C system
that NASA selected the Lunar Orbit Rendevouse (LOR) mode involving two separately
piloted vehicles, the Command/Service Module (CSM) and the Lunar Module. Each would need its
own AGC controlling a wholly different spacecraft with a wholly different configuration of guidance
related hardware.

To meet, size, weight and power reqirements, MIT knew the
AGC would need to use *integrated circuits*, a then fledging technology with numerous
manufacturing challenges. Methods for testing and
screening chips for quality assurance and reliability needed to be developed. Memory capacity
needed to be determined. Initial estimates of 4K were revised in
official design documents no less than 4 times until the final number of 38K was settled
upon. An assembler needed to be written. Astronaut user interfaces needed to be invented
(you can't operate the then standard keyboards wearing a spacesuite glove).

Four different tiers of testing processes would eventually
need to be developed; an all-digital AGC simulator, a hybrid simulator using an actual AGC but
simulated spacecraft systems, system test labs and XXX. The hardware and sofware supporting
these testing resources needed to be developed. Operators needed to be trained in the use of
these test facilities. Methods for rapid but accurate manufacture of rope core memory needed to
be developed. Processes for managing and exercising quality control of the whole development
effort needed to be created. Naturally, NASA applied tried and true management processes for
hardware to software. Finding and hiring people to do all the work.
Testing plans and resources needed to be developed too. Ultimately, four different types of testing
systems were developed; all-digital, hybrid, system test labs, integration tests and crew rehersals
with flight-ready articles. But, the hardware and software supporting these systems was being developed
right along with the guidance system it was being developed to support. The all-digital testing system
was a 10% speed all-digital simulation of an AGC originally written for a Honeywell 800 using MAC
(MIT Algebraic Compiler) language and later ported to H-1800 and IBM 360/75 systems

The all-digital simulation of the AGC for testing would eventually require
MIT to purchase one Honeywell 800, 2 Honeywell-1800s and 2 IBM 360/75 peaking at about
4,500 cpu hours/month (equiv. H-1800 cpu) testing soley for the all-digital testing simulator per month.

While NASA and its contractors had a lot of experience managing complex hardware development
projects, no one had experience with a massive software development effort. Development
process and methods for managing them were being developed right along with the actual
work.
Neither NASA nor MIT had any experience managing large software projects. They had plenty with
hardware. As issues developing the software mounted, the decision was made to impose
hardware-like development processes and oversight.


Early on, the focus was on developing the AGC hardware. By 1964, requirements were
clear enough and enough new ones had been added that it became clear a re-design
of the AGC to support more memory would be required. Thus, AGC developers were
then required to support two different systems; Block I and Block II.

Two separate AGC models were produced and supported. The two machines were different enough that
each required separate software development teams.

Attribute | Block I (fall 1962) | Block II (summer 1966) 
---|---|---
Fixed/Eraseable Memory (k-words) | 24 / 1 | 36 / 2
Logic #ICs (NOR gates/IC) | 4,100 (x1) | 2,800 (x2)
Clock / Instructions | 1.024 Mhz / 11 | 1.024 Mhz / 34
Power/Weight | 85W / 39.5kg | 55W / 31.9kg
Flops (kF) | 7.1 | 14.5

The AGC Block II had only 2K words (a word was 16 bits) of read-write core and 36K words of
read-only core (called *fixed memory* or *rope core*). All software and data for a
particular Apollo mission had to fit into this combined 76KB of memory. The AGC did
not support floating point. Instead, like a *slide rule*<sup>[22]</sup>, it used a
*fractional* representation where the *exponent* was managed implicitly. Developers
simply agreed on the implied scaling of any particular numerical values as well as
occasionally explicitly re-scaling as needed to maintain precision.

These early years of software development are best described in today's jargon as co-design
but in the extreme. A 1962 memo<sup>[25]</sup> lists no less than 45 separate major software
analysis efforts underway, the first step in developing a major program in the AGC was to
understand the equations governing spaceflight and outline computational approaches utilizing
available sensors and controls to affect control in specified time and space (memory) requirements.

# The AGC Software Stack
Early development activity, 1961-1965 focused on infrastructure software...

**Program Name** | **Purpose** | **Size (AGC words)**
:--- | :---: | ---:
Executive | Priority driven large/long-running program manager | ~350
Waitlist | Time sequenced small/short-running program manager | ~300
Interpreter | Space guidance domain specific language | ~2200
DSKY I/O | Cockpit Displays and keyboard | ~3500
**Combined Total** | %18 of fixed memory | **~6350**

These programs largely comprised what we would know today as the AGC *operating system*.
All were written in AGC assembly language.  By 1965, most of this code had been
written and fully tested. And, it represented only a tiny fraction of the whole software
development effort to come.

# Mission Software

Moon/Sun Ephemeris Subroutine: ~90 words (Interpretive code)

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

# Digital Feedback Control System: Kalman Fitlers

DAP decision

systems. The whole system forms a complex feedback control system
the stability<sup>[1]</sup> of which is an essential characteristic. Early on in the software development,
the problem was to understand the equations governing spaceflight certain mission objectives
and then develop approaches utilizing available sensors and controls to affect responses in real-time.

Three key things impacted AGC software development more than any other. The first was the
decision to implement a digital auto-pilot (DAP). The second was the design of the memory
sub-system. The third was the 1967 fire of Apollo 1.

# Apollo Mission Worklow: The AGC had an App for That
Flying to the moon and returning safely involved a lot of coasting. A mission was divided into
phases by *velocity changes*. For each manuever, there was a cooresponding program to handle it.
In addition, time crtical maneuvers such as lunar landing, rendevouse and docking and re-entry
required special groups of programs working together. For every phase of the mission, there was
an *app* for that. But, whole programs utilized smaller sub-routines that performed highly
specialized operations.


A lunar mission was divided into phases by *velocity change manuevers*. For each manuever,
*there was an app for that*; there was a cooresponding program in the AGC to manage the
manuever. For time crtical maneuvers such as lunar landing, rendevouse & docking and
re-entry, several programs worked in sequence.

For any particular maneuver, factors impacting program development were considerable.
They included zero gravity fuel slosh, changing center of mass due to fuel consumption,
main engine throttle and gimbal characteristics, sensor drift and measurement
biases and uncertainties, avoiding IMU gimbal lock, optimizing use of RCS
propellants, contingency logic for failed (on or off) RCS thrusters, positions of Sun,
Earth and Moon (all in constant motion) as well as their *lumpy*<sup>[3],[4]</sup>
gravity fields, narrow windows of opportunity as lines of sight to ground communication
stations varied.

of spacecraft position and position rates (e.g. *velocity*), orientation (e.g. roll, pitch and
yaw) and orientation rates (*rotational velocity*). This is the *state vector*. The inertial
measurement unit (IMU), is the critical sensor system responsible for measuring linear and
angular accelerations the spacecraft experiences. Integration of the accleration data is
required to obtain velocity and position data.

# Testing

Norton

### From Computers in Spaceflight: The NASA Experience
> The need for formal validation rose with the size of the 
> software. Programs of 2,000 instructions took between 50 and 100 test 
> runs to be fully debugged, and full-size mission loads took from 1,000 
> to 1,200 runs ^12 

> There 
> always seem to be enough deficiencies in a final product that the 
> designers wish they had a second chance. 






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

[1]: https://en.wikipedia.org/wiki/Control_theory#Stability "Stability in Control Theory {}"
[2]: https://www.ibiblio.org/apollo/Documents/SGA_Memo11_620716.pdf "Software Development Activities Summary Memo 1962 {}"
[3]: https://en.wikipedia.org/wiki/Gravity_of_Earth "Earth's Lumpy Gravity Field {}"
[4]: https://en.wikipedia.org/wiki/Gravitation_of_the_Moon "Moon's Lumpy Gravity Field {}"
[5]: https://www.americanscientist.org/article/moonshot-computing "Great Article on AGC Software {}"
[6]:http://www.klabs.org/history/apollo_11_alarms/eyles_2004/eyles_2004.htm "Tales from Lunar Landing {}"
[7]: https://www.mathworks.com/company/newsletters/articles/fly-me-to-the-moon-then-and-now.html "DAP Design Then and Now with MathWorks {}"
[8]: https://www.ibiblio.org/apollo/index.html "Virtual AGC Project Home Page {}"
[9]: https://www.researchgate.net/publication/228517819_Architectural_Simulation_for_Exascale_HardwareSoftware_Co-design "Architectural Simulation for ExascaleHardware/Software Co-design {Janssen, Curtis & Quinlan, Dan & Shalf, John. (2019). Architectural Simulation for Exascale Hardware/Software Co-design.}"
[10]: https://www.design-reuse.com/articles/31951/the-power-of-developing-hardware-and-software-in-parallel.html "The Power of Developing Hardware and Software in Parallel {}"
[12]: http://web.mit.edu/digitalapollo/Documents/Chapter6/hoagprogreport.pdf?#page=24 "Hoag Report including DAP Design and Performance {}"
[13]: https://www.mathworks.com/help/simulink/slref/developing-the-apollo-lunar-module-digital-autopilot.html "Simulink Model of DAP {}"
[14]: http://thecomputerboys.com "Early Programmers as Data Entry Personnel - Women's Work {}"
[15]: http://www.ibiblio.org/apollo/hrst/archive/1695.pdf "AGC Software Development Plan {}"
[16]: http://klabs.org/history/history_docs/mit_docs/1711.pdf?#page=12 "Hoag Report: THE HISTORY OF APOLLO ON-BOARD GUIDANCE, NAVIGATION, AND CONTROL {}"
[17]: http://tindallgrams.net "Select Tindall-grams {}"
[18]: https://www.ibiblio.org/apollo/hrst/archive/1687.pdf?#page=40 "Example AGC Interpretive Program To Find Quadratic Roots {}"
[19]: https://history.nasa.gov/computers/Ch2-6.html "Great Overview of Software Development Issues"
[20]: https://www.airspacemag.com/space/practicing-safe-software-180962744/ "Air & Space Article on Mariner 1 {}"
[21]: https://authors.library.caltech.edu/5456/1/hrst.mit.edu/hrs/apollo/public/conference1/hamilton-intro.htm "Interview with Margaret Hamilton {}"
[22]: https://en.wikipedia.org/wiki/Slide_rule "Slide Rule {}"
[23]: https://www.ibiblio.org/apollo/hrst/archive/1728.pdf "AGC Software Development Productivity and Costs {Rankin, DA. (1972) A Model of the Cost of Software Development for the Apollo Spacecraft Computer, Masters Thesis, MIT}"
[24]: https://history.nasa.gov/SP-4029/Apollo_18-16_Apollo_Program_Budget_Appropriations.htm "Apollo Budget By Sub-Program and Year {}"
[25]: https://www.ibiblio.org/apollo/Documents/SGA_Memo11_620716.pdf "List of Software Studies Underway in 1962 {}"

Numerics of Apollo Guidance System

- IMU degredation signature
- eraseable programs
- filter coefficients and instability
- ALU number representations
- scaling among subroutines
- moon position data
- Apollo mission accruacy needs
- 3 or 4 gimbals

Analysis/Development
    equations of motion
    feedback control system
    Kalman filtering
MAC prototype first
Documentation?
Debugging
   - eraseable programs
   - trace/dump
   - more on hybrid sim.
Testing
   - 4 tiers
   - unit and gradual larger components
   - test plans
Management and Organization

Norton-izing and PRs (Thats Peer Reviews not Pull Requests).

People:
    Norton
    Hamilton & her daughter
    Tindall
    Kalman
    "Computers" (women)

Possible framing concepts
   - context
   - testing and debugging
   - co-design (a lot of changes at once)
   - workflow (flight programs)
   - numerics

   - application vs. infrastruction like I/O
   - GUI/Visualization
   - ecosystem or stack
   - restart
   - memory management
   - "communication", people style (a lot of meetings)
   - project organization and management
   - productive output of "journal" publications

Say something about the Russion program, 3-way redundant computer
