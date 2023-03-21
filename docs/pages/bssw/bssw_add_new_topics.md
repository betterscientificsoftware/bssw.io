---
title: Adding new topics on bssw.io
sidebar: bssw_sidebar
permalink: bssw_add_new_topics.html
toc: false
---
## How to add new topics to bssw.io website

This section describes how to add new topics under the existing categories on the bssw.io site.

The following are the steps to be followed:

* Go to https://github.com/betterscientificsoftware/bssw.io
* Modify the appropriate file in Site/Topics to add the new topic. These files are named by category names and these files control the topics and the order in which they are presented, so you can put the topic anywhere in the category list you want if you adjust the sequence numbers.
* Make a PR, add the preview label, and rebuild the preview site.
* Check that the topic appears when you look at the Resources drop-down. (The topic will not have any resources under it, at this stage.)
* Create a 'WhatIs file'.
  - 'WhatIs' file is used to explain the meaning of the new topic. These files are stored in the [WhatIs directory](https://github.com/betterscientificsoftware/bssw.io/tree/master/Articles/WhatIs). 
  - Ensure that this 'WhatIs' file has 'Pinned: yes' metadata.
  - 'Pinned: yes' metadata allows file to show up as 'RECOMMENDED' in a list of resources. For ex: If you navigate to 'Better Development' category, you can see the ['Recommended What Is files'](https://bssw.io/items?category=better-development) for that category and for each of the topics in that category. 
  - The intention is that the reader should know what the definition and meaning of a particular category/topic is and hence the file is present at the very top of the list and marked as "Recommended". Please see the metadata section for more information on this.
* Merge the PR and rebuild the main site.
