# Navigating the Transition of (Climate) Science to the Cloud

As data for science is increasingly available via cloud computing resources, challenges arise in keeping up with
fast-growing and fast-changing innovations in the world of large data and cloud computing.
This article discusses lessons learned in developing a tutorial about how to extract, visualize, and analyze time series of Earth data from satellite and satellite-based datasets in the cloud.

#### Contributed by [Marisol García-Reyes](https://github.com/marisolgr)

#### Publication date: June 29, 2022

Climate-related studies require extensive ocean, atmospheric, and land data sets. Satellite technology has been employed long enough that global data sets now span several decades, and they continue to grow by the minute. These Earth data sets promise answers to many climate-related questions, while also opening the door to the possibility of answering new questions in areas where in situ data are limited in space and/or time. This is especially relevant now that these data are migrating to and are increasingly freely-available in the cloud.

But who has access to these data, really?

Open science, although not a new concept, has gained great popularity in recent years. In my opinion, open science needs to go beyond making publications, data, or code available --- also making them accessible, particularly to those scientists who will bring new ideas, perspectives, and skills to the table. Problems and questions that concern us all, like global climate change and its impacts, can be truly approached only with the creativity and innovation that diverse, interdisciplinary, and international teams can develop together. Those diverse scientists, however, are busy honing their unique skills and perspectives and may not be able to devote a lot of time to keeping up with the fast-growing and fast-changing innovations in the world of large data and cloud computing.

### Challenges of accessing satellite data

Using satellite and satellite-based (reanalysis) datasets for climate and climate impact studies involves, in a nutshell, analyzing decades-long time series. Given the amount of data that exists and the formats in which data are stored (mostly one file with a global field per time step, be that day or month), extracting time series to perform climate-related analysis requires a level of computing expertise and computing resources that currently, for the most part, only climate and data scientists possess.

Luckily, many advances in computing increasingly facilitate the acquisition and analysis of such data, from cloud storage and computing, to programming languages and libraries that have largely increased the efficiency of code while reducing the need of specialized hardware on-site. However, for scientists of other fields who are or can potentially be interested in using long-term time series of satellite data in their research, knowing where to start and what to learn can be daunting and confusing, and the learning curve can be steep and discouragingly time consuming. Providing access to these large Earth dataset and computing advances cannot be achieved only by sharing code in Github or data in the cloud; there is also an urgent need for tools and guides that facilitate their use.

