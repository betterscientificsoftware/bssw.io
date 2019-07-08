# Pre-Reference Version: Celebrating Apollo's 50th Anniversary: User Stories from Space 

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/foo.jpg' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: July 12, 2019

*Third of a three-part series to commemorate the 50th anniversary of the Moon landings.*

In the Apollo program, the *end-users* were first and foremost the astronauts who had to fly the
spacecraft the AGC controlled. Among them throughout the development of the AGC, there were widely
varying perspectives about how much and what kind of control should be given up to the computer.
Wally Schirra was perhaps the most automation-resistant of the bunch. So much so, he planned to
manually fly the re-entry of Apollo 7. But when delays put them dangerously behind on checklist
items, at the last minute he had no choice but to switch to automated re-entry. With the AGC in
control, Apollo 7 splashed down safely, on schedule and within 2 miles of their intended target.
After, Schirra couldn't stop singing the praises of the AGC. He felt it had saved their lives,
giving the crew the extra time they needed to finish stowing equipment and strapping in for
re-entry.

This is the third of three articles about the AGC. In parts 1 and 2, we described the
hardware<sup>[1]</sup> and software.<sup>[2]</sup> Here, in part 3, we focus on *applications*;
that is experiences in the use of the AGC in actual Apollo missions.

## There are no User Stories without Verbs and Nouns
It is impossible to write about how Apollo astronauts flew to the moon without using `Verb`s and
`Noun`s. Unlike Kubrik's 1969 film, *2001: A Space Odyssey*, where the crew held conversations
with their HAL computer, Apollo crews interacted directly with the AGC through LED-like displays
and a keypad called the DSKY (proncouned *disskee*). Verb codes specified an action to take.
Noun codes specified the data upon which the action was taken.<sup>[6]</sup> For example, to
display current velocity, the astronauts would perform the following keystrokes, `Verb`, `0`, `6`,
`Noun`, `6`, `0`, `Enter`. The Verb code `06` means to display some data in decimal. The Noun code
`60` means the data for velocity. The keystrokes, `Verb`, `3`, `7`, `Noun`, `0`, `1`, `Enter`
means to begin the pre-launch program to align the Intertial Measurement Unit (IMU).

The AGC was sometimes refered to as Apollo's fourth crew-member. After hundreds of hours training
in simulators, the astronauts had AGC *code-speak* memorized and could probably operate it
blind-folded. Nonetheless, operating the DSKY in thickly gloved hands, quickly and accuratley under
the pressure of time-crtical flight operations was not easy. Dave Scott explained that in the
lunar module, the computer's *Proceed* button, the main engine *Shutdown* button and the *Abort*
button were in such close proximity<sup>[3]</sup>, it would have been very easy for users to hit
the wrong button at the wrong time. All the astronauts had to *"...think very hard..."* to avoid
making such a mistake. Fortunately, that never happened.

## What an Elementary School Girl Knew about the AGC that Jim Lovell Didn't
While practicing guidance alignments with the space sextent on the return leg of Apollo 8,
Jim Lovell accidentally keyed in a pre-flight program, `P01`, instead of star identifier
`01` from the AGC's star catalog. This corrupted key parameters used in guidance computations
in the AGC's eraseable memory. It took NASA and MIT nine long hours to radio up a fix to the
problem. Little did Lovell know that an elementary aged school girl had helped to find this
problem and a program change to fix it had been proposed months earlier.

One AGC user nobody had planned for was Margaret Hamilton's elementary school daughter, Lauren.
Once while playing astronaut during a visit with her mother at work, Lauren managed to key in
DSKY commands causing an AGC simulator to crash. The simulator was running an in-flight program
and Lauren had keyed in a command to select and run a pre-flight program. Alarmed, Hamilton's
first thought was *what if an astronaut did that in flight?* She investigated the cause and
proposed a program change to prevent such accidental entry. However, NASA believed the
astronauts were so well trained they would never make such a mistake and rejected the
program change. After Lovell's accidental entry in Apollo 8, the program change was approved.

## Flashing the AGC with EMPs 
EMPs are Erasable Memory Programs;<sup>[5]</sup> that is, programs stored in erasable rather
than fixed AGC memory. While often used for special purpose testing of the AGC, EMPs were
thought too risky (last minute changes) to be a planned part of any crewed mission.
However, they were used with increasing regularity in later Apollo missions to work in
functionality that was fully developed but nonetheless couldn't make the typical four
month lead time for rope core manufacture. An early success of EMPs happened on Apollo 9.
Apollo 9 was an Earth orbital mission to test the lunar module descent and ascent engines as
well as rendezvous betwween CSM and LM. One key capability the astronauts wanted as to have
the AGC maintain the CSM nose always pointing "down" towards the Earth as it orbited. This
meant the CSM needed to rotate in sync with its orbital position. A program to support this
had been developed and tested (in simulator testing) earlier but was not part of Apollo 9's
rope core flight program. Once in orbit, the astronauts entered a few dozen DSKY keystrokes
to upload the EMP and it worked exactly how they wanted it to work.

