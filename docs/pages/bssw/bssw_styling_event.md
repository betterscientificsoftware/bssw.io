---
title: Event Styling Specific Guidelines
sidebar: bssw_sidebar
permalink: bssw_styling_event.html
---

## Introduction

All GitHub file names for BSSw.io articles should follow the naming conventions laid out [here](https://betterscientificsoftware.github.io/bssw.io/bssw_file_naming.html).

An "Event" content is a very brief article that highlights an event. An event article can highlight the following 2 types of resources: 
(1) Submission-based Events (Conferences/Workshops/Others), 
(2) Non-submission based Events (Webinars/Panels/Tutorials/Others).

The main part of the event article consists of the (1) *Deck*, (2) *Main body* and (3) *Metadata*. A event article must follow the below style guidelines. 

## Deck Section
All BSSw.io resources have a deck at the start of the article. The deck has two parts: (1) deck text and (2) deck attributes. Following is guidance for "events" and their decks.

### Deck text
Deck text is usually a couple of lines about the event. No images are allowed in the event deck. Please keep the deck text timeline-neutral. That means: do not include words like “call for submissions”, "invited to submit" etc in the deck text. For all other guidance on the deck text, please refer to the [common styling section](bssw_styling_common.html) of the guide.

### Deck Attributes

**Mandatory deck attributes** are part of deck for all BSSw.io content. Following is some guidance, specific to the mandatory deck attributes of event articles.
* **Deck title**: This is the title of the event. In addition to guidelines from the [common styling section](bssw_styling_common.html) of the guide, please also note the following:
	* Please keep the title timeline-neutral. That means: do not include words like "Call for submissions" etc in the title. The reason being is that this BSSw.io event may get updated with archives, videos at a later point. As of Dec 2020, the titles form a part of the URL and we do not want the URL to change over time.
	* Title can include full event name as well as abbreviation in brackets:  
	   * *Example*: `The Research Software Engineers in HPC Workshop (RSE-HPC-2020)`

* **Contributor name**: In addition to guidelines from the [common styling section](bssw_styling_common.html) of the guide, please also note the following:
	* Please indicate the *name of the person* who has **submitted** this event for inclusion on the BSSw site. This should not be the person who is adding the event to the BSSw.io site but rather the person who submitted the event. If you have no contributor name, then use "BSSw.io team". 
		* *Example*: `#### Contributed by BSSw.io team`

* **BSSw Topics**: See [common styling section](bssw_styling_common.html) of the guide.

**Event-specific deck attributes** are seen right below the deck text. These event deck attributes customize different parts of the deck for the event content type.

* **Date**: One can choose to enter the date or range of dates of the submisison deadline or event date.
* **Location**: Use the word "Virtual" or name of physical location
* **Event Website**: URL to the main event website
* **Organizers**:  Name of the organizers (This field is usually used for webinars/tutorials/panels (and not for conferences/workshops))

Example:
   * `Date: November 16, 2020` OR `Date: July 21, 2020 - July 23, 2020`
   * `Location: Online`
   * `Event Website: https://us-rse.org/rse-hpc-2020`
   * `Organizers: Foo`


## Main Body Section
### General Guidelines
1. In the body of the event, first level headings should start with `### ` heading format.
2. Please write the body text in "third person" even if you are copy-pasting it from somewhere. The BSSw.io team is not an organizer of most of these events, hence usage of third-person grammar is essential.
3. If you do not plan to update the event in the future, refrain from adding text such as "TBD", "Coming soon". In such cases, please rephrase text to point to links where such information may be updated by the third-parties.
4. Please add "The *current* deadline is ...." and "Please see event website for deadline updates" to your text where relevant. The BSSw.io site cannot track and keep updating new deadlines to the event. Use this kind of discretion for the text when you write.
5. As far as you can,  please point people to the main event website (and not to specific pages and links). Specific pages can change over time and cause broken links.
6. Avoid copying ALL details from the event website. Event websites have a lot of specific details which we don't have to provide on the BSSw.io website.

### Structure of the main body
The usual sections of the body text for  *upcoming events* has three parts: (1) Short introduction, (2) Event table and (3) Additional information.

#### 1.  Main body introduction
This is text without any heading introducing the event.

#### 2. Event table declaration
This table exists to highlight important information about the event such as event date, deadlines, website, registration, archives. Given below is guidance for two types of tables. Please note that most of the BSSw.io event content can be covered by either of these two tables.
(1) Submission-based events such conference/workshops/similar events. For submission-based events, we add submission deadline information in the table. 
(2) Non-submission based events such as webinars/tutorials/similar events. For non-submission based events, we add presenter and presentation details.
 
##### Submission-based Events (Conferences/Workshops/Others)

Event Information | Details
:--- | :---			   
Event Name |`[Name of the event](URL), in conjunction with [Name](URL)`
Event Date and Time | MONTH dd, yyyy hh:mm timezone Or MONTH dd, yyy - MONTH dd, yyyy
Website | URL
Submission deadlines | MONTH dd, yyyy, any short text. Add "Please see event website for deadline updates."
Registration and other Information| URL
Links to the Recordings and Archives  | Please do not use words like TBD here; please add this row only if you know that there are archives available.

Examples include the following, listed with both GitHub.com and BSSw.io links:

   * *Research Software Engineers in HPC Workshop (RSE-HPC-2020)*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/Events/Workshop.RSE-HPE2020.md) | [BSSw.io](https://bssw.io/events/research-software-engineers-in-hpc-workshop-rse-hpc-2020)
   * *2021 International Workshop on Software Engineering for Computational Science (SE4Science'21)*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/Events/Workshop.SE4Science21.md) | [BSSw.io](https://bssw.io/events/2021-international-workshop-on-software-engineering-for-computational-science-se4science-21)

##### Non-submission based Events (Webinars/Panels/Tutorials/Others)

Event Information | Details
:--- | :---			   
Event Name | `[Name of the event](URL), in conjunction with [Name](URL)`
Event Date and Time | yyyy-mm-dd hh:mm timezone Or yyyy-mm-dd - yyyy-mm-dd
Website | URL
Presenter details | Firstname1 Lastname1 and Firstname2 Lastname2 and ..
Registration and other Information|  URLs, FREE (if the event does not charge any fees, then it should be highlighted)
Links to the Recordings and Archives  | Please do not use words like TBD here; please add this row only if you know that there are archives available.
		
Please add more rows to the table (if you absolutely must). Please do not add empty rows where information is not available.

Examples include the following, listed with both GitHub.com and BSSw.io links:
    
   * *Webinar: Testing and Code Review Practices in Research Software Development*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/Events/hpcbp-044-testingpractices.md) | [BSSw.io](https://bssw.io/events/webinar-testing-and-code-review-practices-in-research-software-development)
   * *Strategies for Working Remotely: Making the transition to virtual software teams*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/Events/panel.RemoteWorking0520.md) | [BSSw.io](https://bssw.io/events/strategies-for-working-remotely-making-the-transition-to-virtual-software-teams)

#### 3. Additional Information
You can add additional information in this section. If you create sections, please remember to start your first level headings with `###`.

##### Submission-based Events (Conferences/Workshops/Others)
Usually the following information is added, but depending on the nature of the event, more information can be added
* `### Description` : Description of the workshop
* `### Program Topics`:  Topics covered in the workshop

##### Non-submission based Events (Webinars/Panels/Tutorials/Others)
Usually the following information is added and is usually sufficient
* `### Abstract` : A section with the abstract of the talk to be presented
* `### Author Bios`: A section with the author bios

## Metadata Section
See [common metadata section](bssw_content_metadata.html) of the guide.

## Updating Past events
Past events may be updated with information pointing to where the presentation or recording archives have been stored. In such updates, you can add rows to the table above or modify the information as needed.

<!--
## QUESTIONS
1. When we add archive information, do we want to state "UPDATED: With presentations, pdf etc etc.", right on the top of the page below the deck? Or is that not needed?
-->

{% include links.html %}
