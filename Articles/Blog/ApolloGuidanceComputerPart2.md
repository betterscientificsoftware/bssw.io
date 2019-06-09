# Celebrating Apollo's 50th Anniversary: The Oldest Code on GitHub

**Hero Image:**

![AGC Major Software Releases](manloading_on_releases.png)

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June, 2019

*Second of a three-part series to commemorate the 50th anniversary of the Moon landings.*

Retro-computing enthusiasts recently uploaded Apollo Guidance Computer (AGC)
source code for various Apollo missions to GitHub. There is even a *Virtual AGC*
that can run this code. In all likelihood, it is the oldest *active* code on
GitHub. Remarkably, its development began over half a century ago in the ashes
of Mariner 1, a Venus probe destroyed shortly after launch due to a bug in its
guidance software. The prevailing explanation was that in the
transcription of hand-written guidance equations into a software specification
for the contractor, TRW, an over-bar to indicate the use of *average* rather than
*instantaneous* velocity went missing;<sup>[20]</sup> along with it, an $18M
probe ($152M in 2019 dollars) and a regrettable ration of American prestige.
How would MIT and NASA avoid similar mistakes developing software for the AGC?

This is the second of three articles about the AGC. In part 1, we described the
hardware.<sup>[26]</sup> Here, in part 2, we focus on MIT's effort to develop
the software. As much information as there is available regarding the AGC, it
is difficult to find details about specific development processes used.
Nonetheless, as in part 1, the scientific computing community will recognize
some familiar themes such as the necessity of *co-design*, the importance of
sufficient testing resources, the role and impact of software process
improvements and more.

# Extreme Co-Design
Initially, about all that was known with any certainty was that a digital
computer would be the centerpiece of a complex collection of GN&C sub-systems.
More than year would pass before NASA finaly selected the Lunar Orbit
Rendevious (LOR) mission plan involving two separately piloted and radically
different vehicles each with its own AGC controlling a substantially different
configuration of GN&C sub-systems. These would be the first digitally controlled,
fly-by-wire vehicles ever created. At the heart of it all, AGC software would
control everything. Even so called *manually controlled* inputs would first
pass through AGC software before affecting the relevant hardware. 

![](agc_and_spacecraft3.png)

A challenge in developing the software is that all the sub-systems
it must interact with and control were under development *simultaneously*
right along with the software itself. Their interfaces, performance
characteristics, size, weight and position within the spacecraft, all of
which effect key parameters in guidance equations were constantly evolving.
Apart from the sub-systems and their integration, a 1962 memo<sup>[25]</sup>
lists no less than 45 major software analysis efforts then underway for
various aspects of an Apollo mission to the moon.

Another challenge was testing. How is the software's
ability to properly utilize and control all these sub-systems tested
without actually flying the vehicle in real-word conditions?
Ultimately, several different test simulators would be developed.
Simulator hardware and software as well as the test plans and methods for
collecting and analyzing test results were being developed right along with
the software it was intended to test. Even techniques to manage the
software effort were effectively under development and evolving with the
software. Eventually, NASA would pressure MIT to adopt techniques pioneered
by IBM to help manage large software development projects.

Today, we would call all of this simultaneous development activity
*co-design*<sup>[31]</sup> and it has a lot of advantages.
But, in the 1960's where there were no dev-ops best practices and collaborative tools
like GitLab, Jenkins, Confluence, Kanban, WebEx, or even Email, it presented a massive
coordination and management challenge.

# Evolving Requiremens, Versions and Releases
Throughout the early phases of development, NASA's expectations for what functions
the GN&C system would perform, and therefore the AGC software, continued to evolve
motivated by a desire to reduce weight, increase safety margins, improve mission
flexibility and optimize propellent usage.

> NASA had established a need for the machine and had determined its general tasks, and
> MIT received a contract based on only a short, very general requirements statement.
> Requirements started changing immediately and continued to change throughout the program.

Midway through development, the AGC was re-desinged to support more memory and an expanded
instruction set. Software developers had to support both the old, Block I, and new, Block II
hardware. Block I would be used on early, uncrewed Apollo test flights and Block II on crewed
flights. They were different enough that each required separate software development teams.
This only exacerebated already strained software development and management burdens.

Attribute | Block I (fall 1962) | Block II (summer 1966) 
---|---|---
Fixed/Eraseable Memory (k-words) | 24 / 1 | 36 / 2
Logic #ICs (NOR gates/IC) | 4,100 (x1) | 2,800 (x2)
Clock / Instructions | 1.024 Mhz / 11 | 1.024 Mhz / 34
Power/Weight | 85W / 39.5kg | 55W / 31.9kg
Flops (kF) | 7.1 | 14.5

