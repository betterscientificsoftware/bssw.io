# Kitchen-sink resource test in Articles

#### Publication date: December 12, 2017


## Test images with relative paths
These images are referenced using relative URLs.  As of 2021-03, we are transitioning to prefer this approach over using fully qualified URLs.  All img URLs should reference
the bssw.io/images directory to work nicely with the typical authoring/development setup.  The front-end will translate such references to the images directory into GH URLs so that the content is ultimately served from the GH repo, as we have been doing. Note that the front-end processes only one image reference per paragraph.  So these must be separated.


[URL prefix: /images (should work on GH)]<img src='/images/Blog_1119_WorkThankful.jpg' />

[URL prefix: ../images (should work on GH)]<img src='../images/Blog_1119_WorkThankful.jpg' />

[URL prefix: ../../images (should *not* work on GH)]<img src='../../images/Blog_1119_WorkThankful.jpg' />

<!---
Publish: preview
Categories: Planning, Reliability
Topics: testing
Tags: [import from subresources]
Level: 2
Prerequisites: [import from subresources]
Aggregate: base
--->
