# Not the whole kitchen-sink resource test in Blog

**Hero Image:**
- [Hero URL prefix: ../../images (should work on GH)]<img src='../../images/Blog_1119_WorkThankful.jpg'>

#### Publication date: December 12, 2017


## Test images with relative paths
These images are referenced using relative URLs.  As of 2021-03, we are transitioning to prefer this approach over using fully qualified URLs.  All img URLs should reference
the bssw.io/images directory to work nicely with the typical authoring/development setup.  The front-end will translate such references to the images directory into GH URLs so that the content is ultimately served from the GH repo, as we have been doing. Note that the front-end processes only one image reference per paragraph.  So these must be separated.

[URL prefix: /images (should work on GH)]<img src='/images/Blog_1119_WorkThankful.jpg' />

[URL prefix: ../images (should *not* work on GH)]<img src='../images/Blog_1119_WorkThankful.jpg' />

[URL prefix: ../../images (should work on GH)]<img src='../../images/Blog_1119_WorkThankful.jpg' />

## Test of HTML comment handling

HTML comments look like this: `<!-- arbitrary text -->` (which we can see becasuse we marked it up as code)

Comments in regular text <!-- like this --> should be interpreted as comments.  They should be visible in the resulting HTML source, but not in the rendered version.

### Comments after headings <!-- should also be treated like comments -->

There should be some real text here, just for the sake of appearances

### References <!-- sfer_ezikiw -->
Maybe the heading makes a difference? Or maybe it is spacing after the heading?

### One last attempt <!-- sfer_ezikiw -->
<p>What if the MD heading is immediately followed by HTML?</p>

Concept Name | Summary | Example Tools or Techniques
:---|:---|:---
**Software Gardener Lattices** | &nbsp; | &nbsp;
Kickoff training/meeting | Use the scientific method to understand and build software gardens. | Scientific Method, Objective and Key Results, Agile Methodology Sprint Goal-setting
Growing together: Cognitive apprenticeship | Work with others in the context of learning opportunities, leveraging cognitive apprenticeship techniques and similar. | Cognitive Apprenticeship techniques, Pull Request Reviews, Pair Programming
Ascendant fortitude: Courage, vulnerability, and resilience | Embody bravery and vulnerability to overcome uncertainty and grow within software gardens. | Psychological Safety, Open communication, Mistake accountability and growth
**Code: Software Gardening Senescence** | &nbsp; | &nbsp;
Living fences: Environmental boundaries and replicability | Use environment managers by default to build protected, replicable contexts for your software garden. | Conda, Poetry, Renv
Adventitious code: Software development velocity and linting |	Add and require software linting tools in order to weed inconsistent, obsolete, or dangerous code “volunteers” which may naturally appear. | Pre-commit, Pylint, Stylr, Ruff
Multi-generational adaptation: Surviving through fluidity |	Use abstraction and fitness testing to keep and ensure code flexibility by design and goal alignment. Remove code which becomes disintegrated or overly complex. | Object-oriented design, Fitness functions, Decoupling strategies
**Season: Software Archeology, Nowness, and Proactivity** | &nbsp; | &nbsp;
Software archeology: Wisdom of the ancients |	Hark past development by using existing software to full potential, reference existing implementations, and remove archived or otherwise “dead” code. | Documentation, GitHub Search, GitStats
Nowness rooting: Code maintenance kairos | Orient work towards what needs to happen today, respecting that our conception of the present consistently shifts. | Mindfulness, Kanban task status, Time blocking techniques
Garden proactivity: Anticipating and preparatory growth |	Hope for the best and plan for the worst, setting aspirational but measurable goals and avoiding known risks, weaknesses, or threats by observing them in your software garden planning. | Backcasting, SWOT Analysis, Risk Matrices

<!---
Publish: preview
Categories: Planning, Reliability
Topics: testing
Tags: [import from subresources]
Level: 2
Prerequisites: [import from subresources]
Aggregate: base
--->
