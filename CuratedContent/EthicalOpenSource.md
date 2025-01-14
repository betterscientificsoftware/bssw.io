## Ethical Open Source Licensing

<!--- deck text start --->
Is your open source code being used for good or evil?
<!--- deck text end --->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: February, 15, 2025

Resource information | Details
:--- | :---
title | 
Authors |
Website |

In the last 20 years, the meaning of *open* in "open-source" has evolved significantly.
Originating out of principles of freedom, transparency, and collaboration, open-source licenses govern the use, modification, and distribution of software and, increasingly, now data. 

The open-source movement traces its origins to Richard Stallman’s creation of the **GNU General Public License (GPL)** in 1989.
A restriction of GPL is that whenever GPL software is used in other software, that other software must itself also be openly and freely available under the terms of GPL.
This *viral* design sought to supercede proprietary interests and ensure that software remains a shared resource free to be modified and redistributed.
Legally speaking, GPL prevents commercial companies developing proprietary software from using any GPL software in their products. 

Eventually, commercial interests subverted this design and permissive open source licenses took hold.
These licenses grant commercial companies the freedom to use the software in virtually any way they wish, including modifying it, integrating it into for-profit products, and redistributing it under a proprietary license.
The only significant requirement is proper attribution.

In particular, with permissive open-source licenses, all ethical considerations are left largely to the discretion of users.
Is it ok if the software is used, for example, in human cloning or in autonomous military drone targetting systems or to design and 3D print a gun that evades security checks or by a government to surveil its population?

In recent years, some examples of the use of open-source software for purposes ethically questionalbe to its developers have emerged.
Elasticsearch, a widely-used open-source search and analytics engine, was reportedly used by U.S. Immigration and Customs Enforcement (ICE) to support family separating deportations.
Developers have sought to release future versions using more [restrictive open-source licensing](https://pureinsights.com/blog/2024/elastics-journey-from-apache-2-0-to-agpl-3/).
There is another example involving ICE and [Chef configuration management software](https://www.wired.com/story/software-company-chef-wont-renew-ice-contact/).
Some Google employees [protested and others resigned](https://www.nytimes.com/2018/04/04/technology/google-letter-ceo-pentagon-project.html) upon learning that TensorFlow was being used for US military drone targetting.
DockerHub and Docker images have been abused for [cryptojacking](https://unit42.paloaltonetworks.com/malicious-cryptojacking-images/).

For these reasons, there is growing interest in the open-source community of developing a new kind of open-source license; [an ethical, open-source license](https://ethicalsource.dev) with the intent of ensuring the use of open-source software only for ethical purposes.

The original GPL license was restrictive in that it demanded it be used only within other GPL licensed software.
The US Department of Energy (DOE) has categories of software, albeit *not* open-source, it deems export controlled or classified.
National and international sanctions can demand cloud providers like Google and Microsoft to restrict access to their software and services in specific regions.
So, placing restrictions on the distribution and use of software is not a new idea.
What is new is the interst in restricting use to ethical purposes.

<!--
For comparison, its worth considering analagous restrictions placed on real-world products and services.
A good example is chemicals.
Chemical manufacturers all over the world face various restrictions -- environmental, human health, regulatory -- in what they produce and where they can sell it.
At the same time, a chemical manufacturer often has little or no control over how their product is ultimately used once it is sold.
-->

Two ethical open-source licenses are currently available; the [Hippocratic License](https://firstdonoharm.dev/learn/) and the [Do No Harm License]().
Of the approximately 8,500 packages in Spack, one uses the Hippocratic License.
The world is becoming more and more controlled by software.
Developers of open source with permissive licenses will likely never know the full impact of their software (for good or evil) throughout the world.

<!---
Publish: yes
Pinned: no
Topics: online learning
--->
