---
title: Troubleshooting Tips for BSSw.io
sidebar: bssw_sidebar
permalink: bssw_troubleshooting.html
toc: true
---


##  Changing Contributor name on BSSw.io

Bssw.io repo > Site > Contributors.md Raw file = make changes to name to override how it displays

There are times when a user’s GitHub display name is **not** their first and last name. For our contributors’ site and author identification, we style all names as first name followed by last name. In order to override the display names from GitHub that do not match our styling, we have created the following process: 

**Step 1:** 
Navigate to the contributors’ list via the GitHub repo bssw.io > Site > Contributors.md

**Step 2:** 
Override the display name using the following format
* Column 1: GH id or "-"
* Column 2: Key for alphabetization (Many of our contributors have multiple words in their last name. Column2 indicates the word from the last name that needs to be alphabetized)
* Column 3: Name to display. (If col 1 is "-" a name matching this column is alphabetized per col 2)

For example: *"vsoch", "Sochat", "Vanessa Sochat"*
      
      Column 1: “vsoch” is the GitHub ID. The user’s name was being displayed as “Vanessasaurus”
      Column 2: “Sochat” is the last name and will be used to alphabetize the name properly on our contributors page
      Column 3: “Vanessa Sochat” is the whole display name that will replace “Vanessasaurus”

Additional examples can also be found in the Contributors.md document. 


{% include links.html %}
