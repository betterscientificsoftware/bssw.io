### Notes for content development

Things to look out for

* Are we considering the right tools (top row)?
* Are we considering the right features (left column)?
* Are we curating the *best* links for the associated info?
* We agreed that use-cases and etiqutte are likely best handled as a sep. article

# Virtual Meeting Tools and Features for the HPC/CSE Community

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

* *Partial* means some support for the feature exists.
* *Maybe* means the feature may exist depending on other factors outside of the typical user's control.
* Numbered footnotes are links to additional information.
* Lettered footnotes
   * <sup>X</sup>Indicates a feature is available in another of the vendor's products.
   * <sup>Y</sup>Indicates a feature can vary depending on your organization's configuration.
* Abbreviations have balloon hints which are revealed by hovering the mouse over them.

Feature | [Zoom](https://www.zoom.us) | [WebEx Meetings](https://www.webex.com)<sup>[1a](#webex-notes)</sup> | [BlueJeans](https://www.bluejeans.com) | [MS Teams](https://teams.microsoft.com/start) | [GoToMeeting](https://www.gotomeeting.com)<sup>[1a](#gotomeeting-notes)</sup> | [Skype Business](https://www.skype.com/en/)
--- | --- | --- | --- | --- | --- | ---
&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**The Basics**](#the-basics)</td></tr>
[Free Plan](#free-plans) | [Yes](https://zoom.us/pricing) | [Yes](https://www.webex.com/pricing/index.html) | xxx | xxx | [Partial](https://www.gotomeeting.com/try)<sup>[1b](#gotomeeting-notes)</sup>
[Plan Pricing](#plan-pricing)<br>$/mo/host | 0/15/20 | 0/15/20/30 | xxx | xxx | 12/16
[Size Limit](#meeting-size-limits) | 100-1000<sup>[1a](#zoom-notes)</sup> | 50-200<sup>[1c](#webex-notes)</sup> | xxx | xxx | 150/250
[Supported Devices](#supported-devices) | XXX | [A]/[W]/[M]/[C]/[VCS] | [A]/[W]/[M]/[C]/[VCS] |
[No Install](#no-install-option)<br>Option
[HD Video](#high-definition-video) | No | [Maybe](https://help.webex.com/en-us/fw8u4j/Webex-Video-Support)
[Test Meeting](#test-meeting) | [Yes](https://zoom.us/test) | [Yes](https://www.webex.com/test-meeting.html) | [Yes](https://bluejeans.com/111/) | [Partial](https://ucstatus.com/2019/06/26/how-to-place-a-test-call-in-microsoft-teams/) | [Yes](https://support.goto.com/meeting/help/join-a-test-session-g2m050001) | [Partial](https://www.businessinsider.com/how-to-test-skype-video)
[Free Dial-in option](#free-dial-in-option) | XXX | [Maybe](https://help.webex.com/en-us/WBX25713/How-Do-I-Find-the-Global-Dial-In-Number-for-My-Meeting)
&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Content Sharing**](#content-sharing)</td></tr>
[Screen Sharing](#screen-sharing) | [Yes](https://support.zoom.us/hc/en-us/articles/201362153-Sharing-your-screen) | [Yes](https://help.webex.com/en-us/i62jfl/Share-Your-Screen-or-Application-in-a-Cisco-Webex-Teams-Meeting) |
[App Sharing](#app-sharing) | XXX | [Yes](https://help.webex.com/en-us/utfx63/Share-an-Application-in-Cisco-Webex-Meetings)
[Shared Whiteboard](#shared-whiteboard) | [Yes](https://support.zoom.us/hc/en-us/articles/205677665-Sharing-a-whiteboard) | [Yes](https://help.webex.com/en-us/5ddww5/Share-Content-in-Cisco-Webex-Meetings-and-Cisco-Webex-Events)
[Shared Annotations](#shared-annotations)  | XXX | [Yes](https://help.webex.com/en-us/hc3tig/Options-Available-on-the-Annotate-Toolbar-in-the-Cisco-Webex-Meetings-Suite)
[Smart chat](#smart-chat)
[Polling/Voting](#voting-or-polling) | [Yes](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) | [Yes](https://help.webex.com/en-us/n0pdj9x/Start-a-Poll-in-Cisco-Webex-Meetings) | [Partial](https://support.bluejeans.com/s/article/Event-Polling) | [Yes](https://support.office.com/en-us/article/create-a-poll-in-microsoft-teams-a3f9112c-01e1-4ee4-bd88-25e4e243b80b) | No | [Yes](https://support.microsoft.com/en-us/office/take-a-poll-in-a-skype-for-business-meeting-6eb1fb85-18a6-422c-ae48-55519841f296?ui=en-us&rs=en-us&ad=us)
[File Sharing](#file-sharing) | [Maybe](https://support.zoom.us/hc/en-us/articles/209605493-In-Meeting-File-Transfer#h_35f5965f-bae8-49b2-a1a9-8956fb8022ff) | [Yes](https://help.webex.com/en-us/5ddww5/Share-Content-in-Cisco-Webex-Meetings-and-Cisco-Webex-Events)
[External Integrations](#external-integrations) |
Chat |
&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Software Compatibility**](#desktop-native-app) (hover for details)</td></tr>
Windows Desktop |[8]/[10h]/[10p] | [8]/[10h]/[10E] | [8]/[10h]
Linux Desktop | [U]/[D]/[C]/[R]/[O]/[F]/[+][+z] | [U]/[R]/[O]/[F] | [R]/[F]
macOS Desktop | [&ge;10.7][osx] | [&ge;10.13][osx] | [&ge;10.11][osx]
Presenter's Browser | **[Ch]**/[Ed] | **[Ch]**/**[Fi]**/[Sa]
Attendee's Browser | **[Ch]**/[Ed]/[Fi]/[Sa] | **[Ch]**/**[Fi]**/[Sa]
Presenter's Mobile | [And]/[iOS] | [And]/[iOS] | [And]/[iOS] |
Attendee's Mobile | [And]/[iOS] | [And]/[iOS] | [And]/[iOS] |
&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">[**Security**](#security)</td></tr>
[Recent Issues](#recent-issue) | [Yes](https://tidbits.com/2020/04/03/every-zoom-security-and-privacy-flaw-so-far-and-what-you-can-do-to-protect-yourself/)
[Best Practices](#best-practices) | [Yes](https://zoom.us/security) | [Yes](https://help.webex.com/en-us/8zi8tq/Cisco-Webex-Best-Practices-for-Secure-Meetings-Hosts)
[Lock Meeting](#lock-meeting) | [Yes](https://blog.zoom.us/wordpress/2014/06/03/spotlight-security/) | [Maybe](https://help.webex.com/en-us/zcvgyc/Webex-Teams-Lock-or-Unlock-Your-Meeting)
[Expel Attendee](#expel-attendee) | [Yes](https://blog.zoom.us/wordpress/2014/06/03/spotlight-security/)|[Partial](https://help.webex.com/en-us/WBX30745/How-Do-I-Expel-a-Meeting-Participant)<sup>[1d](#webex-notes)</sup>
[Expel Recovery](#expel-recovery) | [Yes](https://support.zoom.us/hc/en-us/articles/360021851371-Allowing-Removed-Participants-or-Panelists-to-Rejoin) | Yes |
Encryption | XXX | [Partial](https://help.webex.com/en-us/zcvgyc/Webex-Teams-Lock-or-Unlock-Your-Meeting)
[Privacy](#privacy) | [Poor](https://tidbits.com/2020/04/03/every-zoom-security-and-privacy-flaw-so-far-and-what-you-can-do-to-protect-yourself/)|
&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">**Advanced Features**</td></tr>
[Breakout Rooms](#breakout-rooms) | [Yes](https://support.zoom.us/hc/en-us/articles/206476093-Getting-Started-with-Breakout-Rooms) | [Partial](https://help.webex.com/en-us/8cckd2/Manage-Breakout-Sessions-in-Cisco-Webex-Training) | [Yes](https://www.bluejeans.com/blog/introducing-bluejeans-breakout-sessions) | [Yes](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/introducing-microsoft-teams-rooms-updated/ba-p/323848) | No | No
Live Streaming
Co-Hosting
Augmented Reality |
Recording/playback
Calendar integration
Speaker tracking
Gallery view
Virtual backgrounds
&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;<tr><td colspan=7 align="center">**Real experiences in actual use (subjective)**</td></tr>
Max *effective* size
Years of experience as user
Reliability as experienced by real users
Ease of Use
Audio quality
Video quality
Hands-on trainings
Pair programming
Interviewing
Virtual hack-a-thons
Virtual hallway discussions

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
orginization, the lowest-level paid plan in any of these products is probably sufficient
for most project's needs.

### Plan pricing

Most vendors charge monthly, *per host account* and then offer a few different plans
based on meeting size and plan features. In response to the current pandemic situation,
some vendors are offering discounts on their plans for a year-long purchase. In addition,
most vendors offer *enterprise* level accounts designed for large organizations with many
users each of which may require their own *host account*. 

### Meeting size limits

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

### Supported devices

* [A] = Audio-only telephone device using landline, cell or VoIP.
* [W] = Web-browser device often using a browser-extension.
* [M] = Mobile device (phone or tablet) operating over the internet.
* [C] = Computer device (laptop or desktop) operating over the internet.
* [VCS] = Video Conferencing System with dedicated hardware/network.

### No install option

It can be conveninent to provide your meeting participants with a way of attending that
does not require them to download or install any new software. This is typically possible
only if they connect through a web browser. Even then, some vendor's products may require
a browser extension to be downloaded. In addition, this approach also typically means
that such a participant have limited functionality. For example, they may not be able to
share content from their browser.

### High definition video

So much of human interaction involves
[non-verbal cues](https://www.lifesize.com/en/video-conferencing-blog/speaking-without-words).
Poor video quality can dramatically reduce participant's ability to interpret non-verbal
cues. Among participants with long-standing, pre-existing, high-functioning relationships, the
ability to interpret non-verbal cues is
[not as essential](https://www.comptia.org/blog/the-art-of-non-verbal-communication-in-a-video-conferencing-world).
However, high definition video can be essential in many other circumstances.

Most vendor's products automatically adjust video quality based on moment-to-moment network
responsiveness. In the current pandemic situation, whether the vendor's product supports
high-definition video may be only part of the story. Another issue is whether each
participant's local network as well as the wide-area network loads will be such as to prevent
high definition video.

### Test meeting

For first time users, without actually participating in a meeting it can be difficult
to know of sure if the audio and video of your particulary configuration will work with
the vendor's product. A test meeting is a useful way to test your particular setup to
ensure it works, at a basic level, with the vendor's software and service. You may not
be able to test all features but you should be able to test basic audio and video support.
Most vendors provide a *test meeting* for this purpose. Zoom provides a means to test
audio and video each time prior to connecting to a new meeting.

### Free dial-in option

For those who wish to connect audio via ordinary telphone (landline or cell), it can be
convenient to provide your meeting participants with a toll-free option. This feature may
be particularly important for international participants. While this feature is common
across many vendor's products, enabling it typically involves additional costs. However,
enterprise plans as part of your home organization may provide the feature.

## Content Sharing

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

### Shared annotations

This is similar to but not quite the same thing as [*Screen Sharing*](#screen-sharing).
Shared annotations allows the presenter/host to draw annotations on top of whatever
content is being displayed in the main window so that all other participants can see it.

### Smart chat

All vendor's typically provide some kind of a chat feature which allows participants
to send text messages to each other. By *smart* chat here, we mean the chat handles
more than just *raw* text. For example, a *smart* chat handles clickable URL links,
private messages between participants (instead to all participants), drag-n-drop
for text files, showing who else may be in the midst of typing a chat message, etc.
In the absence of this feature a clumsy but sufficient work-around is to use a shared
[Google doc](https://www.google.com/docs/about/). Of course, you need to find a way
to distribute a link to your meeting participants most likely via email.

### Voting or polling

This is a feature that allows the host to ask participants a question and have
them anonymously vote their responses. In the absence of this feature, a clumsy
but sufficient work-around is to use [Google forms](https://www.google.com/forms/about/) by 
creating the form and then pasting a link to the form in your meeting's chat
window allowing all participants to easily go there and vote their response.

## Security

### Best Practices

For each product, there is a collection of *best practices* for ensuring the
highlest level of security for a meeting.

### Lock Meeting

When a meeting is *locked*, that means it cannot be joined by any other
participants even with the correct credentials. Participants that leave
a locked meeting cannot re-join either.

### Expel Attendee

*Expeling* or *removing* an attendee is typically a power that only meeting
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

### Encryption


### Laptop/Deskside Web Client Compatability

The web client typically allows users to join a meeting through their browser.
A web client is often advantageous because it *usually* allows users to avoid
having to install software on their machine. Sometimes, however, the user may
have to download a browser *extension* to support the web client. In addition,
web clients often **do not** support features needed by a meeting *host* or
*presenter*. They are available primary to support meeting *attendees* only.

### Recommended Browser

The *recommended* browser is either the browser that supports the *most*
features or is the one recommended by the vendor.


### Breakout Rooms

This is a feature that makes it possible for a single meeting to be broken into
sub-meetings among smaller groups of participants and, after a period of time,
re-joined back into the single large meeting.

##### Zoom Notes

* (a) Maximum number of attendees depends on plan. There is a *Large Meeting*
add-on option (not for the *free* plan) for purchase, on a month-to-month basis,
to expand the maximum up to 1000. There is also a *Webinar* add-on option for
purchase, on a month-to-month basis, to expand to up to 10,000 *view-only* participants.
* (b) Zoom's free plan is limited to 40 minutes. The time limit for other plans
is 24 hours.

##### WebEx Notes

* (a) [*WebEx Meetings*](https://www.webex.com/video-conferencing) is one of a variety
of products offered by WebEx. Some of the features described in this article that are
not supported by *WebEx Meetings* may be supported in their other products.
* (b) WebEx's free plan limits of 50 participants and 40 minutes has been temporarily
upgraded to 100 participants and 24 hours.
* (c) A number of factors may effect a WebEx meeting's maximum number of participants.
WebEx meetings can have up to 1,000 *interactive* partcipants and up to 3,000 *view-only*
participants. Meeting capacity varies a lot by product and by how a site administrator,
if applicable, has configured things.
* (d) It appears *expelled* attendees may rejoin as long as the meeting has not been
[*locked*](#lock-meeting).

##### GoToMeeting Notes

* (a) [GoToMeeting](https://www.gotomeeting.com) is part of a larger line of products
including GoToTraining and GoToWebinar. We consider here only the features in
the GoToMeeting product. Some features not availabe in GoToMeeting are available
in these other products.
* (b) GoToMeeting offers a 14-day free trial.

## Other products not considered here

https://en.wikipedia.org/wiki/Comparison_of_web_conferencing_software


<!--- join option notes --->
[A]: https://www.google.com "audio-only Phone call (cell/voip/landline)"
[W]: https://www.google.com "Web-browser with extension"
[M]: https://www.google.com "Mobile app (cell-phone/tablet)"
[C]: https://www.google.com "laptop/desktop Computer app"
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
[Sa]: https://www.apple.com/safari/) "Safari"
[Ed]: https://www.microsoft.com/en-us/edge) "Edge"
[Fi]: https://www.mozilla.org/en-US/firefox/) "Firefox"
