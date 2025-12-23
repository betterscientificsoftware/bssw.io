# Virtual Meeting Tools and Features for the HPC/CSE Community

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: May 28, 2020

<!--- deck start --->
Are you familiar with virtual meeting tools and what features they offer? This article explores popular tools such as *Zoom* and *WebEx meetings*.
<!--- deck end --->

*This article distills information from various sources that are current as of 05/28/2020; information will be periodically updated. Note that features (mentioned below) for the products are valid currently, but vendors may change these features in the future. This article may be considered a starting point for investigating these tools and their features.*

There is a wide array of [Teleconferencing](https://en.wikipedia.org/wiki/Teleconference)
products. Many vendors offer products for *virtual meetings*. However, vendors
also tend to distinguish virtual *meetings* from other modalities of video
telecommunications such as *teams*, *training*, *webinars*, and *webcasts*.
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
that have some degree of variability in support across vendors.

In the table below:

* We've tried to provide as many links as possible to information relevant to 
  a given feature.
* *Partial* means some support for the feature exists but not at the level of
  support one would expect.
* *Maybe* means the feature may exist depending on other factors outside of
  the typical user's control.
* Numbered footnotes are links to additional information.
* Abbreviations have balloon hints that are revealed by hovering the mouse over them.
* [TBD](#tbd) means to be done.

Feature | [Zoom](https://www.zoom.us) | [WebEx Meetings](https://www.webex.com)<sup>[aw](#webex-notes-aw)</sup> 
--- | --- | ---
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=3 align="center">[**The Basics**](#the-basics)</td></tr>
[Free Plan](#free-plans) | [Yes](https://zoom.us/pricing) | [Yes](https://www.webex.com/pricing/index.html) 
[Plan Pricing<br>$/mo/host](#plan-pricing) | 0/15/20 | 0/15/20/30 
[Size Limit](#size-limits) | 100-1000<sup>[az](#zoom-notes-az)</sup> | 50-200<sup>[bw](#webex-notes-bw),[cw](#webex-notes-cw)</sup> 
[Length Limit](#length-limits) | &le;24h<sup>[bz](#zoom-notes-bz)</sup> | &le;24h 
[Supported Devices](#supported-devices) | [A]/[W]/[M]/[L] | [A]/[W]/[M]/[L]/[VCS](https://help.webex.com/en-us/7yxpa9/Join-a-Webex-Meeting-from-a-Video-System)
[No Install<br>option](#no-install-option) | [Partial](https://support.zoom.us/hc/en-us/articles/214629443-Zoom-web-client)<sup>[cz](#zoom-notes-cz)</sup> | [Partial](https://help.webex.com/en-us/ozygebb/Join-a-Cisco-Webex-Meeting#Join-a-Meeting-from-the-Webex-Meetings-Desktop-App-or-Mobile-App)<sup>[ew](#webex-notes-ew)</sup>
[HD Video](#high-definition-video) | No | [Maybe](https://help.webex.com/en-us/fw8u4j/Webex-Video-Support)
[Test Meeting](#test-meeting) | [Yes](https://zoom.us/test) | [Yes](https://www.webex.com/test-meeting.html) | [Yes](https://bluejeans.com/111/) | [Partial](https://ucstatus.com/2019/06/26/how-to-place-a-test-call-in-microsoft-teams/) | [Yes](https://support.goto.com/meeting/help/join-a-test-session-g2m050001) | [Partial](https://www.businessinsider.com/how-to-test-skype-video)
[Free Dial-in option](#free-dial-in-option) | [Maybe](https://support.zoom.us/hc/en-us/articles/201362663-Joining-a-meeting-by-phone) | [Maybe](https://help.webex.com/en-us/WBX25713/How-Do-I-Find-the-Global-Dial-In-Number-for-My-Meeting)
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Content Sharing**](#content-sharing)</td></tr>
[Screen Sharing](#screen-sharing) | [Yes](https://support.zoom.us/hc/en-us/articles/201362153-Sharing-your-screen) | [Yes](https://help.webex.com/en-us/i62jfl/Share-Your-Screen-or-Application-in-a-Cisco-Webex-Teams-Meeting)
[Shared Audio](#audio-sharing) | [Yes](https://support.zoom.us/hc/en-us/articles/201362643-Sharing-Computer-Sound-During-Screen-Sharing) | No
[App Sharing](#app-sharing) | [Yes](https://support.zoom.us/hc/en-us/articles/115005706806-Using-annotation-tools-on-a-shared-screen-or-whiteboard) | [Yes](https://help.webex.com/en-us/utfx63/Share-an-Application-in-Cisco-Webex-Meetings)
[Shared Whiteboard](#shared-whiteboard) | [Yes](https://support.zoom.us/hc/en-us/articles/205677665-Sharing-a-whiteboard) | [Yes](https://help.webex.com/en-us/5ddww5/Share-Content-in-Cisco-Webex-Meetings-and-Cisco-Webex-Events)
[Shared Annotations](#shared-annotations)  | [Yes](https://support.zoom.us/hc/en-us/articles/115005706806-Using-annotation-tools-on-a-shared-screen-or-whiteboard) | [Yes](https://help.webex.com/en-us/hc3tig/Options-Available-on-the-Annotate-Toolbar-in-the-Cisco-Webex-Meetings-Suite)
[Able chat](#able-chat) | [Yes](https://support.zoom.us/hc/en-us/articles/203650445-In-Meeting-Chat)<sup>[dz](#zoom-notes-dz)</sup> | [TBD](#tbd)
[Polling/Voting](#voting-or-polling) | [Yes](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) | [Yes](https://help.webex.com/en-us/n0pdj9x/Start-a-Poll-in-Cisco-Webex-Meetings) | [Partial](https://support.bluejeans.com/s/article/Event-Polling) | [Yes](https://support.office.com/en-us/article/create-a-poll-in-microsoft-teams-a3f9112c-01e1-4ee4-bd88-25e4e243b80b) | No | [Yes](https://support.microsoft.com/en-us/office/take-a-poll-in-a-skype-for-business-meeting-6eb1fb85-18a6-422c-ae48-55519841f296?ui=en-us&rs=en-us&ad=us)
[File sharing](#file-sharing) | [Maybe](https://support.zoom.us/hc/en-us/articles/209605493-In-Meeting-File-Transfer#h_35f5965f-bae8-49b2-a1a9-8956fb8022ff) | [Yes](https://help.webex.com/en-us/5ddww5/Share-Content-in-Cisco-Webex-Meetings-and-Cisco-Webex-Events)
[Recording](#recording) | [Yes](https://support.zoom.us/hc/en-us/sections/200208179-Recording) | Maybe<sup>[gw](#webex-notes-gw)</sup>
[Transcription](#transcription) | [Yes](https://support.zoom.us/hc/en-us/articles/115004794983-Automatically-Transcribe-Cloud-Recordings-) | [TBD](#tbd)
[Closed captioning](#closed-captioning) | [Partial](https://support.zoom.us/hc/en-us/articles/207279736-Getting-started-with-closed-captioning) | [Maybe](https://www.webex.com/ai-assistant.html)<sup>[hw](#webex-notes-hw)</sup>
[Live Streaming](#live-streaming) | Maybe<sup>[ez](#zoom-notes-ez)</sup> | [Yes](https://help.webex.com/en-us/n97pcak/Live-Stream-Your-Webex-Meetings)
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
[Expel Attendee](#expel-attendee) | [Yes](https://blog.zoom.us/wordpress/2014/06/03/spotlight-security/)|[Partial](https://help.webex.com/en-us/WBX30745/How-Do-I-Expel-a-Meeting-Participant)<sup>[dw](#webex-notes-dw)</sup>
[Expel Recovery](#expel-recovery) | [Yes](https://support.zoom.us/hc/en-us/articles/360021851371-Allowing-Removed-Participants-or-Panelists-to-Rejoin) | Yes
[Privacy](#privacy) | [Partial](https://tidbits.com/2020/04/03/every-zoom-security-and-privacy-flaw-so-far-and-what-you-can-do-to-protect-yourself/) | [Yes](https://trustportal.cisco.com/c/dam/r/ctp/docs/privacydatasheet/collaboration/cisco-webex-meetings-privacy-data-sheet.pdf)
[E2E Encryption](#e2e-encryption) | [No](https://citizenlab.ca/2020/04/move-fast-roll-your-own-crypto-a-quick-look-at-the-confidentiality-of-zoom-meetings/) | Maybe<sup>[fw](#webex-notes-fw)</sup>
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Advanced Features**](#advanced-features)</td></tr>
[Personal rooms](#personal-rooms) | [Yes](https://support.zoom.us/hc/en-us/articles/203276937-Using-Personal-Meeting-ID-PMI-) | [Yes]( https://help.webex.com/en-us/nul0wut/Cisco-Webex-Personal-Rooms-in-Cisco-Webex-Meetings)
[Breakout rooms](#breakout-rooms) | [Yes](https://support.zoom.us/hc/en-us/articles/206476093-Getting-Started-with-Breakout-Rooms) | [Partial](https://help.webex.com/en-us/8cckd2/Manage-Breakout-Sessions-in-Cisco-Webex-Training) 
[Virtual background](#virtual-background) | [Yes](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background?_ga=2.14223487.938856509.1585291308-953848128.1583382933&_gac=1.183383508.1583390141.Cj0KCQiAwP3yBRCkARIsAABGiPpO0S3qoN8PTc0qdsQBTPiskm6O520ASHcVcXL8kVvTc5O-VTr0XPIaArGGEALw_wcB)<sup>[fz](#zoom-notes-fz)</sup> | [Partial](https://help.webex.com/en-us/80jduab/Webex-Meetings-Change-Your-Video-Background)<sup>[iw](#webex-notes-iw)</sup>
[Bandwidth Management](#bandwidth-management) | No | [Maybe](https://www.cisco.com/c/en/us/products/collateral/conferencing/webex-meetings/white_paper_c11-691351.html)
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">**Convenient Host Features**</td></tr>
Mute all A/V | [Yes](https://support.zoom.us/hc/en-us/articles/203435537-Mute-All-And-Unmute-All)/No | [Yes](https://help.webex.com/en-us/n94aj5j/Mute-or-Unmute-in-Cisco-Webex-Meetings-Suite)/[Yes](https://help.webex.com/en-us/nylc718/Turn-off-Participants-Video-in-Webex-Meetings-and-Webex-Events)
Mute A/V entry | [Yes](https://support.zoom.us/hc/en-us/articles/115005756143-Changing-your-meeting-settings)/No | [Yes](https://help.webex.com/en-us/n94aj5j/Mute-or-Unmute-in-Cisco-Webex-Meetings-Suite)/No
Disable entry/exit<br>sounds | Yes | Yes
Attendee count | Yes | No
Host exit won't<br>end meeting | [Partial](https://support.zoom.us/hc/en-us/articles/201362573-Pass-Host-Controls-and-Leave-the-Meeting) | [Partial](https://help.webex.com/en-us/WBX000023799/A-Host-Only-has-the-Option-to-End-Meeting-when-Leaving-a-Web-Meeting-the-Audio-Conference-Ends)
Exceed size<br>notification | [TBD](#tbd) | [TBD](#tbd)
&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Experiences in actual use (subjective)**](#experiences-in-actual-use)</td></tr>
Max. size | [TBD](#tbd) | 650
Years of use | [TBD](#tbd) | 5
Reliability | Good | Good
Usability | Excellent |  Good
A/V quality | [TBD](#tbd) | [TBD](#tbd)
[Technical project<br>meetings](#technical-project-meetings) | Good | Excellent
[Hands-on<br>trainings](#hands-on-trainings) | [TBD](#tbd) | [TBD](#tbd)
[Pair<br>programming](#pair-programming) | Excellent | Excellent
[Interviewing](#interviewing) | [TBD](#tbd) | [TBD](#tbd)
[Hack-a-thons](#hack-a-thons) | [TBD](#tbd) | [TBD](#tbd)
[Virtual water<br>cooler](#virtual-water-cooler) | [TBD](#tbd) | [TBD](#tbd)


## <a name='the-basics'>The Basics</a>

### <a name='free-plans'>Free plans</a>

Most vendors offer a *free* plan. However, these typically come with length and/or
size limitations. In response to the COVID-19 pandemic situation, some vendors have
either lowered prices of their paid plans or relaxed limitations of their free plans.

Simply *attending* another host's meeting does not typically require a user to purchase a
plan. However, recent security concerns in some products may cause some meeting hosts to
adjust their meeting's security settings such that users are required to have an *account*
with the vendor before logging in and this in turn may require users to obtain a plan even
if only the free one.

If you do need to *host* meetings *and* you do not already have a plan through your home
organization, the lowest-level paid plan in any of these products is probably sufficient
for most project's needs.

### <a name='plan-pricing'>Plan pricing</a>

Most vendors charge monthly, *per host account* and then offer a few different plans
based on meeting size and plan features. In response to the COVID-19 pandemic situation,
some vendors are offering discounts on their plans for a year-long purchase. In addition,
most vendors offer *enterprise* level accounts designed for large organizations with many
users, each of which may require their own *host account*. 

### <a name='size-limits'>Size Limits</a>

The *maximum meeting size* is the maximum number of *participants* in a meeting. A
number of vendors draw a distinction between a *meeting*, which typically requires
participants to *interact* (e.g., speak, exchange chat messages, share content, etc.)
and other modalities of video telecommunications such as a *webinar* where the
majority of people are mere *attendees* who just need to hear and view content.
Some products offer two different limits: one on interactive *participants* and
another on listen/view-only *attendees*.

For *enterprise* products, the maximum meeting size may also depend on how your
organization's plan administrator has configured it.

Be aware that many people like to use an ordinary telephone<sup>[A]</sup> for the audio
part of the meeting and their computer for everything else. This is because ordinary
telephone audio (landline/cell) is often more reliable than
[VoIP-audio](https://en.wikipedia.org/wiki/Voice_over_IP). If their internet connection
fails during the meeting, they can still at least listen and speak.
This raises a couple of potential issues. First, there is no practical advantage in doing
this if the "telephone" the user employs is using a
[VoIP service](https://www.voip-info.org/voip-providers-usa/).
Next, participants use this approach and do not also *bind* the phone call connection together
*with* their computer connection, they appear to the system as two different
meeting participants, taking up two slots. If a majority of participants wind up using this approach
in a large meeting, the effective size limit can be reduced by almost a factor
of two.

What happens if a meeting exceeds its size limit? In most cases, attempts to
join a meeting that is at its size capacity will be prevented. A key question
is if and how the host may be notified of this. At present, this behavior is
unclear.

### <a name='supported-devices'>Supported devices</a>

* [A] = Audio-only telephone device using landline, cell or VoIP
* [W] = Web-browser device often using a browser-extension
* [M] = Mobile device (phone or tablet) operating over the internet
* [L] = Laptop or desktop computer device operating over the internet
* [VCS] = Video Conferencing System with dedicated hardware/network

### <a name='no-install-option'>No-install option</a>

It can be convenient to provide your meeting participants with a way of attending that
does not require them to download or install any new software. This is typically possible
only if they connect through a web browser. Even then, some vendor's products may require
a browser extension to be downloaded. In addition, this approach also typically means
that such participants have limited functionality. For example, they may not be able to
host a meeting as a presenter and share content from their browser.

### <a name='high-definition-video'>High-definition video</a>

So much of human interaction involves
[non-verbal cues](https://www.lifesize.com/en/video-conferencing-blog/speaking-without-words).
Poor video quality can dramatically reduce participants' ability to interpret non-verbal
cues. Among participants with long-standing, pre-existing, high-functioning relationships, the
ability to interpret non-verbal cues is
[not as essential](https://www.comptia.org/blog/the-art-of-non-verbal-communication-in-a-video-conferencing-world).
However, high-definition (HD) video can be essential in other circumstances,
particularly those where the people involved are meeting for the first time.

In the COVID-19 pandemic situation, with so many people being forced to work from home,
the increase in network load has caused some vendors to temporarily disable
support for high-definition video.

In addition, most vendors' products automatically adjust video quality based
on moment-to-moment network responsiveness. Each participant's local
network and/or the wide-area network loads may be such that even if 
high-definition video is supported, the network loads will not support it.

### <a name='test-meeting'>Test meeting</a>

For first-time users, without actually participating in a meeting it can be difficult
to know for sure whether the audio and video of your particular configuration will work with
the vendor's product. A test meeting is a useful way to test your particular setup to
ensure it works, at a basic level, with the vendor's software and service. You may not
be able to test all features, but you should be able to test basic audio and video support.
Most vendors provide a *test meeting* for this purpose. Zoom provides a means to test
audio and video each time prior to connecting to a new meeting.

### <a name='free-dial-in-option'>Free dial-in option</a>

For those who wish to connect audio via ordinary telephone (landline or cell), it can be
convenient to provide your meeting participants with a toll-free option. This feature may
be particularly important for international participants. While this feature is common
across many vendors' products, enabling it typically involves additional cost. However,
enterprise plans as part of your home organization may provide the feature.

## <a name='content-sharing'>Content sharing</a>

Virtual meeting tools provide a variety of features to allow meeting participants to
share content. In the absence of any one of these features, there are often acceptable
work-arounds using other dedicated tools. For example,
[Google docs](https://www.google.com/docs/about/) can be used for some kinds of content
sharing, including some limited whiteboarding;
[Google forms](https://www.google.com/forms/about/) can be used for polling attendees; and
[Google hangouts](https://hangouts.google.com/) (now called *Google Meet*) can be
used for chat.
 
### <a name='screen-sharing'>Screen sharing</a>

Screen sharing is a feature that allows the host/presenter to share everything on his/her screen
with all the participants. All teleconference tools support this feature even from 
mobile devices. However, a number of tools also support variations of this feature for
different needs, as described below.

### <a name='audio-sharing'>Share Audio</a>

Shared audio is a feature that allows any audio content, such as videos with sound, music or
podcasts, to be properly handled such that attendees here *direct* audio as opposed to
indirect audio (e.g. out through the presenter's speakers and back in through the presenter's
microphone). It means audio originating from content on the presenter's computer needs to be
mixed with audio of the presenter's voice, etc. Not all teleconferencing tools support this.


### <a name='app-sharing'>App sharing</a>

App (or Application) sharing is like [*Screen Sharing*](#screen-sharing) except that
the windows of only a single application (e.g., PowerPoint or Word) are shared. The
host/presenter is not forced to share an entire screen but can select only the
window(s) from a specific application to share. This approach can be useful in cases where the
host/presenter tends to have a lot of windows open, and they want to keep the
participants from accidentally seeing the content of those other windows. When you
have a choice, using application-specific sharing is a **best privacy practice**.

### <a name='shared-whiteboard'>Shared whiteboard</a>

A shared whiteboard is similar to but not quite the same functionality as *Shared Annotations*. A shared
whiteboard is a separate drawing area, like a whiteboard in an office, where all
participants can doodle content and paste images that they capture locally.

For some, a shared whiteboard is more than just a realization shared drawing area
where content is created by a mouse or keyboard. The whiteboard includes the *integrations* necessary
to create content using a tablet and pen-based drawing gestures with touch sensitivity, etc.
Currently, no virtual meeting vendors provide such an experience in their shared whiteboard
features. In fact, there are few *dedicated* shared whiteboard solutions available
that work on all platforms that support tablet & pan-based drawing gestures.

### <a name='shared-annotations'>Shared annotations</a>

Shared annotations are similar to but not quite the same as [*Screen Sharing*](#screen-sharing).
Shared annotations allow the presenter/host to draw annotations on top of whatever
content is being displayed in the main window so that all other participants can see it.
In addition, some products allow *attendees* also to draw shared annotations.


### <a name='able-chat'>Able chat</a>

All vendors typically provide some kind of a chat feature that allows participants
to send text messages to each other. We use the term *able* chat to mean that the chat handles
more than just *raw* text. For example, an *able* chat handles functionality such as cut-and-paste across
applications, clickable URL links, private messages between participants (instead
only to all participants), drag-and-drop for some file types, showing who else may be
in the midst of typing a chat message, the ability to save all chat messages to a
text file, and allowing the host to disable chat if necessary.
In the absence of *able chat*, a clumsy
but sufficient work-around is to use a shared [Google doc](https://www.google.com/docs/about/)
or [Google Hangout](https://hangouts.google.com/).
Of course, there is still the issue of how best to distribute a link to meeting participants,
probably via email. Note that Zoom's chat is not *persisted* to newly arriving attendees. A
newly arriving attendee in Zoom will not see any chats that occurred prior to their arrival.

### <a name='voting-or-polling'>Voting or polling</a>

Polling is a feature that allows the host to ask participants a question and have
them anonymously vote their responses. In the absence of this feature, a clumsy
but sufficient work-around is to use [Google forms](https://www.google.com/forms/about/) by 
creating the form and then pasting a link to the form in your meeting's chat
window, allowing all participants to easily go there to vote their response.

### <a name='file-sharing'>File sharing</a>

File sharing allows participants to share whole files, which attendees can then
download to their own systems. This feature has varying levels of support 
among products, often restricted by file types (e.g., extensions). Some
vendors provide support for scripts and even augmented reality files. File
sharing, especially executable scripts, may introduce additional security
concerns.

### <a name='recording'>Recording</a>

Recording of a virtual meeting session is often convenient for participants
who were unable to attend to watch later or for a scribe to go back
and fill in gaps in meeting notes. However, recordings are generally not useful
for *replacing* meeting notes because of the summarization often involved in the
curation of such notes.

The various products provide differing levels of support for what content gets recorded. 
Some products may not make a record of chat messages, for
example. Recorded chat may or may not be synced with A/V content.
It can sometimes be useful for the host to select the content to be
recorded (e.g., audio-only).

Some vendors provide support for producing textual
*transcriptions* from recordings. Recordings can introduce
[*privacy concerns*](#privacy), so it is a best practice to obtain *written*
consent not only to create a recording but also to specify with whom the
recording may later be shared.

### <a name='transcription'>Transcription</a>

Recorded sessions can be transcribed into time-stamped text to enable easy
searching of the recorded stream. Transcription typically requires about 2x
the recording time to complete and is typically available only for sessions
recorded to the *cloud* and pricier plans.

### <a name='closed-captioning'>Closed captioning</a>

All vendors offer *some* support for closed captioning. Typically, the support
provided is just the *display* of captions. The *generation* of captions is
delegated to some other service. For example, a *live captioner* is a person who
transcribes the conversation in real time during a meeting, much like a court
stenographer. Those participants who wish can then enable display of closed
captions.
Some vendors appear already to provide or plan to provide *add-on* features
with automatic captioning.

### <a name='live-streaming'>Live streaming</a>

Some products offer the ability to stream a *live* session to platforms like
YouTube or Facebook. Of course, this also means that the session will be
effectively be *recorded* but only on that platform.
 
### <a name='compatibility'>Compatibility</a>

The web client typically allows users to join a meeting through their browser.
A web client is often advantageous because it *usually* allows users to avoid
having to install software on their machine. Sometimes, however, the user may
have to download a browser *extension* to support the web client. In addition,
web clients often **do not** support features needed by a meeting *host* or
*presenter* but are intended primarily to support only meeting *attendees*.

### <a name='recommended'>Recommended</a>

The *recommended* platform is either the OS or browser that supports the *most*
features or is the platform recommended by the vendor.

## <a name='security'>Security</a>

Depending on the kind of information to be *processed* in a virtual meeting,
the level of security the product provides may or may not be an issue.
When security vulnerabilities of a given virtual meeting product are a
concern, one possible though inconvenient work-around is for
*all meeting participants* to be on the same
[*virtual private network (VPN)*](https://www.techradar.com/news/how-using-a-vpn-with-zoom-can-keep-you-and-your-data-more-secure). This approach adds significantly to the logistical
aspects of running a virtual meeting but may be the best option in
some circumstances.

### Recent issues

Recent security concerns in various virtual meeting products have been all
the rage in the mainstream media. Unfortunately, many sources lack the
technical background to provide any sort of *evaluation* of the level of
risk of issues encountered with respect to the kinds of information
to be *processed*. When we have found technically competent sources, we
provide links to them in the table.

### <a name='best-practices'>Best Practices</a>

For each product, when there is a collection of *best practices* for ensuring
the best possible level of security when using that product for a meeting, we
indicate that in the table and provide a link.

### <a name='lock-meeting'>Lock Meeting</a>

When a meeting is *locked*, it cannot be joined by any other
participants even with the correct credentials. Participants who leave
a locked meeting cannot re-join.

### <a name='expel-attendee'>Expel Attendee</a>

*Expelling* or *removing* an attendee is typically a power that only meeting
hosts have. It is important for hosts to know how to do this *quickly*. If for
some reason the meeting is *bombed*, quick action from the host can correct
the situation before it gets out of hand.

### <a name='expel-recovery'>Expel Recovery</a>

In most products, an attendee who is expelled cannot rejoin that
meeting instance; the attendee would have to use a wholly different *identity* or email
address.  Thus, it is important for hosts to take care when taking the drastic
action of expelling an attendee. Some products do enable a host to *recover*
from this situation, however, allowing an inadvertently expelled attendee to
rejoin with the same identity.

### <a name='privacy'>Privacy</a>

[Privacy is related to but also distinct from security](https://www.hiv.gov/blog/difference-between-security-and-privacy-and-why-it-matters-your-program). While security is about safeguarding data
of any kind, privacy is specifically about safeguarding
[*personally identifiable information (PII)*](https://www.gsa.gov/reference/gsa-privacy-program/rules-and-policies-protecting-pii-privacy-act)
as well as a person's rights about how that information is managed by a third
party.

A potentially common privacy-related situation in virtual meeting settings is the
use of a product's *recording* feature. Doing so without consent of all parties
may create a significant breach of privacy laws.
Making the recording available to a wider audience than attendees believe they
originally consented to may also create a privacy issue.

Another example is whether the system may
notify the host if an attendee has *changed application focus* away from the
virtual meeting application to something else. Such functionality might be
wholly appropriate for an elementary school teacher in a virtual classroom setting
needing to keep an eye on his students. However, if the same thing were to 
happen among adult, professional colleagues without their consent, it may not be
viewed too kindly.

### <a name='e2e-encryption'>E2E Encryption</a>

[End-to-end encryption (E2EE)](https://en.wikipedia.org/wiki/End-to-end_encryption)
is a system of communication where only the communicating users have the ability to
decrypt and read the messages. If this feature is essential, readers should take
caution to read as much as possible about how a given product supports E2EE.

## <a name='advanced-features'>Advanced features</a>

### <a name='personal-rooms'>Personal rooms</a>

A *personal* room is the virtual equivalent of a meeting place that only the
owner has the *keys* to open for an event. Only the owner can host meetings there
and s/he can do so at any time and without advanced scheduling. A personal room is typically a static
URL where anyone with the link can go at any time to meet with the owner and others
to whom the owner has given the link. This feature is useful for spontaneous meetings
and open meetings, where the owner is connected and waiting but probably engaged
in other tasks and can be *interrupted* by another person who *enters* their
room. Some products support *notifications* that inform an owner that someone
is trying to enter a room when the owner is not already connected there.

### <a name='breakout-rooms'>Breakout Rooms</a>

Breakout rooms are a feature that makes it possible for a single meeting to break into
sub-meetings among smaller groups of participants and, after a period of time,
re-join back into the single large meeting.

In the absence of direct support for breakout rooms, there are other ways of
using either [personal rooms](#personal-rooms) or multiple, parallel scheduled
*virtual meetings* to serve as breakout rooms. If breakout room *leaders* each
have their own personal rooms, each can use their personal room as a breakout
room. A minor inconvenience with this approach is that attendees are not typically
allowed to be in multiple virtual meetings simultaneously. So, attendees wind up
having to disconnect from one meeting and connect to another to move between
the main meeting and the breakout rooms (which to be honest isn't too different
from real-world breakout rooms).

It turns out that the current implementation of breakout rooms in Zoom is
fairly limited in that the host *must* decide which attendees go into which
rooms. For large numbers of attendees there is an automated *random* assignment
but there is no way for attendees to leave one breakout room and join another
or to have different breakout rooms representing wholly different activity and
allow attendees to decide for themselves which room (e.g. activity) they want
to go to. The rooms have a specific time limit and when the time is up, they
are all ended and everyone is re-joined to the main meeting.

### <a name='virtual-background'>Virtual background</a>

A virtual background is an image (some products also support short video loops)
that displays as though you are seated just in front of it. Some products may
require a real-world constant color (typically green) called a *green-screen*
behind you. Newer products can make this feature work without requiring anything
special behind you. In particular, you can hide a messy office by using a photo
you take of your office when it was once clean.

### <a name='bandwidth-management'>Bandwidth management</a>

Bandwidth management are those features of the virtual meeting product that enable
any attendee to do some amount of management of the bandwidth to/from their device.
An example is WebEx's ability for an attendee to disable all incoming video. Other
options may involve aspects of tools apart from the virtual meeting software itself.
For example, the camera you use may have ability to control video quality explicitly
allowing you to *always* share only low quality video to conserve bandwidth.

## <a name='experiences-in-actual-use'>Experiences in actual use</a>

In this section, we capture some high-level, subjective assessments
of the products as well as their perceived suitability in
various usage scenarios, based on experiences from actual use.

We use a 4-point Likert subjective quality scale:

1. **Excellent** - Product truly enables/facilitates the use case.
2. **Good** - Product supports the use case well.
3. **Workable** - Product handles the use case but overlooking some shortcomings.
4. **Poor** - Product really doesn't support this use case without relying upon
other tools.
 
### <a name='technical-project-meetings'>Technical project meetings</a>

A technical project meeting involves a lot of technical dialog and technical
diagrams, some of which are either created or revised and shared live. This
kind of technical exchange can involve shared screens, shared whiteboards, and
shared annotations. Anyone on the team may use a *screen grab* tool or even a
cell phone to capture and save content that is created this way.


### <a name='hands-on-trainings'>Hands-on trainings</a>

In hands-on training scenarios, raise-hand, chat, and even break-out room features
can be important. Breakout rooms can be useful for people (e.g., helpers for the training session) to sit virtually
with participants who encounter problems and need some direct help
without interrupting the training leader. Breakout rooms also are helpful in this
use case for the hands-on leader and helpers to *walk the virtual room* and
check on individual participants, even looking at their screen and work.

### <a name='pair-programming'>Pair programming</a>

Most of the products described here are excellent for virtual
[pair programming](https://en.wikipedia.org/wiki/Pair_programming). In fact, 
pair programming with these technologies is likely *easier* than in a traditional
scenario, where the two participants might have to squint over a single laptop
screen.

### <a name='interviewing'>Interviewing</a>

Interviewing involves people meeting for the first time. Interviewing requires good
high-definition video, good audio, and reliable network performance to be fully
effective. Chances are, whether these products are really suitable in this use
case probably depends more on prevailing network performance at the time the interview
is conducted than anything else. There are some
[best practices](https://builtin.com/recruiting/video-interview) to follow when
conducting interviews in this manner.

### <a name='hack-a-thons'>Hack-a-thons</a>

[Hack-a-thons](https://www.mabl.com/blog/hosting-our-first-hackathon-during-covid-19-quarantine-2020)
typically involve many individuals and teams coming together in the same
venue to collaborate and develop software. There is a need for a virtual
event that consists of *all* participants as well as smaller virtual meeting rooms
for individual teams. Depending on size, a breakout room feature may work for the
individual teams. If all participants are part of some larger organization through
which they all have access to an *enterprise* level product, then each team's virtual
room can likely be created using one of the team member's [personal rooms](#personal-rooms).

### <a name='virtual-water-cooler'>Virtual water cooler</a>

All of the products here are perfectly sufficient for *virtual water cooler* chats.
In many cases, if the participants know each other well, video may not even be needed
nor any sharing of content. Audio-only virtual water cooler chats work great and
give participants a chance to socialize in a way similar to how they might if they
were all together at the same work site. In the real world, water cooler chats are
*spontaneous*, whereas in the virtual world, some amount of scheduling may be involved.
One approach is to identify one person to serve as a *host* during some agreed upon
time(s). The host's job is to start and end the virtual water cooler event at the agreed
upon time(s), and others can be free to decide to join or not as they wish. Another
aspect to virtual water cooler chats is that the host may also need to perform some
moderator/facilitator duties. This need arises because many of the visual cues about who wants
to speak at any given moment are often missing, and it becomes necessary to take a slightly
more formal approach, with someone (e.g., the host) helping to moderate and facilitate
the discussion. There are many
[other ideas](https://medium.com/@aarondinin/how-to-enable-water-cooler-innovation-for-remote-working-teams-2dfb3d50b1ab)
on the use of video teleconferencing technology for virtual water cooler conversations.

### <a name='tbd'>To be done</a>

The information here is evolving and we have only limited resources to create and
maintain it. We intend to make routine updates.

## Other resources

* [Wikipedia comparison](https://en.wikipedia.org/wiki/Comparison_of_web_conferencing_software)
   * Many products compared but small feature set
* [Virtual Conferences: A Guide to Best Practices](https://www.acm.org/virtual-conferences)
   * [A recent ACM report](https://www.hpcwire.com/off-the-wire/acm-releases-report-on-best-practices-for-virtual-conferences/)

## Zoom notes

* <a name='zoom-notes-az'>[az]</a>: Maximum number of attendees depends on the plan. There is a *Large Meeting*
add-on option (not for the *free* plan) available for purchase, on a month-to-month basis,
to expand the maximum to 1000. There is also a *Webinar* add-on option for
purchase, on a month-to-month basis, to expand up to 10,000 *view-only* participants.
* <a name='zoom-notes-bz'>[bz]</a>: Zoom's free plan is limited to 40 minutes. The time limit for other plans
is 24 hours.
* <a name='zoom-notes-cz'>[cz]</a>: Zoom's no-install option requires a web client and has limited functionality. Hosts/presenters
cannot use this option.
* <a name='zoom-notes-dz'>[dz]</a>: Be aware of recently revealed [security issues about Zoom's chat](https://lifehacker.com/dont-click-on-links-in-public-zoom-chats-right-now-1842618749).
* <a name='zoom-notes-ez'>[ez]</a>: Live streaming to YouTube/Facebook is supported only in Zoom's Webinar product.
* <a name='zoom-notes-fz'>[fz]</a>: Zoom virtual backgrounds can be *videos*.

## WebEx notes

* <a name='webex-notes-aw'>[aw]</a>: [*WebEx Meetings*](https://www.webex.com/video-conferencing) is one of a variety
of products offered by WebEx. Some features described in this article that are
not supported by *WebEx Meetings* may be supported in other WebEx products.
* <a name='webex-notes-bw'>[bw]</a>: WebEx's free plan limits of 50 participants and 40 minutes has been temporarily
upgraded to 100 participants and 24 hours.
* <a name='webex-notes-cw'>[cw]</a>: Apart from the selected plan, a number of other factors may affect a WebEx meeting's
maximum number of participants.
WebEx meetings can have up to 1,000 *interactive* participants and up to 3,000 *view-only*
participants. Meeting capacity varies a lot by product and by how a site administrator,
if applicable, configures an *enterprise* plan.
* <a name='webex-notes-dw'>[dw]</a>: It appears *expelled* attendees may rejoin as long as the meeting has not been
[*locked*](#lock-meeting).
* <a name='webex-notes-ew'>[ew]</a>: WebEx's no-install option requires a web client and has limited functionality. Hosts and presenters
cannot use this option.
* <a name='webex-notes-fw'>[fw]</a>: 2E encryption appears to be available only in WebEx's *Enterprise* plan.
* <a name='webex-notes-gw'>[gw]</a>: Cloud recording is not available in WebEx's free plan.
* <a name='webex-notes-hw'>[hw]</a>: WebEx plans to offer *automatic*, AI-assisted closed captioning as part of an
add-on product called *WebEx Assistant* later this year.
* <a name='webex-notes-iw'>[iw]</a>: WebEx virtual background currently works only on mobile platforms.

[TBD]: ./TelecomToolsForRemoteWork.md#to-be-done "To be done"

<!--- join option notes --->
[A]: #supported-devices "audio-only Phone call (cell/voip/landline)"
[W]: #supported-devices "Web-browser with extension"
[M]: #supported-devices "Mobile app (cell-phone/tablet)"
[L]: #supported-devices "Laptop/desktop computer app"
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
Publish: yes
RSS update: 2020-05-28
Pinned: no
Topics: personal productivity and sustainability
Track: Experience
--->
