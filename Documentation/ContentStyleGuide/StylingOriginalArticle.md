Table of Contents
===============================
[Click to Return to HomePage Table of Contents](../../README.md)

[Click to Return to Content Style Guide main page](ContentStyleGuide.md)


# Styling for Original Articles

An original article can highlight the following 2 types of resources: (1) blogs, (2) short article

The following figure shows different parts of a original article.

![Parts of an event article: UPDATE PLEASE](https://github.com/betterscientificsoftware/images/blob/master/documentation-cc-example.jpg)

The main part of the original article consists of the (1) Deck, (2) Main body of the article and (3) Metadata. The following sections describe the structure and various parts of such an article.

A original article must follow the below style guidelines. There are several examples available in the [betterscientificsoftware.github.io repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io) to use as a starting point.


## DECK
As we know, all BSSw.io resources have decks and the deck has two parts: (1) deck text and (2) deck attributes. Following is guidance for "original articles" and their decks.

### Deck text/image
Original articles may have deck text or deck images. Deck text is usually a couple of lines about the event. Deck images creation is out-sourced by the BSSw.io team (for now). They are however added to articles, only after approval has been obtained from the authors.
 * Blogs *usually* have deck images and no deck text. 
 * Short articles *usually* have deck text. For guidance on the deck text, please see [common layout section](CommonLayout.md) of the guide.

### Deck Attributes

**Mandatory deck attributes** that are part of deck for all BSSw.io content. Guidance, specific for "Events" for these common mandatory deck attributes is given below.

1. **Deck title**: This is the title of the event. In addition to guidelines from the [common layout section](CommonLayout.md) of the guide, please also note the following:
	* Please keep the title timeline-neutral. That means: do not include words like "Call for submissions" etc in the title. The reason being that this BSSw.io event may get updated with archives, videos at a later point. As of July 2020, the titles form a part of the URL and we do not want the URL to change over time.
	* Title can include full event name as well as abbreviation in brackets:  *Example*: `The Research Software Engineers in HPC Workshop (RSE-HPC-2020)`

2. **Contributor name**: In addition to guidelines from the [common layout section](CommonLayout.md) of the guide, please also note the following:
* Please indicate the *name of the person* who has submitted this event for inclusion on the BSSw site. This should not be the person who is adding the event to the BSSw.io site but rather the person who submitted the event. If you have no contributor name, then use "BSSw.io team". 
	* *Example1*: `#### Contributed by [Firstname Lastname](https://github.com/author-github-id "Firstname Lastname GitHub Profile")`
	* *Example2*: `#### Contributed by BSSw.io team`

3. **Deck Publication date**: There is no specific guidance for this for the event content type. See [common layout section](CommonLayout.md) of the guide.

4. **BSSw Categories**:  There is no specific guidance for this for the event content type. See [common layout section](CommonLayout.md) of the guide.

5. **BSSw Topics**: There is no specific guidance for this for the event content type. See [common layout section](CommonLayout.md) of the guide.

**Event Specific deck attributes** are seen right below the deck text. There are four deck attributes specific to events and are listed below. These event deck attributes customize different parts of the deck for the event content type.

1. **Date**: Date or range of dates when the EVENT is taking place.
2. **Location**: Use the word "Virtual" or name of physical location
3. **Event Website**: URL to the main event website
4. **Organizers**:  Name of the organizers (This field is usually used for webinars/tutorials/panels (and not for conferences/workshops)

*Example:*
- `Date: November 16, 2020`
- `Location: Online`
- `Event Website: https://us-rse.org/rse-hpc-2020`

## MAIN BODY
### General Guidelines
1. In the body of the event, first level headings should start with `### ` heading format.
2. Please write the body text in "third person" even if you are copy-pasting it from somewhere. The BSSw.io team is not an organizer of most of these events, hence usage of third-person grammar is essential
3. If you do not plan to update the event in the future, refrain from adding text such as "TBD", "Coming soon". In such cases, please rephrase text to point to links where such information may be updated by the third-parties
4. Please add "The *current* deadline is ...." and "Please see event website for deadline updates" to your text where relevant. The BSSw.io site cannot track and keep updating new deadlines to the event. Use this kind of discretion for the text when you write.
5. As far as you can,  please point people to the main event website (and not to specific pages and links). Specific pages can change over time and cause broken links.
6. Avoid copying ALL details from the event website. Event websites have a lot of specific details which we don't have to provide on the BSSw.io website.

### Structure of the main body
The usual sections of the body text for  *upcoming events* has three parts: (1) Short introduction, (2) Event table and (3) Additional information.

#### 1.  SHORT INTRODUCTION 
This is text without any heading introducing the event

#### 2. EVENT TABLE
This table exists to highlight important information about the event such as event date, deadlines, website, registration, archives. Given below is guidance for two types of tables: (1) conference/workshops/similar events, (2) webinars/tutorials/similar events. Most of the BSSw.io event content can be covered by these two tables. Major difference between in the tables: for deadline-based events, we add submission deadline information in the table and for events such as webinars, we add presenter details.
 
##### CONFERENCES AND WORKSHOPS
Event Information | Details
:--- | :---			   
Event Name |` [Name of the event](URL), in conjunction with [Name](URL)`
Event Date and Time | yyyy-mm-dd hh:mm timezone Or yyyy-mm-dd - yyyy-mm-dd
Website | URL
Submission deadlines | yyyy-mm-dd, any short text. Add "Please see event website for deadline updates."
Registration and other Information| URL
Links to the Recordings and Archives  | Please do not use words like TBD here; please add this row only if you know that there are archives available.

##### WEBINARS, PANELS AND TUTORIALS
Event Information | Details
:--- | :---			   
Event Name | `[Name of the event](URL), in conjunction with [Name](URL)`
Event Date and Time | yyyy-mm-dd hh:mm timezone Or yyyy-mm-dd - yyyy-mm-dd
Website | URL
Presenter details | Firstname1 Lastname1 and Firstname2 Lastname2 and ..
Registration and other Information|  URLs, FREE (if the event does not charge any fees, then it should be highlighted)
Links to the Recordings and Archives  | Please do not use words like TBD here; please add this row only if you know that there are archives available.
		
Please add more rows to the table (if you absolutely must). Please do not add empty rows where information is not available.

#### 3. ADDITIONAL INFORMATION
You can add additional information here. If you create sections, please remember to start your first level headings with `###`. Below is guidance for two types of events: (1) conference/workshops/similar events, (2) webinars/tutorials/similar events.

##### CONFERENCES AND WORKSHOPS
Usually the following information is added, but depending on the nature of the event, more information can be added
* `### Description` : Description of the workshop
* `### Program Topics`:  Topics covered in the workshop

##### WEBINARS, PANELS AND TUTORIALS
Usually the following information is added and is usually sufficient
* `### Abstract` : A section with the abstract of the talk to be presented
* `### Author Bios`: A section with the author bios

## METADATA SECTION
There is no specific guidance for this for the event content type. See [common layout section](CommonLayout.md) of the guide.

## UPDATING PAST EVENTS
Past events may be updated with information pointing to where the presentation, recording archives have been stored. In such updates, you can add rows to the table above or modify the information as needed.

## LINKS TO EXAMPLES IN BSSW.IO GITHUB FOR *EVENTS* CONTENT TYPE
TBD

## QUESTIONS
1. When we add archive information, do we want to state "UPDATED: With presentations, pdf etc etc.", right on the top of the page below the deck? Or is that not needed?

## ORIGINAL BLOG STUFF

### Blog Articles

All text under blog articles is taken from the old blog guide. The text needs to be reviewed and corrected.

#### Publication and Announcements
Blog articles appear here: https://bssw.io/blog_posts and also are announced on the [BSSw email digest](https://bssw.io/pages/receive-our-email-digest) (monthly).

#### Length
General guidance is 250-500 words, though this is flexible (some articles have been shorter, some a bit longer). 

#### Source Format
We use [Github-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for blog article markup.  However we'll work with you at accept other formats.

A skeleton Markdown template for a blog article, which you can copy and customize is available at https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/Articles/Blog/BlogArticleSkeletonA.md

You can provide a pull request for the article in the appropriate directory of the repository: https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/Articles/Blog

If you prefer to use another format, you can email the draft to the editor you've been dealing with.

##### Detailed Formatting Tips
 - The formatting to include a hero image is a bit finicky.
   - The `**Hero Image:**` tag must be followed by a blank line
   - The image itself must be in a Markdown list item (that is, it starts with `-`)
 - Positioning of the hero image relative to the contributor and publication date metadata doesn't matter
 - Having a deck and having a hero image in a blog post are mutually exclusive
   - A way to approximate having both is to have the hero image and then put the deck as your first (short) paragraph after the image and italicize it.
 - `#### Publication date:` is case sensitive (`d` in particular)

#### Employer Approval
If your employer requires an internal review and approval process prior to publication, please let us know.

#### Content
##### General

*Need to say something here*

##### Links, and References
We encourage you to point to a modest numder of additional resources that enhance your article.  Too many links tend to distract readers.  In most cases, we would like to have the items you refer to in BSSw.  These would usually be what we call "curated content", which means short items that provide a pointer to an extenral resource with a short description.  You're welcome to prepate those as separate contributions, and we're happy to help.

##### Images
*Need to say something about what kind of images we want to encourage/discourage and point to writeup of how to deal with images in the other repo.*


<!---
   Publish: no
---!>
