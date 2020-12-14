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

The BSSw.io frontpage contains a featured item carousel. The items, in the carousel, can be specified as `slides` on the [Homepage](https://github.com/betterscientificsoftware/bssw.io/edit/master/Site/Homepage.md) file. 

**Carousel format and example**
````
<!---
Slide1 L: link/image
Slide1 R: link/image
Slide2 L: link/image
.
.
Slide6 R: link/image
--->
````
Some points to note:
- The carousel has six `slides`, each having a left (L) and right (R) side. 

````
- Slide1 L: indicates 1st slide in the carousel, left side
- Slide1 R: indicates 1st slide in the carousel, right side
````
- Each side of a slide can hold (1) link to a content page or (2) an image. For example: For a blog post, left side can hold link to the blog post and right side can hold a deck image.
- The `link` is a relative url of the article hosted on the BSSw.io site. For ex: The [article](https://bssw.io/blog_posts/give-thanks) with url `https://bssw.io/blog_posts/give-thanks` would be referred to `blog_posts/give-thanks` in the link.
- The `image` is also the relative url to the [BSSw.io images repo](https://github.com/betterscientificsoftware/images) with a strict path. For ex: If we need to put [this image](https://github.com/betterscientificsoftware/images/blob/master/Blog_1119_seasonal.png) in the carousel, you would specify it as `images/raw/master/Blog_1119_seasonal.png`.

**Carousel highlight slides example**
````
<!---
Slide1 L: blog_posts/performance-portability-and-the-exascale-computing-project
Slide1 R: images/raw/master/Blog_1220_PerfPorta.png
Slide2 L: blog_posts/give-thanks
Slide2 R: images/raw/master/Blog_1119_seasonal.png
Slide3 L: items/tips-for-producing-online-panel-discussions
Slide3 R: images/raw/master/Resource_1120_RemotePanel.png
Slide4 L: blog_posts/recent-successes-with-psip-on-hdf5
Slide4 R: images/raw/master/Blog_1120_PSIP_HDF5_BlackHole.png
Slide5 L: events/panel-year-in-review-what-have-we-learned-so-far
Slide5 R: items/a-collection-of-resources-for-sustaining-open-source-software
Slide6 R: items/software-and-workflow-development
Slide6 L: items/scientific-software-bloggers-worth-following
--->
````

## Front page highlight banner

Highlight banners, on the front page, are configured in the [annoucements](https://github.com/betterscientificsoftware/bssw.io/blob/master/Site/Announcements/Announcements.md) file.

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
- Location of the article where the banner points is relative to the [annoucements.md](https://github.com/betterscientificsoftware/bssw.io/blob/master/Site/Announcements/Announcements.md) file in the BSSw.io github repo.

**Highlights banner example**
````
Announcement:
- [Productivity and Sustainability Improvement Planning (PSIP)](../../Articles/Blog/PsipMainPage.md)
- Display dates: 03/15/2020 - 03/30/2020
````

{% include links.html %}