Neither Block I or Block II supported floating point. Instead, like a *slide rule*,<sup>[22]</sup>
the AGC used single-, double- or triple-precision *fractional* representation where the
*exponent* was managed implicitly. Developers simply agreed on the implied scaling of any
particular numerical value as well as occasionally coding explicit re-scaling as needed to
maintain precision. Block II had only 2K words of *erasable* core and 36K words of *fixed*
or *rope core* memory. All software and data had to fit into this combined 76KB of memory.

**The essential step for MIT software developers was to produce a *flight program* or *rope*
and release it to Raytheon for rope core manufacture approximately 4 months prior to launch;
2 months to manufacture the ropes followed by 2 months for installation in the spacecraft,
checkout, testing and crew rehersals.**

A *rope mother* would be the lead engineer in coordinating all the software that went into
a particular flight program and would also have the honor of giving the program release its
name. Early on the names were fairly creative including ECLIPSE, SUNRISE, RETREAD, AURORA.
Eventually, only the names COLUSSUS and LUMINARY together with revision numbers of each would
be used to identify CM and LM AGC flight programs<sup>[34]</sup>. Each flight program involved
a combination of common, utility modules as well as those that were highly mission specific.
The mission specific components required significant analysis and development time.

# The AGC Software Stack
![](./agc_sw_stack.png)

Early development activity, 1961-1965, focused on infrastructure software. This
included fuctions we would call today such as the operating system, I/O

**Program Name** | **Purpose** | **Size (AGC words)**
:--- | :--- | ---:
Executive | Priority driven large/long-running process manager | ~350
Waitlist | Time sequenced small/short-running process manager | ~300
Interpreter | Space guidance domain specific progamming language interpreter | ~2200
DSKY I/O | Cockpit Displays and Keypad | ~3500
**Combined Total** | %18 of fixed memory | **~6350**

These programs largely comprised what we would know today as the AGC *operating system*.
All were written in AGC assembly language.  By 1965, most of this code had been
written and fully tested. And, it represented only a tiny fraction of the whole software
development effort to come.

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

star list, space sextant

# Testing
an all-digital simulator of the AGC as well as associated spacecraft GN&C sub-systems,
a hybrid simulator using a real AGC but with simulated spacecraft GN&C sub-systems,
a test-lab simulator using a real AGC with some real and some simulated spacecraft
sub-systems. The final level of testing involved actual spacecraft checkouts, crew
rehersals with flight-ready artiles and *in-flight* testing of the AGC in the
real spacecraft as part of various of early Apollo missions.
The all-digital testing system

was a 10% speed all-digital simulation of an AGC originally written for a Honeywell 800 using MAC
(MIT Algebraic Compiler) language and later ported to H-1800 and IBM 360/75 systems
The all-digital simulation of the AGC for testing would eventually require
MIT to purchase one Honeywell 800, 2 Honeywell-1800s and 2 IBM 360/75 peaking at about
4,500 cpu hours/month (equiv. H-1800 cpu) testing soley for the all-digital testing simulator per month.
Four different tiers of testing processes would eventually
need to be developed; an all-digital AGC simulator, a hybrid simulator using an actual AGC but
simulated spacecraft systems, system test labs and XXX. The hardware and sofware supporting
these testing resources needed to be developed. Operators needed to be trained in the use of
these test facilities. Methods for rapid but accurate manufacture of rope core memory needed to
be developed. Processes for managing and exercising quality control of the whole development
effort needed to be created. Naturally, NASA applied tried and true management processes for
hardware to software. Finding and hiring people to do all the work.


# Nortonizing: Manual Static Analysis
The failure of Mariner 1 was a painful experience for one NASA team member in particular;
John Norton. Norton was a guidance software expert at TRW and was partly responsible for
the Mariner 1 software failure. Remarkably, he was later hired by NASA to perform
independent peer review of the code MIT was producing.

That failure remained a painful reminder to one software engineer in particular,
John Norton, a guidance software expert at TRW who was partly responsible for
Mariner 1 and later hired by NASA to review AGC software for quality.
He dedicated himself to becoming a human static analyzer, frequently manually reverse
engineering AGC code he was asked to review to reveal the equations it had been programmed
to solve. Early on, he discovered multiple instances of the use of 22/7 as an approximation
for pie. failures in units conversions


