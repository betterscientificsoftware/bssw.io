---
title: Content Highlighting on BSSw.io
sidebar: bssw_sidebar
permalink: bssw_content_highlighting.html
toc: true
---
Content can be highlighted in three ways on BSSw.io:
- Article recommendations
- Front page carousel highlights slides
- Front page highlight banner

## Article recommendations
To "recommend" any content in a topic area on BSSw.io, you can simply set the "pinned: yes" metadata parameter in that content file. For more details, see [common metadata](bssw_content_metadata.html#pinned) section.

````
pinned: yes
````

## Front page carousel highlight slides

The BSSw.io frontpage contains a featured item carousel. The items, in the carousel, can be specified as `slides` on the [Homepage](https://github.com/betterscientificsoftware/bssw.io/edit/main/Site/Homepage.md) file. 

**Carousel format and example**
````
<!---
Slide1 L: article or image reference
Slide1 R: article or image reference
Slide2 L: article or image reference
.
.
Slide5 R: article or image reference
--->
````
Some points to note:
- The carousel can have as many `slides`, as we like.  Each slide has a left (L) and right (R) side, so it can highlight two articles or an article and an accompanying image (preferred, particularly for blog articles).  We need to be careful not to have too many slides in the carousel.  Use *five* slides as a guideline.

````
- Slide1 L: indicates 1st slide in the carousel, left side
- Slide1 R: indicates 1st slide in the carousel, right side
````
- Each side of a slide can hold (1) a reference to a content page or (2) an image. For example: For a blog post, left side should reference the blog post itself and right side should reference the hero image.
- An `article` is a relative path to the source of the article in the bssw.io repository. For ex: The [article](https://bssw.io/blog_posts/give-thanks), which corresponds to the source file `Articles/Blog/GiveThanks.md`, would be referred to as `../Articles/Blog/GiveThanks.md` in the carousel.
- An `image` is also a relative path to the desired image. For ex: If we need to put [this image](https://github.com/betterscientificsoftware/images/blob/main/Blog_1119_seasonal.png) in the carousel, you would specify it as `../images/Blog_1119_seasonal.png`.

**Carousel highlight slides example**
````
<!---
Slide1 L: ../Articles/Blog/BSSwFellowshipApplicationsOpen2021.md
Slide1 R: ../images/Blog_2108_FellowsAppOpen.png
Slide2 L: ../Articles/Blog/2021-08-registry-best-practices.md 
Slide2 R: ../CuratedContent/ThingsYouShouldNeverDoPartI.md
Slide3 L: ../Articles/Blog/2021-08-IntegratingInterns.md
Slide3 R: ../images/Blog_0821_Interns.png
Slide4 L: ../Articles/Blog/2021-07-BSSwFellows21.md
Slide4 R: ../images/Blog_0720_Fellows.png
Slide5 L: ../CuratedContent/SwEcosystems.md
Slide5 R: ../CuratedContent/InclusiveNamingInitiative.md
--->
````

## Front page highlight banner

Highlight banners, on the front page, are configured in the [annoucements](https://github.com/betterscientificsoftware/bssw.io/blob/main/Site/Announcements/Announcements.md) file.

**Highlights banner format**
````
Announcement:
- [Text on the banner](Location-of-markdown-file-relative-to-the-annoucements-markdown-file)
- Display dates: mm/dd/yyyy - mm/dd/yyyy
````
Some points to note:
- Only one annoucement is allowed. Please comment any other annoucement in the file before adding a new one.
- Please follow the format exactly
- The display dates are the date range during which the banner will be displayed.
- Location of the article where the banner points is relative to the [annoucements.md](https://github.com/betterscientificsoftware/bssw.io/blob/main/Site/Announcements/Announcements.md) file in the BSSw.io github repo.

**Highlights banner example**
````
Announcement:
- [Productivity and Sustainability Improvement Planning (PSIP)](../../Articles/Blog/PsipMainPage.md)
- Display dates: 03/15/2020 - 03/30/2020
````

{% include links.html %}