With the support of the [Better Scientific Software (BSSw) Fellowship](https://bssw.io/fellowship), and building on NASA-supported work, I developed a tutorial that aims to provide an overview of how to extract, visualize, and analyze time series of Earth data from satellite and satellite-based datasets in the cloud. The idea behind the tutorial is to get new users’ toes wet, so that they can learn about the capabilities of new data technologies through hands-on examples, hopefully inspiring them to learn more and apply these tools to their research.

The tutorial can be found in Github (<https://github.com/marisolgr/python_sat_tutorials>) and can be run entirely in the cloud with the help of [mybinder.org](https://mybinder.org). That way, new users can bypass the technicalities of installing Python, Jupyter Notebooks, and all the necessary libraries, and in particular, keeping those libraries up-to-date and compatible. The tutorial is divided in two sections. The first contains the basic Python concepts and commands that are needed to understand and run. The second part contains examples of data acquisition and analysis and is divided into three sections: ocean, atmospheric, and land data, with a combination of data from the cloud and online, satellite, and satellite-based. The tutorial is designed for self-study, but I gave a few online classes as a demonstration and to gauge the user experience with the tutorial material and approach.

I hope you take a look at the tutorial and judge for yourself. Here, I want to share my own learning experience while making and teaching it.

### Lessons learned in developing the tutorial

First of all, let me state for the record that I am not a Python expert, although I am an experienced programmer. I learned Python a couple of years ago while also learning about cloud computing, and that made developing this tutorial one of the most challenging and fun computing experiences I have ever had.

The first thing I learned is that not everybody is as crazy about time series as I am, and the fact that satellite data are not formatted to facilitate time series analysis should have been my first clue. In most instances, satellite data are stored as one global image or file per time unit. This makes the acquisition of a time series (of a latitude/longitude point or of a number of points within a region) an I/O nightmare and also a nightmare for somebody who is just learning to code. I also learned that there are not as many examples to follow or borrow code from for time series analysis as there are for processing spatial data. Even reanalysis data (output from models that incorporate satellite and other in situ data to provide a gap-free dataset) are sometimes stored in chunks of time to avoid gigantic file sizes.  Sometimes the files are organized in monthly and yearly folders, making the acquisition of a time series a good exercise for coding loops.

While understandable from a historical point of view, this data formatting is outdated and cumbersome now that decades of data are available. New data formats and archiving methods are being tested and created as we speak, so there is hope. But for those outside technology circles, this means too much change to be easy to absorb and use. A certain level of expertise and patience is necessary to modify scripts when necessary due to changing locations, access, and formats. It will require some vision and resources from data scientists and managers to keep testing these new formats until we land on one that accommodates the most needs.

This circumstance goes hand-in-hand with the second thing I learned: cloud technologies (including data access) and access libraries have not reached a point of maturity and stability for a non-expert to keep up. It is still time-consuming, challenging, and frustrating to keep your code working, even when your skills are above average. There is a lot of information online, true, but sometimes there is too much information for non-experts to discern what addresses their challenges or recent changes. I wouldn’t be able to complete the scripts that access cloud data if (1) I didn’t have a grant that pays for my time, and (2) I didn’t have an expert to ask when I was in deep darkness about what was wrong or what to try next.

The final lesson learned came once I managed to run my first data acquisition script without a single error or warning, and I started to look for data that I could use in other examples. My goal was to make one script for ocean data, another for atmospheric data, and the last one for land data. I had lots of ideas for cool analyses, but then came a reality-check when I realized that not all satellite data were available or freely available in the cloud. Although growing, the actual data available to do time series analysis are still limited. This situation is reflected in the tutorial, as I needed to use reanalysis data products located both in the cloud and other online locations. In the end, I think this circumstance worked out for me as now I have scripts for a wide range of data sources, but this was not the initial goal. There is a need for a harder push for data to become more freely and easily available on the cloud. But there is also a need for more overlapping time when non-experts can access data the old-fashioned way (online), before we all can handle acquiring data from the cloud.

Things are by not by any means bad. We’re making progress. During the year I worked on this project, many things changed for good. In the end, what initially seemed like a moving target ended up in a better place than I thought it would. Although data formats and storage issues are still difficult to navigate, during this year data access has improved in two ways: there are more data freely available, and there are more standardized ways to access it. In addition, cloud computing platforms like mybinder are stable enough to be consistently and reliably used. So, the pieces are falling into place. I do think we are getting close to the day when time series of satellite data and cloud computing tools are within reach of any researcher interested in using climate data in their research, regardless of their level of expertise with large data sets or computing resources. Hopefully, really close. Our planet needs their science.

### Related resources
* Webinar: [Acquisition and Analysis of Times Series of Satellite Data in the Cloud – Lessons from the Field](https://ideas-productivity.org/events/hpc-best-practices-webinars/#webinar063)
* Tutorial: [Timeseries of Satellite Data using Python](https://github.com/marisolgr/python_sat_tutorials)

### Author bios

[Marisol García-Reyes](https://github.com/marisolgr) is a principal scientist at the [Farallon Institute](http://www.faralloninstitute.org/), a nonprofit scientific organization. [Her research](http://www.faralloninstitute.org/marisol) focuses on the relationships between ocean conditions and marine ecosystems, and how they are impacted by climate. Marisol is committed to increasing equity and diversity in science and education by improving access to computational technology and increasing and broadening participation.

<!---
Publish: yes
Pinned: no
Topics: big data, cloud computing, online learning
--->