## Overcooking the Barbecue
*Passive Thermal Control (PTC)* or *Barbecue Mode* as it is often called, is likely most
tempermental manuever in the Apollo program. Why? It is very sensitive to initial conditions
The goal is to spin up the docked CSM/LM (or on return from the moon just the CSM) rotating
along its longitudnal axis ever so slightly at one to three revolutions per hour to even out heating over the
spacecraft skin due to the Sun. The challenge is to get the spacecraft *barbecueing* and then
allow it to just coast for long periods of time without falling into a bad *wobble*. If it isn't done just right,
the spacecraft's orientation will slowly wobble causing a whole host of issues with IMU drift
risk of gimbal lock, overuse of RCS propellents to keep the wobble in check, etc. In
particular, it can prevent the crew from getting a good night's sleep if they have to always
be pestered to make adjustments or if the AGC is frequently firing RCS thrusters. The 
challenge with this manuever was that the desired axis of rotation (down the geometric center of the
docked CSM/LM) doesn't align with any of the body's inertial principle axes of rotation.
This means the RCS have to be consantly firing to maintain the torque required to keep the
axis of rotation aligned correctly.

This means that starting with an initial condition of angular velocity about only the desired
axis of rotation, alone is that over time, the time varying rotation of the body will be such 
that it will rotate signficantly on all 3 axes. The solution is to input some non-zero rotational
velocity (two orders of magnitude lower) about the other axes of rotation which has the effect
of keeping under control the growth of rotation about those axes as time evolves. Ultimately,
this mean astronauts needed to engage the AGC to impose a small driving torque

## Cycle Stealing Gone Awry; Restart to the Rescue
The Apollo 11 lunar landing is perhaps the most dramatic and oft-told story about the AGC.
Most versions of this story focus on what was happening in the cockpit of the lunar lander.
In this most intense moment of the Apollo program, the first time humans would land on the
surface of the moon, the AGC flashed a *program alarm*, a *1202*. The particular situation
causing the alarm is perhaps less important than the computer's response to it; a *restart*.
It cleared out all running programs and then restarted them in priority order according to
a pre-programmed set of restart rules. Restart was something that had been designed into
the AGC from the very beginning. For Niel and Buzz who were still descending to the surface
and streaking across the lunar horizon at over 2,000 feet/second, their DSKY went blank 
for several seconds. The descent engine was still burning to slow their velocity. They could
see the surface approaching out the windows. But their computer, which controlled the whole show,
blanked out. In hundreds of simulations, neither Niel nor Buzz had ever been confronted with
this situaton. In fact, most software developers at MIT had never seen it. But, one did; Jack Garman.
At Gene Kranz' behest, in the months before the Apollo 11 launch, Jack audited AGC software 
and compiled a cheat sheet of every possible error code the AGC could produce, their meanings and
what their impact would be depending on when they occurred during landing. After consulting his
cheat sheet, it was the 26 year old Jack Garman who made the "go" call to proceed with the landing.
But, at mission control, the whole process took 30 seconds.  From the time Niel
and Buzz reported the program alarm and awaited guidance from mission control on what to do
about it, 30 seconds passed. The LEM dropped over a mile in altitude and traveled over 10 miles
down range. During the landing, Armstrong and Aldrin experienced four 1202 alarms and one 1201
alarm. Each time, Jack Garman made the "go" call to proceed past them.

Later investigations found the root cause to be a problem in phasing in the hardware interface
between the computer and rendezvous radar. The AGC used the technique of *cycle stealing* to
allow GN&C hardware components to update their state in eraseable memory. In cycle stealing,
normal program execution is briefly paused as the program counter is temporarily stopped
incrementing while data from the external hardware is routed over the bus to the computer's eraseable
memory. Ordinarily, the delays caused by cycle stealing are insignificant to overal computer
performance. The problem with Apollo 11 is that due to a phasing problem in RR circuitry,
the computer was being updated 6400 times per second, each time stealing precious cycles
primary guidance routines needed for landing. The resulting additional load on the computer
meant that it occasionally did not have sufficient memory to run all processes.

## "Try SCE To Aux"
I tried to get a personalized plate with SCE2AUX. Someone in California already has it.
Less than 30 seconds into the launch of Apollo 12, with the Saturn booster pushing them 
towards space with 7 million pounds of thrust, much to the surprise of the crew, the AGC
went on the fritz. The DSKY went blank and then the whole cabin lit up with caution and
warning lights and buzzers. Pete Conrad reported "we just lost the whole platform". In
mission control...the same story. All the telemetry went on the fritz. Nonetheless, 
John Aarons noticed a pattern in the jibberish on the displays in mission control.
John Aaron wasn't an *end-user*. He was an Apollo flight controller. So, he sort of worked
at the main Apollo telephone support center. In simulations years prior to Apollo 12,
Aarons had experienced a similar situation for which the solution was to switch the
CSM Signal Conditioning Equipment (SCE) to Auxiliary. Aaron's had mission control radio
up to the crew "Try SCE to Aux." Miraculously, the AGC and all the displays in mission
control came back on line and Apollo 12 safely continued flying