Norton developed a way of expressing AGC assembly code in a human readable form he called
*Programmed Equations*.<sup>[32]</sup> He would then manually reverse engineer critical
sections of AGC interpreter code that performed key guidance computations, documenting them
in this form. The documents he produced became invaluable technical documentation for both NASA and MIT.
Although Norton's software skills became legendary, he was otherwise apparently a tad
quirky...often not cashing several months worth of paychecks at a time. One when one MIT
programmer tried to have a bit of fun, burying the phrase "Norton Needs Glasses" in comments
in the bowels of major mode program P52 (just to see how long it would take him to find it
apparently only a few hours of analysis), Norton asked for MIT to be removed from the project.

This was a form of *independent peer review* akin to what code teams do now every day with
pull requests on GitHub.


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
The whole collection of components
represented a complex feedback control system, the stability of which was
crucial to crew safety and mission success.

Originally, Honeywell was to develop the autopilot was the responsibility of the Honeywell.
However, was an analog design that lacked the flexibility and versatility required for the
complex Apollo mission plans. It also added significant
weight to the spacecraft. Consequently, NASA directed the MIT to develop software for
a digital autopilot which would have none of these limitations. In addition MIT
requested that the autopilot logic be able to serve as a backup for guidance of
the full Saturn V rocket boost phase into Earth orbit.
Originally, the auto-pilot features of the LEM were planned to be developed using tried and true
analog control system. However, as concepts and confidence grew in the potential to use
the AGC as a *digital* control system, the decision was made in late 1964 to develop the
Digital Autopilot (DAP) software. The DAP software would control main engine gimbal and
attitude control thrusters during a *burn* to maintain a given attitude or attitude rate
and to achieve a given desired velocity change (magnitude and direction). The DAP software
would also need to affect its controls subject to a number of limitations in the RCS jets
and main engine including optimizing RCS propellent use, avoiding gimbal lock as the
spacecraft orientation is changed, detecting and avoiding failed on or off RCS jets,
minimizing jet thrust durations in certain directions that impinge on spacecraft skin
or direct debris at windows

DAP software was
given a budget of 10% of rope core memory (< 3,600 words) and 20-30% of full computational
load (3-4.5 kFLOPS).

This was the first known use of a digital control 

With the AGC at the hear of complex collection of sensors, thusters, the main engine and
pilot controls and displays, the whole set of components formed a complex feedback control
system.  *Stability* was a key concern.

Something like this had never been done before.

It would take 4 developers 3 years and 2000 words of rope core

4 developers over 3 years ~2000 words at 20% of CPU 

change in coordinates to *jet axes* reduced complexity of code, increased performance, 

systems. The whole system forms a complex feedback control system
the stability<sup>[1]</sup> of which is an essential characteristic. Early on in the software development,
the problem was to understand the equations governing spaceflight certain mission objectives
and then develop approaches utilizing available sensors and controls to affect responses in real-time.

In the software system, just as in the case of hardware systems, the engineering attention required of the interface between two components may sometimes exceed the attention required for the selection or de- sign of the components.


By early 1965, the basic RCS autopilot functions were laid out, including phase-plane and jet- select logic, a new maneuver routine, and interfaces for the various manual modes.



# AGC *Apps* and Apollo Mission Workflow
Flying to the moon and returning safely involved *long periods of boredom
punctuated by moments of extreme peril*. A mission was divided into phases by
*velocity change maneuvers* or *burns* of the main engines. A complete mission
involved around 11 burns. For each manuever,
there was a cooresponding program, called a *major mode* in the AGC to handle
it. Time crtical maneuvers such as lunar landing, rendevouse and docking and
re-entry involved multiple programs working in sequence. For every phase of the
mission, in today's parlance we'd say *there was an app for that*.

Development of a *major mode* software program began by understanding the equations
of motion governing the particular phase of spaceflight and then outline computational
approaches utilizing available spacecraft sensors, controls and engines to affect the
desired outcomes and in specified computer time and space (memory) requirements.
The minimum time an RCS thruster could be fired was 14 milli-seconds. The LEM descent
engine could not operate 

equations of motion
of design and planning, development of the equations of motion,
identification of goals and constraints (usually fuel consumption), prototypes
code on IBM and Honeywell mainframes

As mission software evolved...


By far the most critical sequence of manuevers occured during lunar landing.
Lunar landing was divided into 4 phases depending on the amount and type of
control the pilot required. Powered Descent (P63), Approach (P64), Terminal Descent (P66), Touchdown (P68)

- Powered Descent / Braking Phase (P63)
  - Fully auotmatic
  - Pilots compare state to cheat sheet prediction
- Approach Phase (P64) 
  - Pilot can re-designate landing target for auto to hit
  - Pilot controls rate of descent
- Terminal Descent (P66)
  - Auto Descent (P65)
  - Full Manual (P67)
