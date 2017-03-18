# What is Issue Tracking? Note, the first part is identical to the material in the collaboration.md file; how do we organize the material so it can be presented in multiple places but there is only one copy in the repository? Plus if the material on this page is provided as a popup in the collaboration.md page then the first part should NOT be displayed in the popup.

Issue tracking is the process of managing a collection of issues (bugs, feature requests, missing documentation, etc.) that are currently being handled, or should be handled, by a software development team.

An issue tracker is a software system that is used by the software developers to keep track of the issues (who is responsible for each issue, when the issue was reported, etc). Most modern issue trackers used in the open source community are web-based and provide rich functionality for adding new issues, assigning issues to developers, recording notes on the issue, linking repository commits associated with the issue, etc. Issue trackers can also be used to plan new development activities.



An "issue" represents anything that, if resolved, results in an improvement to a software system. When used for bug tracking, an issue is often called a (trouble) ticket. This document takes the expansive view, as is common in open source development, that a single issue tracker can be used to manage both bug tracking as well as future development plans for the software project. As such a useful issue tracker must have the following capabilities. 

* Be accessable anywhere, from any system. Hence most modern issue trackers are web based.
* Be available for both users to report bugs, (and requests for new features) and track progress on the requests, while also allowing developers to manage permissions for updating issues with progress reports etc.
* Provide email updates on the status of the issue to relevent users and developers.
* Allow setting priorities (which are more important or urgent than others) on issues.
* Allow assigning developers to fix particular issues.
* Allowing searching and sorting issues.
* Allow labeling issues with keywords to facilitate searching issues.
* Allow providing and tracking milestones needed for resolution of an issue.
* Allow tracking the time needed to resolve an issue.
* Allow both users and developers to add (and update) notes on particular issues.
* Provide links from the issue tracker to the commits in the software that represent progress on the issue, and vice versa.
* Be intuitive to new and casual users, yet retain powerful features needed by experienced developers.

All three modern web-based repository hosting systems, bitbucket, github, and gitlab provide an issue tracking system integrated with the repository management system and support most, if not all of the capabilities listed above.

Contributed by: Barry Smith
