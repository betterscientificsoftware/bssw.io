Table of Contents
===============================
[Click to Return to HomePage Table of Contents](../../README.md)

[Click to Return to Content Style Guide main page](ContentStyleGuide.md)

### Events

## DECK
All BSSw.io resources have decks and the deck has two parts: (1) deck text and (2) deck attributes. Please see the following guidance for "Events" and their decks.

### Deck text
Deck text is usually a couple of lines about the event. See COMMON RULES section of this guide.

### Deck Attributes

**Mandatory deck attributes** that are part of deck for all BSSw.io content are listed below. Guidance, specific for "Events" for these common mandatory deck attributes is given below.

1. **Title**: This is the title of the event
* Please keep the title timeline-neutral. That means: do not include words like "Call for submissions" etc in the title. The reason being that this BSSw.io event may get updated with archives, videos at a later point. As of July 2020, the titles form a part of the URL and we do not want the URL to change over time.
* Title can include full event name as well as abbreviation in brackets:  *Example*: `The Research Software Engineers in HPC Workshop (RSE-HPC-2020)`

2. **Contributor name**: Please indicate the *name of the person* who has submitted this event for inclusion on the BSSw site. This should not be the person who is adding the event to the BSSw.io site but rather the person who submitted the event. If you have no contributor name, then use "BSSw.io team".
*Example1*: `#### Contributed by [Firstname Lastname](https://github.com/author-github-id "Firstname Lastname GitHub Profile")`
*Example2*: `#### Contributed by BSSw.io team`

3. **Topics**: Rules are the same across all BSSw.io content type for this deck attribute. See COMMON RULES section of this guide. For the sake of repetition, this field indicate the categories and their sub-topical areas that this event might belong to.  Please refer to the metadata tags section to set the topics. We set the "Topics" information in the meta-data portion of the event markdown raw file.

4. **Publication date**: Rules are the same across all BSSw.io content type for this deck attribute. See COMMON RULES section of this guide. For the sake of repetition, this is the date when this event information was published on the BSSw.io website. *Example*: `#### Publication date: MONTH-DD, YYYY`.

**Event Specific deck attributes** are shown right below the deck text. See COMMON RULES section of this guide. In the case of events, the event deck attributes consist of the following: event date, location, event website and possibly the names of the organizers of the event. Please note that these deck attributes are specific to events (in contrast to other types of BSSw.io content)

1. **Date**: Date or range of dates when the EVENT is taking place.
2. **Location**: Use the word "Virtual" or name of physical location
3. **Event Website**: URL to the main event website
4. **Organizers**:  Name of the organizers (This field is usually used for webinars/tutorials/panels (and not for conferences/workshops)

*Example:*
- `Date: November 16, 2020`
- `Location: Online`
- `Event Website: https://us-rse.org/rse-hpc-2020`


## BODY TEXT
### General Guidelines
1. In the body of the event, first level headings should start with `### ` heading format.
2. Please write the body text in "third person" even if you are copy-pasting it from somewhere. The BSSw.io team is not an organizer of most of these events, hence usage of third-person grammar is essential
3. If you do not plan to update the event in the future, refrain from adding text such as "TBD", "Coming soon". In such cases, please rephrase text to point to links where such information may be updated by the third-parties
4. Please add "The *current* deadline is ...." and "Please see event website for deadline updates" to your text where relevant. The BSSw.io site cannot track and keep updating new deadlines to the event. Use this kind of discretion for the text when you write.
5. As far as you can,  please point people to the main event website (and not to specific pages and links). Specific pages can change over time and cause broken links.
6. Avoid copying ALL details from the event website. Event websites have a lot of specific details which we don't have to provide on the BSSw.io website.

### Structure of the body text 
The usual sections of the body text for  *upcoming events* has three parts: (1) Short introduction, (2) Event table and (3) Additional information.

#### 1.  Short introduction 
This is text without any heading introducing the event

#### 2. Event table with details
This table exists to highlight important information about the event such as event date, deadlines, website, registration, archives. There is guidance for two types of tables: (1) conference/workshops/similar events, (2) webinars/tutorials/similar events.

##### CONFERENCES AND WORKSHOPS
Event Information | Details
:--- | :---			   
Event Name |` [Name of the event](URL), in conjunction with [Name](URL)`
Event Date and Time | yyyy-mm-dd hh:mm timezone Or yyyy-mm-dd - yyyy-mm-dd
Submission deadlines | yyyy-mm-dd, any short text. Add "Please see event website for deadline updates."
Website | URL
Registration and other Information|  URLs

##### WEBINARS, PANELS AND TUTORIALS
Event Information | Details
:--- | :---			   
Event Name | `[Name of the event](URL), in conjunction with [Name](URL)`
Presenter details | Firstname1 Lastname1 and Firstname2 Lastname2 and ..
Event Date and Time | yyyy-mm-dd hh:mm timezone Or yyyy-mm-dd - yyyy-mm-dd
Website | URL
Registration and other Information|  URLs, FREE (if the event does not charge any fees, then it should be highlighted)
Links to the Recordings and Archives  | [Please do not use words like TBD here]
		
Please add more rows to the table (if you absolutely must).

#### 3. Additional information
You can add additional information here. If you create sections, please remember to start your first level headings with `###`. Below is guidance for two types of events: (1) conference/workshops/similar events, (2) webinars/tutorials/similar events.

##### CONFERENCES AND WORKSHOPS
Usually the following information is added, but depending on the nature of the event, more information can be added
`### Description` : Description of the workshop
`### Program Topics`:  topics covered in the workshop

##### WEBINARS, PANELS AND TUTORIALS
Usually the following information is added and is usually sufficient
`### Abstract` : A section with the abstract of the talk to be presented
`### Author Bios`:  A section with the author bios


## PAST EVENTS
Past events may be updated with information pointing to where the presentation, recording archives have been stored. In such updates, you can add rows to the table above or modify the information as needed.

## QUESTIONS
1. When we add archive information, do we want to state "UPDATED: With presentations, pdf etc etc.", right on the top of the page below the deck? Or is that not needed?



<!---
   Publish: no
---!>