- Touchdown (P68)

The sequence of operations the software needed to perform during these 4 phases were...
small *ullage* burn of the RCS thrusters to force main engine fuel to bottom of the tank,
countdown and pilot **PRO**ceed acknowledgement to descent engine start up at 10% thrust,
gimbaling main engine around to detect center of mass, throttle up to 96% thrust at 26 seconds
maintaining windows down attitude, yaw-around to windows up attitude at about 6 minutes
into descent, maintaining orientation for communication with Houston, maintaining landing
radar lock on the lunar surface, maintaining spacecraft attitude with DAP, responding to
pilot inputs on the DSKY, joystick or other controls and updating cockpit displays
and status lights. So, although the *main* program (major mode) the AGC was running during
each phase was P63-\>P64-\>P66, the AGC would typically be running several other (a maximum
of 8 simultaneous programs) programs to perform other functions. Although the spacecraft
is no longer in motion at the moment of touchdown, the main engine is still running, the
DAP is still furiously trying to maintain attitude. The astronauts need to perform a 

the DAP is still trying to maintain spacecraft attitude even though it is no longer moving
there are a number of time-critical tasks to astronauts needed to perform

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

the first step in developing a major program in the AGC was to
understand the equations governing spaceflight and outline computational approaches utilizing
available sensors and controls to affect control in specified time and space (memory) requirements.


# Managing Software in the face of Evolving Requirements
The whole GN&C system for all 16 uncrewed and 11 crewed Apollo missions
cost a total of ~$600 million<sup>[24]</sup> over 10 years. The software
effort was about 10% of that<sup>[23]</sup> the majority of it occurring
over the last 5 years.

> Before the first lunar landing, more than 1400 person-years of software
> engineering effort had been expended, with a peak level of effor of 350
> engineers reached in 1968.

Below we compare key aspects of the Apollo GN&C effort with
the Exascale Computing Project. One aspect in all likelihood remarkably
different between the two projects is the emphasis on publication.
Although the Apollo effort did publish some, the amount of publication
relative to the whole effort is in all likelihood smaller than that
required of ECP software developers.

Project | 1965 Dollars | 2019 Dollars | Publications + Theses 
---|---|---|---
Apollo GNC Total | $600M | ~$5B | ~60 + 60
Apollo GNC Software | $60M | ~$0.5B | ~25 + 13
ECP Total | ~$100M | $809M |
ECP Software | XXX | XXX | XXX

> In the early stages, there were no "programmers". Instead engineers and scientists
> learned the techniques of programming. It was believed that competent engineers could
> learn programming more easily than programmers could learn engineering.<sup>[30]</sup>

We can thank Margaret Hamilton, who received the Presidential Medal of Freedom for her
work on the on AGC<sup>[29]</sup>, for being the first to champion *Software Engineering*<sup>[28]</sup>
as a discipline unto itself "...to bring the software [effort] legitimacy so that it
and those building it would be given due respect."

Throughout the early phases of development, NASA's expectations for what functions
the GN&C system would perform continued to evolve motivated by a desire to reduce
weight, increase safety margins, improve mission flexibility and optimize propellent
usage.

> NASA had established a need for the machine and had determined its general tasks, and
> MIT received a contract based on only a short, very general requirements statement.
> Requirements started changing immediately and continued to change throughout the program.

Midway through the project the AGC was re-desinged to support more memory.
Developers had to support both the old, Block I, and new, Block II systems.
Block I would be used on early, uncrewed Apollo test flights and Block II on crewed flights.
They were different enough that each required separate software development teams which
served to increase the software management burden.

Attribute | Block I (fall 1962) | Block II (summer 1966) 
---|---|---
Fixed/Eraseable Memory (k-words) | 24 / 1 | 36 / 2
Logic #ICs (NOR gates/IC) | 4,100 (x1) | 2,800 (x2)
Clock / Instructions | 1.024 Mhz / 11 | 1.024 Mhz / 34
Power/Weight | 85W / 39.5kg | 55W / 31.9kg
Flops (kF) | 7.1 | 14.5

Block II had only 2K words of read-write (*erasable*) core and 36K words of
read-only core (*fixed* or *rope core*). All software and data had to fit into
this combined 76KB of memory. The AGC did not support floating point. Instead,
like a *slide rule*,<sup>[22]</sup> it used a *fractional* representation where
the *exponent* was managed implicitly. Developers simply agreed on the implied
scaling of any particular numerical value as well as coding explicit re-scaling
as needed to maintain precision.

