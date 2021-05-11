# Performing the Requirements Engineering Process (INCOMPLETE ARTICLE UNPUBLISHED)
<!-- deck text start --> 
This short article talks about how the requirements process can be carried out in the context of a scientific software development project.
<!-- deck text end --> 

#### Contributed by [Reed Milewicz](https://github.com/rmmilewi)
#### Publication date: August 06, 2019

How should the requirements process be carried out in the context of a scientific software development project? A review of the literature suggests three trends of interest:

- Scientific software tends to be exploratory. Many key requirements may be unknown at the start.
- It is often long-lived. It is likely that the requirements will change over time. 
- Software developed for the broader community has frequently come out of smaller projects intended for internal use. Therefore, stakeholders can change, and with them, the requirements. 

Because of these factors,  the requirements process should be thought of not as a singular event but as an ongoing activity that spans the lifecycle of the product. We outline here the activities involved and show how they can be realized for a hypothetical scientific software product.

## Case Study: LIGRE

We consider the case of a hypothetical future software project, LIGRE, a next-generation subsurface modeling code designed to support colonization operations on Mars. The LIGRE team comprises a diverse US-EU coalition, including engineers, physicists, and planetary geologists, and draws funding and support from numerous sources, such as space agencies (e.g., NASA, ESA), fundamental research organizations (e.g., NSF, ERC), university partners, and private industry. The main objective of LIGRE is to improve our understanding of the Martian subsurface in order to facilitate future human habitation. This includes identifying underground sources of water, ore lodes, and lava tube formations. These, among other factors, will be used to select suitable landing zones. In addition, LIGRE serves broader objectives of scientific discovery, to better understand the Universe and our place in it as human beings.

The primary investigatory tool of LIGRE is ground-penetrating radar (GPR) tomography. A transmitter emits pulsed electromagnetic energy that propagates through the subsurface. As the wave field encounters objects along the way, varying amounts of the energy are absorbed, pass through, or are reflected back to a receiver. Various instruments are used to collect this data, namely, GPR satellites (MARSIS, SHARAD) and rover-based subsurface radar (RIMFAX), each providing samples at different resolutions and depths. Because the attenuation of the wave field is strongly influenced by the material properties of the subsurface objects (e.g., permittivity, conductivity, resistivity), LIGRE must also integrate complex, a priori information about the Martian lithosphere: surface and borehole samples, analog experiments on Earth, and geological simulations. 

In the run-up to the LIGRE project, relevant agencies put together a workshop on topics related to Mars exploration, convening knowledgeable experts (including some of the future LIGRE team members) to share their ideas. The workshop resulted in a 30-page report that outlined the expert consensus and recommended short- and long-term goals for future Mars missions. Taking these recommendations into consideration and having allocated generous funding from various national governments, the agencies synthesized and integrated the findings into a call for proposals. After weeks of organizing and many sleepless nights, the LIGRE team submitted a proposal. The project was approved.

At this point, time and talent have been allocated, and all that remains is to actually do the work. That is easier said than done:

- Given the complex, interdisciplinary nature of the task, it is guaranteed that no one person fully understands what is needed to realize the software. 
- Different funding sources have competing interests in the product. Some expect highly performant software delivered on time to provide decision support. Others are more interested in having reusable software components to enable future research activities.
- The software is expected to be a keystone analysis product for the Mars mission. Hence, the software likely will need to be extended and repurposed to meet mission objectives as the situation on the ground evolves.

We will walk through the various stages of the requirements process as it applies to the LIGRE project.

### Requirements Elicitation

The **requirements elicitation** step consists of seeking out and discovering the needs and wants of stakeholders. What this means for scientific software may not at first be obvious. In conventional software development contexts, a goal of elicitation is to cultivate an understanding of the application domain; but in the case of scientific software, the developers are often domain experts themselves. As both producers and consumers of knowledge generated by the software, developers often play a central role in driving the creation of requirements. That being said, software engineering praxis offers many elicitation tools and techniques that can be helpful here.

The first objective is to identify the stakeholders. A stakeholder can be anyone who has an interest in the project and its outcome. On a first pass, we can identify the people developing the software and those footing the bill. Realistically, however, the requirements for the software will be influenced by many different actors. For the LIGRE project, we can name several:

- The developers, including government researchers (staff, postdocs, and interns), university participants, and private contractors, who have an interest in realizing the software as a product and the software as a vehicle for research.
- The agencies funding the project, who must ensure that the software meets the objectives outlined in their grants. 
- End-user analysts who will make use of the software and who have a responsibility to provide guidance to leadership (e.g., directorates, policymakers).
- The broader research community, for whom the work will create new research and funding opportunities.
- Private industry, which has concurrent interests in Mars and beyond.
- Future space exploration teams, who will directly benefit from the data provided. 
- The general public, who will ultimately be paying for the software and for whose benefit the work is justified.

## Mini-series list
- [Overview of Requirements and Requirements Engineering](Part1-RequirementsAndRequirementsEngineering.md)
- [Understanding requirements](Part2-UnderstandingRequirements.md)
- [Writing requirements](Part3-WritingRequirements.md)
- [Understanding and Performing the requirements engineering process](Part4-UnderstandingPerformingRequirementsEngineering.md)

<!---
Publish: no
Topics: requirements
Pinned: no
RSS update: 2019-08-06
--->
