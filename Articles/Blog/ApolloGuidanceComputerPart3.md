# Pre-Reference Version: Celebrating Apollo's 50th Anniversary: User Stories from Space

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/foo.jpg' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: July 12, 2019

*Third of a three-part series to commemorate the 50th anniversary of the Moon landings.*

In the Apollo program, the *end-users* were first and foremost the astronauts who
had to fly the vehicles the AGC controlled. Among the astronauts there were widely varying
perspectives about how much and what kind of control they would yield to this new technology.


In the lunar module, the computer's *Proceed*
button, the main engine *Shutdown* button and the *Abort* button were in such close
proximity<sup>[3]</sup>, it would have been very easy for users to hit the wrong button.
Fortunately, this never happened.


the users really had think carefully about hitting the right
buttons at the right times and not hitting the wrong buttons.

making sure they hit the right button(s) at the right time. 

I am reminded







This is the third of three articles about the AGC. In parts 1 and 2, we described the
hardware<sup>[1]</sup> and software.<sup>[2]</sup> Here, in part 3, we focus on *applications*;
that is the actual use of the AGC in Apollo missions.


We cannot write about how Apollo astronauts flew to the moon without using *verbs*
and *nouns*?

## Uncrewed Missions
Block I AGCs were used in 4 uncrewed Apollo missions designed primarily to test
the main spacecraft components and less so to test the AGC. Nonetheless, the computer was a
critical part of these missions because of the flexibility it gave mission planners and
mission control. For example, Apollo 6 was to be the first Apollo flight to perform
a trans-lunar injection burn. However, the main Saturn booster suffered serious
*pogo oscillations* damaging the upper stages preventing such a test. Using the in-situ
programmability of the AGC, mission control was able to easily adjust the mission plan
mid-flight.

## Wally Schirra

Wally Shcirra was perhaps the most automation-resistant of the bunch. He planned to manually
fly the re-entry of Apollo 7. But when delays put them dangerously behind on checklist items,
at the last minute he had no choice but to switch to automated re-entry. With the AGC in control,
Apollo 7 splashed down safely, on schedule and within 2 miles of their intended target. After,
Schirra wouldn't stop singing the praises of the AGC. He felt it had saved their lives, giving
the crew the extra time they needed to finish adjusting equipment and strapping in for re-entry.

## Jim Lovell
While practicing guidance alignments with the space sextent on the return leg of Apollo 8,
Jim Lovell accidentally keyed in a pre-flight program, `P01`, instead of star identifier
`01` from the AGC's star catalog. This potentially corrupted key portions of the AGC's
eraseable memory causing the computer to loose track of the spacecraft's position and
orientation. It took NASA and MIT 9 long hours to radio up a fix to the problem.
Little did Lovell know that an elementary aged school girl had helped to
find this problem and a program change to fix it had been proposed months earlier.

One user nobody had planned for was Margaret
Hamilton's elementary school daughter, Lauren. Once while playing astronaut during a visit
with her mother at work, Lauren managed to key in DSKY commands causing an AGC simulator
to crash. The simulator was running an in-flight program and Lauren had keyed in a command
to select and run a pre-flight program. Alarmed, Hamilton's first thought was
*what if an astronaut did that in flight?* She investigated the cause and proposed a program
change to prevent such accidental entry. However, NASA believed the astronauts were so well
trained the would never make such a mistake and rejected the program change. 

On Apollo 13, Lovell would benefit from "what if" thinking by MIT software developers that
might have prevented his earlier problems on Apollo 8. For Apollo 9, MIT software developers
needed to create a major mode program that allowed the crew to test the lunar module descent
engine while the LM and CSM were docked, a unusual coniguration not ordinarily used for a
normal Apollo mission. It was considered the safest configuration for the first ever test of
the lunar module. That code remained in the flight program for later Apollo missions and is
what enabled the crew of Apollo 13 to use the LM descent engine for two of the burns that
brought them home. A third burn was also needed but because the LM AGC had been shut down
used a second computer, the Abort Guidance System (AGS) and a guidance technique using the
Sun and both end-points of the Earth's terminator, something Lovell had in fact practiced
on Apollo 8.

## Apollo 9 and EMPs (in-situ firmware updates to Apollo hardware) Flashing the CSM
EMPs are Erasable Memory Programs;<sup>[5]</sup> that is, programs stored in erasable rather
than fixed AGC memory. While for special purpose testing of the AGC, EMPs were viewed as too
risky (last minute changes) to be a planned part of any crewed mission.
However, they were used with increasing regularity in later Apollo missions to work into the
mission functionality that was fully developed but nonetheless couldn't make the typical 4
month lead time for rope core manufacture. An early success of EMPs happened on Apollo 9.
Apollo 9 was an Earth orbital mission to test the lunar module descent and ascent engines as
well as rendezvous betwween CSM and LM. One key capability the astronauts wanted as to have
the AGC maintain the CSM nose always pointing "down" towards the Earth as it orbited. This
meant the CSM needed to rotate in sync with its orbital position. A program to support this
had been developed and tested (in simulator testing) earlier but was not part of Apollo 9's
rope core flight program. Once in orbit, the astronauts entered a few dozen DSKY keystrokes
to upload the EMP and it worked as advertised.

## Barbeque Mode (10)
After the lunar landing itself, *Passive Thermal Control (PTC)* is perhaps the most challenging
manuever in the Apollo program. Why? It is very subtle. It is also known as *Barbecue Mode*.
The goal is to spin up the docked CSM/LM (or on return from the moon just the CSM) rotating
along its longitudnal axis, at one to three revolutions per hour to even out heating over the
spacecraft due to the Sun. The challenge comes in due to *wobble*. If it isn't done just right,
the spacecraft's orientation will slowly wobble causing a whole host of issues with IMU drift
potential of gimbal lock, overuse of RCS propellents to keep the wobble in check, etc. In
particular, it can prevent the crew from getting a good night's sleep if they have to always
be pestered to make adjustments or if the AGC is frequently firing RCS thrusters. The problem
was best described during Apollo 10

## Jack Garman, Niel Armstrong and Computer Alarms
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
blanked out. In hundreds of simulations, neither Niel nor Buzz had ever seen this program alarm.
In fact, most software developers at MIT had never seen it. But, one did; Jack Garman.
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
normal program execution is briefly delayed as the program counter is temporarily stopped
incrementing while data from the external hardware is routed to the computer's eraseable
memory. Ordinarily, the delays caused by cycle stealing are insignificant to overal computer
performance. The problem with Apollo 11 is that due to a phasing problem in RR circuitry,
the computer was being updated 6400 times per second, each time stealing precious cycles
primary guidance routines needed for landing. The resulting additional load on the computer
meant that it occasionally did not have sufficient memory to run all processes.

## John Aaron, Alan Bean 
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

## Greatest Hack in the History of Computers

## Terrain Models

## IMU "Recognition"

## Earth Rotation and IMU
Russian failure and American

## Uses of AGS (10, 11, 13)

## Russian

## Apollo had Four Computers



###### Ref to Fairchild, AGS and Moore's law
https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips


[1]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap "AGC Blog Part 1 {}"
[2]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-the-oldest-code-on-github "AGC Blog Part 2 {}"
[3]: https://youtu.be/hCywOf0Czgg?t=1841 "Presentation by Dave Scott about the AGC {}"
[4]: https://www.ibiblio.org/apollo/hrst/archive/1033.pdf "AGC Restart System Design {}"
[5]: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19720025984.pdf "Erasable Memory Programs {}"