Developer productivity was measured in new *words per month* of fully tested
AGC code. Given the tight memory constraints, however, the main problem was not
developer productivity. It was fitting all the developed code into
memory. In early 1966, a new "watchdog" manager was assigned; Bill
Tindall. He became famous for his sharply worded progress memos known as
*Tindallgrams*. His first major action was to hold a series of meetings, the first on
Friday the 13th of May in which decisions were made on which programs to cut
from the AGC to fit the code they had into memory. This was the first of many such
meetings which became known as *black friday* meetings. As difficult and emotional
as these meetings were resulting in months if not years of software development
work being removed from missions, most MIT development staff eventually recognized
they would not have produced a working mission program without Bill Tindall's
relentless efforts to cut functionality to meet constraints.


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
[23]: https://www.ibiblio.org/apollo/hrst/archive/1728.pdf "AGC Software Development Productivity and Costs {Rankin DA. (1972) A Model of the Cost of Software Development for the Apollo Spacecraft Computer, Masters Thesis, MIT}"
[24]: https://history.nasa.gov/SP-4029/Apollo_18-16_Apollo_Program_Budget_Appropriations.htm "Apollo Budget By Sub-Program and Year {}"
[25]: https://www.ibiblio.org/apollo/Documents/SGA_Memo11_620716.pdf "List of Software Studies Underway in 1962 {}"
[26]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap "Part 1 in this series {}"
[27]: https://www.doneyles.com/LM/ORG/index.html "MIT Org Charts (1969) {}"
[28]: https://www.computer.org/publications/tech-news/events/what-to-know-about-the-scientist-who-invented-the-term-software-engineering "Origin of the term 'Software Engineering' {}"
[29]: https://www.nasa.gov/feature/margaret-hamilton-apollo-software-engineer-awarded-presidential-medal-of-freedom "Margaret Hamiliton Medal of Freedom {}"
[30]: https://www.ibiblio.org/apollo/hrst/archive/1137.pdf "The MIT Software Effort {Johnson MS Giller DR (1971) MIT's Role in the Project: Final Report on Contracts, Vol. 5 The Software Effort, NAS 9-153 & NAS 9-4065}"
[31]: https://www.google.com/search?client=safari&rls=en&ei=YeryXMO2H6m_0PEPvciWiA8&q=what+is+co-design+in+computing&oq=what+is&gs_l=psy-ab.1.0.35i39l2j0i67l5j0l2j0i131.1499.3009..4244...2.0..0.121.836.5j4......0....1..gws-wiz.......0i71j0i10j0i10i67.bQxpLbPTVwU "Google Search co-design in computing {}"
[32]: https://www.ibiblio.org/apollo/Documents/j2-80-MSC-69-FS-4_text.pdf "Example of Norton's Programmed Equations {}"
[33]: http://tindallgrams.net/66-FM1-68 "Tindall-gram about Software Development Processes {}"
[34]: https://www.ibiblio.org/apollo/AGC-versions.jpg "AGC Software Version History {}"

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

Say something about Kerbel Space Program and how its calculational aspects work and how they are broken down into pieces.

Say something about 4 computers

Say something about Russian space program computers

Mission specific programming and testing.

11 burns needed...

Launch from earth. This you might count as three burns, since it requires all three stages of the Saturn V rocket. They're not only launching from earth at this point, but they're also burning to get into a circular orbit around the earth.
Leave earth orbit for the moon (translunar injection). Here they relight the third stage of the Saturn V, using up the rest of its fuel. At this point, they should be on a free-return trajectory, meaning that if they do nothing else, they'll slingshot around the moon and come back to the vicinity of the earth.
Make a midcourse correction. These corrections are made using the engine built onto the Service Module (SM).
Make another midcourse correction, as needed.
Get into an elongated orbit around the moon. This uses the SM engine.
Circularize the orbit around the moon. This also uses the SM engine.
Get into descent orbit. This uses the descent engine on the Lunar Module (LM).
Descend to the moon. This also uses the descent engine on the LM.
Ascend from the moon. This uses the ascent engine on the LM, leaving the descent portion behind.
Leave lunar orbit for the earth (transearth injection). This uses the SM engine.
Make a midcourse correction. This also uses the SM engine.






> Throughout much of the Apollo effort, MIT experienced difficulty in estimating the
> time and effort requirements to design, test and verify successive mission programs.<sup>[30]</sup>

> No one doubted the quality of the software eventually produced by MIT. It was the
> process used in software development that caused great concern. The lessons were:
> (a) up-to-date documentation is crucial, (b) verification must proceed through
> several levels, (c) requirements must be clearly defined and carefully managed,
> (d) good development plans should be created and executed, and (e) more programmers
> do not mean faster development<sup>[19]</sup>.