Apollo 12 had been hit by lightning. Fortunately, the AGC was only monitoring the Saturn
booster during the launch, not controlling it. A second computer, the Launch Vehicle Digital
Computer (LVDC) designed and manufactured by IBM, was controlling the vehicle into Earth orbit.
It performed flawlessly and Apollo 12 continued to the moon.

Apollo 12 went on to perform a pin-point landing, within a short lunar stroll of Surveyor III.
To achieve this landing accuracy, AGC software was revised just for this mission to incorporate  

## What-if Thinking
On Apollo 13, Lovell would benefit from "what if" thinking by MIT software developers that
might have prevented his earlier problems on Apollo 8. For Apollo 9, MIT software developers
needed to create a major mode program that allowed the crew to test the lunar module descent
engine while the LM and CSM were docked, a coniguration not ordinarily used for an
Apollo mission. It was considered the safest configuration for the first ever test of
the lunar module. That code remained in the flight program for later Apollo missions and is
what enabled the crew of Apollo 13 to use the LM descent engine for two of the burns that
brought them home. A third burn was also needed but because the LM AGC had been shut down
used a second computer, the Abort Guidance System (AGS) and a guidance technique using the
Sun and both end-points of the Earth's terminator, something Lovell had in fact practiced
on Apollo 8.


## Tech Support from 1/4 Million Miles
During Apollo 14, the all important *Abort* button in the LEM was found to be faulty. It was occasionally
closing a circuit indicating to the AGC that the *Abort* command had been given. This of course
would be disasterous if it occurred during a landing attempt. MIT needed to quickly devise a
procedure the crew would use to allow the landing to proceed without risk of being inadvertently
aborted due to the faulty switch. Apollo 14 waited, orbiting the moon and delaying their landing
four long hours as MIT poured over AGC source code looking for a solution that required as few
keystrokes as possible but provided assurance the faulty *Abort* switch would be ignored. MIT
radioed up

. It his hard to enter keystrokes in thickly gloved hands accurately and quickly while you also flying
a vehicle descending at high speed to the lunar surface.

## Earth Rotation and IMU
Russian failure and American

## Computing and Spaceflight
Each Apollo lunar landing mission included four computers. There was on AGC in each of the the CSM and LM.
There was also the Launch Vehicle Digital Computer (LVDC) that provided guidance for the Saturn rocket's
first three stages during launch and the Abort Guidance System (AGS) on the LM which served as a backup
to the AGC in case a lunar landing needed to be aborted. Below, we capture some of the key design features
of each of these computers

Computer | Manufacturer | Power &<br>Weight
---|---|---
LVDC|IBM|
AGC|Raytheon|32kg, 55W
AGS|TRW|14Kb, 90W

Although it was intended only for backup, AGS was ultimately used in four Apollo missions. In Apollo 9,
both the descent and ascent stages of the LM were tested in Earth orbital flight. The test of the ascent
stage and rendevous with the CSM used the AGS computer for guidance. In Apollo 10, the LM descended to
within 47,000 feet of the lunar surface and then, as planned, executed a full up abort 
severing the descent stage and turning control of the ascent stage from the AGC over to the AGS computer.
However, an incorrect switch setting putting AGS in *Auto* mode rather than *Attitude Hold* prior to the
manuever led to a prompt and pronounced deviation in attitude just moments before staging. In 16mm camera
footage, the descent stage as well as the lunar horizon are seen racing across field of view for a period
of ~15 seconds before the situation is brought under control. In Apollo 11, AGS was briefly used for 
attitude control at the final moments of docking with the CSM because the LM had been manuevered such
that PGNS was in gimbal lock. The final use of AGS was in Apollo 13 for two mid-course corrections on 
the return to Earth. PGNS had been fully shut down due to its power and water use.

* RTCC
* The Russians
* 



###### Ref to Fairchild, AGS and Moore's law
https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips


[1]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap "AGC Blog Part 1 {}"
[2]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-the-oldest-code-on-github "AGC Blog Part 2 {}"
[3]: https://youtu.be/hCywOf0Czgg?t=1841 "Presentation by Dave Scott about the AGC {}"
[4]: https://www.ibiblio.org/apollo/hrst/archive/1033.pdf "AGC Restart System Design {}"
[5]: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19720025984.pdf "Erasable Memory Programs {}"
[6]: https://www.ibiblio.org/apollo/A17_VN_Checklist.png "Verbs and Nouns Cheat Sheet {}"
[7]: https://youtu.be/22adjMrYl0E?t=20 "Demonstrating DSKY during Apollo 11 {}"

<!---
Image source infor

https://en.wikipedia.org/wiki/Apollo_Guidance_Computer#/media/File:Dsky.jpg

--->



