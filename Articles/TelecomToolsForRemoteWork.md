# Virtual Meeting Tools and Features for the HPC/CSE Community

<!--- deck start --->
Are you familiar with virtual meeting tools and what features they offer? This article explores popular tools such as *Zoom* and *WebEx meetings*.
<!--- deck end --->

*The information provided here will be periodically updated to
include either more products or more features. Please also note
that features (mentioned below) for the products are valid currently;
but vendors may change these features in the future. This article
may be considered a starting point for you to start investigating
these tools and their features.*

There is a wide array of [Teleconferencing](https://en.wikipedia.org/wiki/Teleconference)
products. Many vendors offer products for *virtual meetings*. However, vendors
also tend to distinguish virtual *meetings* from other modalities of video
telecommunications such as *teams*, *trainings*, *webinars*, and *webcasts*.
Typically, vendors offer a line of *different* products for each purpose.
Features of interest may not all exist in a single product. In addition, there
is also a wide variety of features among virtual meeting products.

Next, many vendors offer *enterprise* licensing for large organizations. If
a given product is available to you through your organization, the features
of interest may be constrained by how your organization chooses to configure
and deploy the product to its employees.

All of this complicates navigating and comparing the available products and
their features. This article is not meant to cover everything. Here, we focus
only on virtual meeting products and those features likely to be relevant to
the HPC/CSE community in a work-at-home (small to medium scale) setting *and*
which have some degree of variability in support across vendors.

In the table below...

* We've tried to provide as many links as possible to information relevant to 
  a given feature.
* *Partial* means some support for the feature exists but not at the level of
  support one would expect.
* *Maybe* means the feature may exist depending on other factors outside of
  the typical user's control.
* Numbered footnotes are links to additional information.
* Lettered footnotes
   * <sup>X</sup>Indicates a feature is available in another of the vendor's products.
   * <sup>Y</sup>Indicates a feature can vary depending on your organization's configuration.
* Abbreviations have balloon hints which are revealed by hovering the mouse over them.
* [TBD] means to be done.

Feature | [Zoom](https://www.zoom.us) | [WebEx Meetings](https://www.webex.com)<sup>[a](#webex-notes)</sup> 
--- | --- | ---
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**The Basics**](#the-basics)</td></tr>
[Free Plan](#free-plans) | [Yes](https://zoom.us/pricing) | [Yes](https://www.webex.com/pricing/index.html) 
[Plan Pricing<br>$/mo/host](#plan-pricing) | 0/15/20 | 0/15/20/30 
[Size Limit](#size-limits) | 100-1000<sup>[a](#zoom-notes)</sup> | 50-200<sup>[b](#webex-notes),[c](#webex-notes)</sup> 
[Length Limit](#length-limits) | &le;24h<sup>[b](#zoom-notes)</sup> | &le;24h 
[Join Device](#supported-devices) | [A]/[W]/[M]/[L] | [A]/[W]/[M]/[L]/[VCS](https://help.webex.com/en-us/7yxpa9/Join-a-Webex-Meeting-from-a-Video-System)
[No Install<br>option](#no-install-option) | [Partial](https://support.zoom.us/hc/en-us/articles/214629443-Zoom-web-client)<sup>[c](#zoom-notes)</sup> | [Partial](https://help.webex.com/en-us/ozygebb/Join-a-Cisco-Webex-Meeting#Join-a-Meeting-from-the-Webex-Meetings-Desktop-App-or-Mobile-App)<sup>[e](#webex-notes)</sup>
[HD Video](#high-definition-video) | No | [Maybe](https://help.webex.com/en-us/fw8u4j/Webex-Video-Support)
[Test Meeting](#test-meeting) | [Yes](https://zoom.us/test) | [Yes](https://www.webex.com/test-meeting.html) | [Yes](https://bluejeans.com/111/) | [Partial](https://ucstatus.com/2019/06/26/how-to-place-a-test-call-in-microsoft-teams/) | [Yes](https://support.goto.com/meeting/help/join-a-test-session-g2m050001) | [Partial](https://www.businessinsider.com/how-to-test-skype-video)
[Free Dial-in option](#free-dial-in-option) | [Maybe](https://support.zoom.us/hc/en-us/articles/201362663-Joining-a-meeting-by-phone) | [Maybe](https://help.webex.com/en-us/WBX25713/How-Do-I-Find-the-Global-Dial-In-Number-for-My-Meeting)
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Content Sharing**](#content-sharing)</td></tr>
[Screen Sharing](#screen-sharing) | [Yes](https://support.zoom.us/hc/en-us/articles/201362153-Sharing-your-screen) | [Yes](https://help.webex.com/en-us/i62jfl/Share-Your-Screen-or-Application-in-a-Cisco-Webex-Teams-Meeting)
[App Sharing](#app-sharing) | [Yes](https://support.zoom.us/hc/en-us/articles/115005706806-Using-annotation-tools-on-a-shared-screen-or-whiteboard) | [Yes](https://help.webex.com/en-us/utfx63/Share-an-Application-in-Cisco-Webex-Meetings)
[Shared Whiteboard](#shared-whiteboard) | [Yes](https://support.zoom.us/hc/en-us/articles/205677665-Sharing-a-whiteboard) | [Yes](https://help.webex.com/en-us/5ddww5/Share-Content-in-Cisco-Webex-Meetings-and-Cisco-Webex-Events)
[Shared Annotations](#shared-annotations)  | [Yes](https://support.zoom.us/hc/en-us/articles/115005706806-Using-annotation-tools-on-a-shared-screen-or-whiteboard) | [Yes](https://help.webex.com/en-us/hc3tig/Options-Available-on-the-Annotate-Toolbar-in-the-Cisco-Webex-Meetings-Suite)
[Able chat](#able-chat) | [Yes](https://support.zoom.us/hc/en-us/articles/203650445-In-Meeting-Chat)<sup>[d](#zoom-notes)</sup> | [TBD]
[Polling/Voting](#voting-or-polling) | [Yes](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) | [Yes](https://help.webex.com/en-us/n0pdj9x/Start-a-Poll-in-Cisco-Webex-Meetings) | [Partial](https://support.bluejeans.com/s/article/Event-Polling) | [Yes](https://support.office.com/en-us/article/create-a-poll-in-microsoft-teams-a3f9112c-01e1-4ee4-bd88-25e4e243b80b) | No | [Yes](https://support.microsoft.com/en-us/office/take-a-poll-in-a-skype-for-business-meeting-6eb1fb85-18a6-422c-ae48-55519841f296?ui=en-us&rs=en-us&ad=us)
[File sharing](#file-sharing) | [Maybe](https://support.zoom.us/hc/en-us/articles/209605493-In-Meeting-File-Transfer#h_35f5965f-bae8-49b2-a1a9-8956fb8022ff) | [Yes](https://help.webex.com/en-us/5ddww5/Share-Content-in-Cisco-Webex-Meetings-and-Cisco-Webex-Events)
[Recording](#recording) | [Yes](https://support.zoom.us/hc/en-us/sections/200208179-Recording) | Maybe<sup>[g](#webex-notes)</sup>
[Transcription](#transcription) | [Yes](https://support.zoom.us/hc/en-us/articles/115004794983-Automatically-Transcribe-Cloud-Recordings-) | [TBD]
[Closed captioning](#closed-captioning) | [Partial](https://support.zoom.us/hc/en-us/articles/207279736-Getting-started-with-closed-captioning) | [Maybe](https://www.webex.com/ai-assistant.html)<sup>[h](#webex-notes)</sup>
[Live Streaming](#live-streaming) | Maybe<sup>[e](#zoom-notes)</sup> | [Yes](https://help.webex.com/en-us/n97pcak/Live-Stream-Your-Webex-Meetings)
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Compatibility**](#compatibility) (hover for details, [**recommended in bold**](#recommended))</td></tr>
Windows Desktop |[8]/[10h]/[10p] | [8]/[10h]/[10E]
Linux Desktop | [U]/[D]/[C]/[R]/[O]/[F]/[+][+z] | [U]/[R]/[O]/[F]
macOS Desktop | [&ge;10.7][osx] | [&ge;10.13][osx]
Presenter Browser | **[Ch]**/[Ed] | **[Ch]**/**[Fi]**/[Sa]
Attendee Browser | **[Ch]**/[Ed]/[Fi]/[Sa] | **[Ch]**/**[Fi]**/[Sa]
Presenter Mobile | [And]/[iOS] | [And]/[iOS]
Attendee Mobile | [And]/[iOS] | [And]/[iOS]
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Security**](#security)</td></tr>
[Recent Issues](https://www.google.com/search?q=security+issues+with+video+conferencing+software&as_qdr=m) | [Yes](https://tidbits.com/2020/04/03/every-zoom-security-and-privacy-flaw-so-far-and-what-you-can-do-to-protect-yourself/) | No
[Best Practices](#best-practices) | [Yes](https://zoom.us/security) | [Yes](https://help.webex.com/en-us/8zi8tq/Cisco-Webex-Best-Practices-for-Secure-Meetings-Hosts)
[Lock Meeting](#lock-meeting) | [Yes](https://blog.zoom.us/wordpress/2014/06/03/spotlight-security/) | [Maybe](https://help.webex.com/en-us/zcvgyc/Webex-Teams-Lock-or-Unlock-Your-Meeting)
[Expel Attendee](#expel-attendee) | [Yes](https://blog.zoom.us/wordpress/2014/06/03/spotlight-security/)|[Partial](https://help.webex.com/en-us/WBX30745/How-Do-I-Expel-a-Meeting-Participant)<sup>[d](#webex-notes)</sup>
[Expel Recovery](#expel-recovery) | [Yes](https://support.zoom.us/hc/en-us/articles/360021851371-Allowing-Removed-Participants-or-Panelists-to-Rejoin) | Yes
[Privacy](#privacy) | [Partial](https://tidbits.com/2020/04/03/every-zoom-security-and-privacy-flaw-so-far-and-what-you-can-do-to-protect-yourself/) | [Yes](https://trustportal.cisco.com/c/dam/r/ctp/docs/privacydatasheet/collaboration/cisco-webex-meetings-privacy-data-sheet.pdf)
[E2E Encryption](#e2e-encryption) | [No](https://citizenlab.ca/2020/04/move-fast-roll-your-own-crypto-a-quick-look-at-the-confidentiality-of-zoom-meetings/) | Maybe<sup>[f](#webex-notes)</sup>
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Advanced Features**](#advanced-features)</td></tr>
[Personal rooms](#personal-rooms) | |
[Breakout rooms](#breakout-rooms) | [Yes](https://support.zoom.us/hc/en-us/articles/206476093-Getting-Started-with-Breakout-Rooms) | [Partial](https://help.webex.com/en-us/8cckd2/Manage-Breakout-Sessions-in-Cisco-Webex-Training) 
[Virtual background](#virtual-background) | [Yes](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background?_ga=2.14223487.938856509.1585291308-953848128.1583382933&_gac=1.183383508.1583390141.Cj0KCQiAwP3yBRCkARIsAABGiPpO0S3qoN8PTc0qdsQBTPiskm6O520ASHcVcXL8kVvTc5O-VTr0XPIaArGGEALw_wcB)<sup>[f](#zoom-notes)</sup> | [Parial](https://help.webex.com/en-us/80jduab/Webex-Meetings-Change-Your-Video-Background)<sup>[i](#webex-notes)</sup>
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">**Convenient Host Features**</td></tr>
[Mute all A/V](#mute-all) | [Yes](https://support.zoom.us/hc/en-us/articles/203435537-Mute-All-And-Unmute-All)/No | [Yes](https://help.webex.com/en-us/n94aj5j/Mute-or-Unmute-in-Cisco-Webex-Meetings-Suite)/[Yes](https://help.webex.com/en-us/nylc718/Turn-off-Participants-Video-in-Webex-Meetings-and-Webex-Events)
[Mute A/V entry](#mute-on-entry) | [Yes](https://support.zoom.us/hc/en-us/articles/115005756143-Changing-your-meeting-settings)/No | [Yes](https://help.webex.com/en-us/n94aj5j/Mute-or-Unmute-in-Cisco-Webex-Meetings-Suite)/No
[Disable entry/exit<br>sounds](#disable-chimes) | Yes | Yes
[Attendee count](#attendee-count) | Yes | No
[Host exit wont<br>end meeting](#host-exit-wont-end-meeting) | [Partial](https://support.zoom.us/hc/en-us/articles/201362573-Pass-Host-Controls-and-Leave-the-Meeting) | [Partial](https://help.webex.com/en-us/WBX000023799/A-Host-Only-has-the-Option-to-End-Meeting-when-Leaving-a-Web-Meeting-the-Audio-Conference-Ends)
[Exceed size<br>notification](#exceed-size-notification) | [TBD] | [TBD]
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Experiences in actual use (subjective)**](#experiences-in-actual-use)</td></tr>
Max. size | [TBD] | 650
Years of use | [TBD] | 5
Reliability | Good | Good
Usebility | Excellent |  Good
A/V quality | [TBD] | [TBD]
[Technical project<br>meetings](#technical-project-meetings) | Good | Excellent
[Hands-on<br>trainings](#hands-on-trainings) | [TBD] | [TBD]
[Pair<br>programming](#pair-programming) | Excellent | Excellent
[Interviewing](#interviewing) | [TBD] | [TBD]
[Hack-a-thons](#hack-a-thons) | [TBD] | [TBD]
[Virtual water<br>cooler](#virtual-water-cooler) | [TBD] | [TBD]

## The Basics

### Free plans

Most vendors offer a *free* plan. However, these typically come with length and/or
size limitations. In response to the current pandemic situation, some vendors have
either lowered prices of their paid plans or relaxed limitations of their free plans.

Simply *attending* another host's meeting does not typically require a user to purchase a
plan. However, recent security concerns in some products may cause some meeting hosts to
adjust their meeting's security settings such that users are required to have an *account*
with the vendor before logging in and this in turn may require users to obtain a plan even
if only the free one.

If you do need to *host* meetings *and* you do not already have a plan through your home
organization, the lowest-level paid plan in any of these products is probably sufficient
for most project's needs.

### Plan pricing

Most vendors charge monthly, *per host account* and then offer a few different plans
based on meeting size and plan features. In response to the current pandemic situation,
some vendors are offering discounts on their plans for a year-long purchase. In addition,
most vendors offer *enterprise* level accounts designed for large organizations with many
users each of which may require their own *host account*. 

### Size limits

The *maximum meeting size* is the maximum number of *participants* in a meeting. A
number of vendors draw a distinction between a *meeting*, which typically requires
participants to *interact* (e.g. speak, exchange chat messages, share content, etc.)
and other modalities of video telecommunications such as a *webinar* where the
majority of people are mere *attendees* who just need to hear and view content.
Some products offer two different limits; one on interactive *participants* and
another on listen/view-only *attendees*.

For *enterprise* products, the maximum meeting size may also depend on how your
organization's plan administrator has configured it.

Be aware that many people like to use an ordinary telephone<sup>[A]</sup> for the audio
part of the meeting and their computer for everything else. This is because ordinary
telephone audio (landline/cell) is often more reliable than
[VoIP-audio](https://en.wikipedia.org/wiki/Voice_over_IP). If their internet connection
fails during the meeting, they can still at least listen and speak.
This raises a couple of potential issues. First, there is no practical advantage in doing
this if the "telephone" the user calls in with is using a
[VoIP service](https://www.voip-info.org/voip-providers-usa/).
Next, when they do this and do not also *bind* the phone call connection together
*with* their computer connection, they wind up appearing to the system as two different
meeting participants taking up two slots. If a majority of participants wind up doing
this in a large meeting, it can reduce the effective size limit by almost a factor
of two.

What happens if a meeting exceeds its size limit? In most case, attempts to
join a meeting that is at its size capacity will be prevented. A key question
is if and how the host may be notified of this. At present, this behavior is
unclear.

### Supported devices

* [A] = Audio-only telephone device using landline, cell or VoIP.
* [W] = Web-browser device often using a browser-extension.
* [M] = Mobile device (phone or tablet) operating over the internet.
* [L] = Laptop or desktop computer device operating over the internet.
* [VCS] = Video Conferencing System with dedicated hardware/network.

### No install option

It can be convenient to provide your meeting participants with a way of attending that
does not require them to download or install any new software. This is typically possible
only if they connect through a web browser. Even then, some vendor's products may require
a browser extension to be downloaded. In addition, this approach also typically means
that such a participant has limited functionality. For example, they may not be able to
host a meeting as a presenter and share content from their browser.

### High definition video

So much of human interaction involves
[non-verbal cues](https://www.lifesize.com/en/video-conferencing-blog/speaking-without-words).
Poor video quality can dramatically reduce participant's ability to interpret non-verbal
cues. Among participants with long-standing, pre-existing, high-functioning relationships, the
ability to interpret non-verbal cues is
[not as essential](https://www.comptia.org/blog/the-art-of-non-verbal-communication-in-a-video-conferencing-world).
However, high definition (HD) video can be essential in other circumstances
particularly those where the people involved are meeting for the first time.

In the current pandemic situation, with so many being forced to work from home,
the increase in network load has caused some vendors to temporarily disable
support high definition video.

In addition, most vendor's products automatically adjust video quality based
on moment-to-moment network responsiveness anyway. Each participant's local
network and/or the wide-area network loads may be such that even if high
definition video is supported, the networks will not support it.

### Test meeting

For first time users, without actually participating in a meeting it can be difficult
to know of sure if the audio and video of your particular configuration will work with
the vendor's product. A test meeting is a useful way to test your particular setup to
ensure it works, at a basic level, with the vendor's software and service. You may not
be able to test all features but you should be able to test basic audio and video support.
Most vendors provide a *test meeting* for this purpose. Zoom provides a means to test
audio and video each time prior to connecting to a new meeting.

### Free dial-in option

For those who wish to connect audio via ordinary telephone (landline or cell), it can be
convenient to provide your meeting participants with a toll-free option. This feature may
be particularly important for international participants. While this feature is common
across many vendor's products, enabling it typically involves additional costs. However,
enterprise plans as part of your home organization may provide the feature.

## Content sharing

Virtual meeting tools provide a variety of features to allow meeting participants to
share content. In the absence of any one of these features, there are often acceptable
work-arounds using other, dedicated tools. For example,
[Google docs](https://www.google.com/docs/about/) can be used for some kinds of content
sharing even some limited whiteboarding,
[Google forms](https://www.google.com/forms/about/) can be used for polling attendees,
[Google hangounts](https://hangouts.google.com/) (now called *Google Meet*) can be
used for chat, etc.

### Screen sharing

This is a feature that allows the host/presenter to share everything on his/her screen
with all the participants. All teleconference tools support this feature even from 
mobile devices. However, a number of tools also support variations of this feature for
different needs. These are described below.

### App sharing

App (or Application) sharing is like [*Screen Sharing*](#screen-sharing) except that
the window(s) of only a single application (e.g. PowerPoint or Word) is shared. The
host/presenter is not forced to share their whole screen but can select only the
window(s) from a specific application to share. This can be useful in cases where the
host/presenter tends to have a lot of windows open and they want to keep the
participants from accidentally seeing the contents of those other windows. When you
have a choice, using application-specific sharing is a **best privacy practice**.

### Shared whiteboard

This is similar to but not quite the same thing as *Shared Annotations*. A shared
whiteboard is a separate drawing area, like a whiteboard in an office, where all
participants can doodle content and paste images they captured locally.

For some, a shared whiteboard is more than just a realization shared drawing area
where content is created by a mouse a keyboard. It includes the *integrations* necessary
to create content using a tablet & pen-based drawing gestures with touch sensitivity, etc.
No virtual meeting vendors provide such an experience in their shared whiteboard
features. In fact, there are few *dedicated* shared whiteboard solutions available
that work on all platforms that support tablet & pan-based drawing gestures.

### Shared annotations

This is similar to but not quite the same thing as [*Screen Sharing*](#screen-sharing).
Shared annotations allows the presenter/host to draw annotations on top of whatever
content is being displayed in the main window so that all other participants can see it.
In addition, some products allow *attendees* to also draw shared annotations.

### Able chat

All vendor's typically provide some kind of a chat feature which allows participants
to send text messages to each other. By *able* chat here, we mean the chat handles
more than just *raw* text. For example, an *able* chat handles cut-n-paste across
applications, clickable URL links, private messages between participants (instead
only to all participants), drag-n-drop for some file types, showing who else may be
in the midst of typing a chat message, the ability to save all chat messages to a
text file, and whether the host can disable chat if necessary.
In the absence of *able chat* a clumsy
but sufficient work-around is to use a shared [Google doc](https://www.google.com/docs/about/)
or [Google Hangout](https://hangouts.google.com/).
Of course, there is still the issue of how best to distribute a link to meeting participants,
probably via email.

### Voting or polling

This is a feature that allows the host to ask participants a question and have
them anonymously vote their responses. In the absence of this feature, a clumsy
but sufficient work-around is to use [Google forms](https://www.google.com/forms/about/) by 
creating the form and then pasting a link to the form in your meeting's chat
window allowing all participants to easily go there and vote their response.

### File sharing

File sharing allows participants to share whole files which attendees can then
download to their own systems. There are varying levels of support for this
among the products often restricted by file types (e.g. extensions). Some
vendor's provide support for scripts and even augmented reality files. File
sharing, especially executable scripts, may introduce additional security
concerns.

### Recording

Recording of a virtual meeting session is often convenient for participants
who were unable to attend to watch later or for a meeting scribe to go back
and fill in gaps in their notes. However, recordings are generally not useful
for *replacing* a scribe because of the summarization often involved in the
curation of meeting notes.

There are differing levels of support for what content gets recorded among the
various products. Some products may not make a record of chat messages for
example. It can sometimes be useful for the host to select the content to be
recorded (e.g. audio-only). Some vendors provide support for producing textual
*transcriptions* from recordings. Recordings can introduce
[*privacy concerns*](#privacy) so it is a best practice to obtain *written*
consent not only to create a recording but also to specify with whom the
recording may later be shared with.

### Transcription

Recorded sessions can be transcribed into time-stamped, text to make easy
searching of the recorded stream. Transcription typically requires about 2x
the recording time to complete and is typically available only for sessions
recorded to the *cloud* and pricier plans.

### Closed captioning

All vendors offer *some* support for closed captioning. Typically, the support
provided is just the *display* of captions. The *generation* of captions is
delegated to some other service. For example, a *live captioner* is a person who
transcribes the conversation in real-time during a meeting much like a court
stenographer. Those participants who wish can then enable display of closed
captions.

Some vendors appear to already provide or plan to provide *add-on* features
with automatic captioning.

### Live streaming

Some products offer the ability to stream a *live* session to platfroms like
YouTube or Facebook. Of course, this also means that the session will be
effectively be *recorded* but only on that platform.

## Security

Depending on the kind of information to be *processed* in a virtual meeting,
the level of security the product provides may or may not be an issue.

When security vulnerabilities of a given virtual meeting product are a
concern, one possible though inconvenient work-around is for
*all meeting participants* to be on the same
[*virtual private network (VPN)*](https://www.techradar.com/news/how-using-a-vpn-with-zoom-can-keep-you-and-your-data-more-secure). This adds significantly to the logistical
aspects of running a virtual meeting but may be the best option in
some circumstances.

### Recent issues

Recent security concerns in various virtual meeting products have been all
the rage in the mainstream media. Unfortunately, many sources lack the
technical background to provide any sort of *evaluation* of the level of
risk of any issues encountered with respect to the kinds of information
to be *processed*. When we have found technically competent sources, we
provide links to them here.

### Best Practices

For each product, when there is a collection of *best practices* for ensuring
the best possible level of security when using that product for a meeting we
indicate that here and provide a link to them.

### Lock Meeting

When a meeting is *locked*, that means it cannot be joined by any other
participants even with the correct credentials. Participants that leave
a locked meeting cannot re-join either.

### Expel Attendee

*Expelling* or *removing* an attendee is typically a power that only meeting
hosts have. It is important for hosts to know how to do this *quickly*. If for
some reason the meeting is *bombed*, quick action from the host can correct
the situation before it gets out of hand.

### Expel Recovery

In most products, an attendee is expelled, they cannot ever again rejoin that
meeting instance. They have to use a wholly different *identity* or email
address or. So, it is important for hosts to take care when taking the drastic
action of expelling an attendee. Some products do enable a host to *recover*
from this situation however allowing an inadvertently expelled attendee to
rejoin with the same identity.

### Privacy

[Privacy is related to but also distinct from security](https://www.hiv.gov/blog/difference-between-security-and-privacy-and-why-it-matters-your-program). While security is about safeguarding data
of any kind, privacy is specifically about safeguarding
[*personally identifiable information (PII)*](https://www.gsa.gov/reference/gsa-privacy-program/rules-and-policies-protecting-pii-privacy-act)
as well as a person's rights about how that information is managed by a third
party.

A potentially common privacy-related situation in virtual meeting settings is the
use of a product's *recording* feature. Doing so without consent of all parties
may create a significant
[breach of privacy laws](https://blog.clickmeeting.com/accordance-record-recording-consent-laws).
Making the recording available to a wider audience than attendees believe they
originally consented to may also create a privacy issue.

Another example is whether the system may
notify the host if an attendee has *changed application focus* away from the
virtual meeting application to something else. Such functionality might be
wholly appropriate for an elementary school teacher in a virtual classroom setting
needing to keep an eye on his students. However, if the same thing were to 
happen among adult, professional colleagues without their consent, it may not be
viewed too kindly.

### E2E Encryption

[End-to-end encryption (E2EE)](https://en.wikipedia.org/wiki/End-to-end_encryption)
is a system of communication where only the communicating users have the ability to
decrypt and read the messages. If this feature is essential, readers should take
caution to read as much as possible about how a given product supports E2EE.

### Compatibility

The web client typically allows users to join a meeting through their browser.
A web client is often advantageous because it *usually* allows users to avoid
having to install software on their machine. Sometimes, however, the user may
have to download a browser *extension* to support the web client. In addition,
web clients often **do not** support features needed by a meeting *host* or
*presenter*. They are available primarily to support meeting *attendees* only.

### Recommended

The *recommended* platform is either the OS or browser that supports the *most*
features or is the one recommended by the vendor.

## Advanced features

### Personal rooms

A *personal* room is the virtual equivalent of a meeting place that only the
owner has the *keys* to open for an event. Only the owner can host meetings there
and s/he can do so at any time and without scheduling it. It is typically a static
URL where anyone with the link can go at any time to meet with the owner and others
the owner has given the link to. This feature is useful for spontaneous meetings
and open meetings where the owner is connected and waiting but probably engaged
in other tasks and can be *interrupted* then by another person who *enters* their
room. Some products support *notifications* that inform an owner that someone
is trying to enter their room when the owner is not already connected there.

### Breakout Rooms

This is a feature that makes it possible for a single meeting to be broken into
sub-meetings among smaller groups of participants and, after a period of time,
re-joined back into the single large meeting.

In the absence of direct support for breakout rooms, there are other ways of
using either [personal rooms](#personal-rooms) or multiple, parallel scheduled
*virtual meetings* to serve as breakout rooms. If breakout room *leaders* each
have their own personal rooms, each can use their personal room as a breakout
room. A minor inconvenience with this approach is that attendees are not typically
allowed to be in multiple virtual meetings simultaneously. So, attendees wind up
having to disconnect from one meeting and connect to another to move between
the main meeting and the breakout rooms (which to be honest isn't too different
from real-world breakout rooms).

### Virtual background

A virtual background is an image (some products also support short video loops)
which displays is though you are seated just in front of it. Some products may
require a real-world constant color (typically a green) called a *green-screen*
behind you. Newer products can make this feature work without requiring anything
special behind you. In particular, you can hide a messy office by using a photo
you take of your office when it was once clean.

## Experiences in actual use

In this section, we try to capture some high level, subjective assessments,
of the products in useful terms as well as the products perceived suitability in
various usage scenarios based on experiences from actual use.

We use a 4-point Likert subjective quality scale here

1. **Excellent** - Product truly enables/facilitates the use case.
2. **Good** - Product supports the use case well.
3. **Workable** - Product handles the use case but overlooking some shortcomings.
4. **Poor** - Product really doesn't support this use-case without relying upon
other tools.

### Technical project meetings

A technical project meeting involves a lot of technical dialog and technical
diagrams some of which are either created or revised and shared live. This
kind of technical exchange can involve shared screens, shared whiteboards and
shared annotations. Anyone on the team may use a *screen grab* tool or even a
cell phone to capture and save content that is created this way.

### Hands-on trainings

In hands-on training scenarios raise-hand, chat and even break-out room features
can be important. Breakout rooms can be useful for training helpers to virtually
sit with a participant that is running into problems and needs some direct help
without interrupting the training leader. Break-out rooms are also useful in this
use case for the hands-on leader and helpers to *walk the virtual room* and
check in on individual participants even looking at their screen and work.

### Pair programming

Most of the products described here are excellent for virtual
[pair programming](https://en.wikipedia.org/wiki/Pair_programming). In fact, 
pair programming with these technologies is likely *easier* than in a traditional
scenario where the two participants might have to squint over a single laptop
screen.

### Interviewing

Interviewing involves people meeting for the first time. It really requires good
high definition video, good audio and good, reliable network performance to be fully
effective. Chances are, whether these products are really suitable in this use
case probably depends more on prevailing network performance at the time the interview
is conducted than anything else. There are some
[best practices](https://builtin.com/recruiting/video-interview) to follow when
conducting interviews in this manner.

### Hack-a-thons

[Hack-a-thons](https://www.mabl.com/blog/hosting-our-first-hackathon-during-covid-19-quarantine-2020)
typically involve many individuals and teams coming together in the same
venue and event to collaborate and develop software. There is a need for a virtual
event that is comprised of *all* participants as well as smaller virtual meeting rooms
for individual teams. Depending on size, a breakout room feature may work for the
individual teams. If all the participants are part of some larger organization through
which they all have access to an *enterprise* level product, then each team's virtual
room can likely be created using one of the team member's [personal room](#personal-rooms).

### Virtual water cooler

All of the products here are perfectly sufficient for *virtual water cooler* chats.
In many cases, if the participants know each other well, video may not even be needed
nor any sharing of content. Audio-only virtual water cooler chats work great and
give participants a chance to socialize in a way similar to how they might if they
were all together at the same work site. In the real world, water cooler chats are
*spontaneous* whereas in the virtual world, some amount of scheduling may be involved.
One approach is to identify one person to serve as a *host* during some agreed upon
time(s). The host's job is to start and end the virtual water cooler event at the agreed
upon time(s) and others can be free to decide to join or not as they wish. Another
aspect to virtual water cooler chats is that the host may also need to perform some
moderator/facilitator duties. This is because many of the visual cues about who wants
to speak at any given moment are often missing and it becomes necessary to take a slightly
more formal approach with someone (e.g. the host) helping to moderate and facilitate
the discussion. There are many
[other ideas](https://medium.com/@aarondinin/how-to-enable-water-cooler-innovation-for-remote-working-teams-2dfb3d50b1ab)
in the use of video teleconferencing technology similar to this.

### To be done

The information here is evolving and we have only limited resources to create and
maintain it. We intend to make routine updates.

## Other resources

* [Wikipedia comparison](https://en.wikipedia.org/wiki/Comparison_of_web_conferencing_software)
   * Many products compared but small feature set
* [Virtual Conferences: A Guide to Best Practices](https://www.acm.org/virtual-conferences)
   * [A recent ACM report](https://www.hpcwire.com/off-the-wire/acm-releases-report-on-best-practices-for-virtual-conferences/)

##### Zoom notes

* (a) Maximum number of attendees depends on plan. There is a *Large Meeting*
add-on option (not for the *free* plan) for purchase, on a month-to-month basis,
to expand the maximum up to 1000. There is also a *Webinar* add-on option for
purchase, on a month-to-month basis, to expand to up to 10,000 *view-only* participants.
* (b) Zoom's free plan is limited to 40 minutes. The time limit for other plans
is 24 hours.
* (c) Zoom's no-install option requires a web client and has limited functionality. Hosts/presenters
cannot use this option.
* (d) Be aware of recently revealed [security issues about Zoom's chat](https://lifehacker.com/dont-click-on-links-in-public-zoom-chats-right-now-1842618749).
* (e) Live streaming to YouTube/Facebook is support only in Zoom's Webinar product.
* (f) Zoom virtual backgrounds can be *videos*.

##### WebEx Notes

* (a) [*WebEx Meetings*](https://www.webex.com/video-conferencing) is one of a variety
of products offered by WebEx. Some of the features described in this article that are
not supported by *WebEx Meetings* may be supported in their other products.
* (b) WebEx's free plan limits of 50 participants and 40 minutes has been temporarily
upgraded to 100 participants and 24 hours.
* (c) Apart from the selected plan, a number of other factors may effect a WebEx meeting's
maximum number of participants.
WebEx meetings can have up to 1,000 *interactive* participants and up to 3,000 *view-only*
participants. Meeting capacity varies a lot by product and by how a site administrator,
if applicable, configures an *enterprise* plan.
* (d) It appears *expelled* attendees may rejoin as long as the meeting has not been
[*locked*](#lock-meeting).
* (e) WebEx's no-install option requires a web client and has limited functionality. Hosts/presenters
cannot use this option.
* (f) E2E encryption appears to be available only in WebEx's *Enterprise* plan.
* (g) Cloud recording is not available in WebEx's free plan.
* (h) WebEx plans to offer *automatic*, AI-assisted closed captioning as part of an
add-on product called *WebEx Assistant* later this year.
* (i) WebEx virtual background currently works only on mobile platforms.

[TBD]: ./TelecomToolsForRemoteWork.md#to-be-done "To be done"

<!--- join option notes --->
[A]: https://www.google.com "audio-only Phone call (cell/voip/landline)"
[W]: https://www.google.com "Web-browser with extension"
[M]: https://www.google.com "Mobile app (cell-phone/tablet)"
[L]: https://www.google.com "Laptop/desktop computer app"
[VCS]: https://en.wikipedia.org/wiki/List_of_video_telecommunication_services_and_product_brands "Video Conferencing System with dedicated hardware/networking"

<!--- Linux Distribution Notes --->
[U]: https://ubuntu.com/ "Ubuntu"
[D]: https://www.debian.org/ "Debian"
[R]: https://www.redhat.com/en "RedHat"
[O]: https://www.opensuse.org/ "openSUSE"
[C]: https://www.centos.org/ "CentOS"
[F]: https://getfedora.org/ "Fedora"
[+z]: https://support.zoom.us/hc/en-us/articles/204206269-Installing-or-updating-Zoom-on-Linux "Other Linux Distributions"

<!--- Windows Version Notes --->
[8]: https://www.microsoft.com/en-us/software-download/windows8ISO "Windows 8"
[10h]: https://www.microsoft.com/en-us/software-download/windows10ISO "Windows 10 Home"
[10P]: https://www.microsoft.com/en-us/software-download/windows10ISO "Windows 10 Pro"
[10ed]: https://www.microsoft.com/en-us/software-download/windows10ISO "Windows 10 Education"
[10Pw]: https://www.microsoft.com/en-us/software-download/windows10ISO "Windows 10 Pro Workstation"
[10Pe]: https://www.microsoft.com/en-us/software-download/windows10ISO "Windows 10 Pro Education"
[10E]: https://www.microsoft.com/en-us/software-download/windows10ISO "Windows 10 Enterprise"

<!--- OSX Version Notes --->
[osx]: https://www.macworld.co.uk/feature/mac/os-x-macos-versions-3662757/ "OSX version names and numbers"

<!--- iOS Version Notes --->
[iOS]: https://www.apple.com/ios/ios-13/ "iOS Versions"

<!--- Android Version Notes --->
[And]: https://en.wikipedia.org/wiki/Android_version_history "Android version names and numbers"

<!--- Browser Version Notes --->
[Ch]: https://www.google.com/chrome/ "Chrome"
[Sa]: https://www.apple.com/safari/ "Safari"
[Ed]: https://www.microsoft.com/en-us/edge "Edge"
[Fi]: https://www.mozilla.org/en-US/firefox/ "Firefox"


<!---
Publish: preview
RSS update: 2020-05-20
Pinned: yes
RSS update: 
Categories: skills
Topics: personal productivity and sustainability
--->
