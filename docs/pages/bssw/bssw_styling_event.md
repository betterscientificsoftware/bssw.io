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

* **Location**: Use the physical location (City, State or City, Country) for in-person events and the term "online" for events being held online.  For hybrid events use the physical location "and online".
  	* *Example*: `Location: Knoxville, TN` OR `Location: Online` OR `Location: Knoxville, TN and online`
* **Event Website**: URL to the main event website.
  	* *Example*: `Event Website: https://us-rse.org/rse-hpc-2020`
* **Organizers**:  Name of the organizers (This field is usually used for webinars/tutorials/panels (and not for conferences/workshops))
  	* *Example*: `Organizers: Foo`
* **Dates for the Event**: We allow for flexibility while specifying dates for an event. Following are some general guidelines:
	* The website allows specifying multiple dates related to any given event.
	* Each date entry in the list is identified by a key, which serves as a label indicating the "type" of date in the events listing. Common examples include "Submission Deadline," "Survey Closing Date," and "Event Date" (referring to the date(s) of the event itself).
	* The [event listing](https://bssw.io/events) will continue to showcase the event until all scheduled dates have concluded. For instance, once the "Submission deadline" has passed, the same event will still appear in the listing for "Event Dates" or any other relevant dates until the entire schedule is completed.
 	* The website will present all pertinent dates in the deck section of individual events. However, in the event listing, only the upcoming label and date will be visible.
  	* The site accommodates both start/end date ranges and multiple dates separated by semicolons.
	* Date ranges may occur, and in such instances, redundant display of the same month and year is eliminated wherever feasible. When an event spans across months, the month is specified for each date, while the year is mentioned only once. In cases where an event spans multiple years, both the months and years are indicated.
	* Site allows flexibility in how to label the dates. All labels are case insensitive. 
	* Label names with earlier start date are considered and if there is a duplicate label name with later start date, it is ignored.
	* The label "Event date" holds a distinct significance in its parsing. It indicates the timing of the main event and is typically (though not always) presented as the initial date in the individual event post. The author has the option to specify either "Event date" or "Event dates" in the source, and both are treated equivalently. If the "Event date/Event dates" label has a singular date as its value, the site will exhibit the label name "Event date" in both the event listing and individual event post. In the case of a date range, the site will showcase the label name "Event dates" in both the event listing and individual event post.
	*  In the individual event post, the labels and dates are displayed in ascending order, _usually_. Sometimes "event date/event dates"  is displayed first (unclear is what circumstances, will be debugged later).
	* Any new labels where value is not a date are ignored.
   	* Internally, the site applies a [date parsing library](https://github.com/mojombo/chronic) for dates.
 
	Following are some examples:

	1. When an event happens on one specific date and there are no other dates/deadlines in the event source file.
	     * *Example*: `Event Dates: February 16, 2023`
	     * See  event *2023 ECP Community BOF for BSSw Fellowship*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/2023-02-ECP23-BOF-BSSw-fellowship.md) | [BSSw.io](https://bssw.io/events/2023-ecp-community-bof-for-bssw-fellowship)
	   
	2. When an event is spanning a date range:
		* *Example*: `Event Dates: February 26 - March 3, 2023`
		* See  event *SIAM CSE23 Software-Related Events*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/2023-02-siam-cse23.md) | [BSSw.io](https://bssw.io/events/siam-cse23-software-related-events). The [BSSw.io event listing page](https://bssw.io/events) will display the label and date range.
  	          
	3. When the same event occurs periodically OR on multiple non-consecutive days, enter each date specifically as shown below:
		* *Example*: `Event Dates: Apr 20, 2023; May 18, 2023; Jun 15, 2023; Jul 20, 2023; Aug 17, 2023; Sep 21, 2023;`
		* See  event *Leadership Scientific Software Town Hall Meetings (Series)*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/LeadershipScientificSoftwareTownHallMeetings.md) | [BSSw.io](https://bssw.io/events/leadership-scientific-software-town-hall-meetings-series)
           
	5. An event may have different types of deadlines.  Some common deadline could be `Closing Date` for surveys, or `Submission Deadline` for registration, `Abstract Deadline` for abstracts.
		* *Example*: See  event *United States Research Software Engineer Association Conference 2023 (US-RSE'23)*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/2023-usrse-conf.md) | [BSSw.io](https://bssw.io/events/united-states-research-software-engineer-association-conference-2023-us-rse-23).
		

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

   * *Research Software Engineers in HPC Workshop (RSE-HPC-2020)*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/Workshop.RSE-HPE2020.md) | [BSSw.io](https://bssw.io/events/research-software-engineers-in-hpc-workshop-rse-hpc-2020)
   * *2021 International Workshop on Software Engineering for Computational Science (SE4Science'21)*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/Workshop.SE4Science21.md) | [BSSw.io](https://bssw.io/events/2021-international-workshop-on-software-engineering-for-computational-science-se4science-21)

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
    
   * *Webinar: Testing and Code Review Practices in Research Software Development*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/hpcbp-044-testingpractices.md) | [BSSw.io](https://bssw.io/events/webinar-testing-and-code-review-practices-in-research-software-development)
   * *Strategies for Working Remotely: Making the transition to virtual software teams*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/main/Events/panel.RemoteWorking0520.md) | [BSSw.io](https://bssw.io/events/strategies-for-working-remotely-making-the-transition-to-virtual-software-teams)

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

## Citations/References

Event articles should **not** use more formal citations/references documented in the [common citations/references section](bssw_styling_common.html#citationsreferences).

## Updating Past events
Past events may be updated with information pointing to where the presentation or recording archives have been stored. In such updates, you can add rows to the table above or modify the information as needed.

<!--
## QUESTIONS
1. When we add archive information, do we want to state "UPDATED: With presentations, pdf etc etc.", right on the top of the page below the deck? Or is that not needed?
-->

{% include links.html %}
