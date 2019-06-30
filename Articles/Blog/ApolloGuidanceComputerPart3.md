# Pre-Reference Version: Celebrating Apollo's 50th Anniversary: User Stories from Space

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/foo.jpg' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: July 12, 2019

*Third of a three-part series to commemorate the 50th anniversary of the Moon landings.*

In the Apollo program, the computer *users* were first and foremost the astronauts who
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
orientation. Little did Lovell know that an elementary aged school girl had helped to
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

## John Aaron (or Alan Bean) CSE-2-Aux
John Aaron wasn't a *user*. He was, however, an Apollo fight controller.

## Apollo 1
Pure oxygen at 2 psi above atmospheric pressure, 5000 in<sup>2</sup> of highly combustable
Velcro and a spark in the electrical system lead to a horrendous fire killing the crew
of Apollo 1 during a launch rehersal. The subsequent pause in the launch schedule for safety
improvements gave MIT an extra 21 months to resolve issues with delivering flight-ready software.
In that time, under the relentless leadership of system integrator Bill Tindall, MIT developers
transitioned from *triage* mode to *optimization* mode.

###### Ref to Fairchild, AGS and Moore's law
https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips


[1]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap "AGC Blog Part 1 {}"
[2]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-the-oldest-code-on-github "AGC Blog Part 2 {}"
[3]: https://youtu.be/hCywOf0Czgg?t=1841 "Presentation by Dave Scott about the AGC {}"


