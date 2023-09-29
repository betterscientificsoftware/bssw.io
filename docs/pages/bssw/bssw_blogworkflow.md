---
title: Blog Content Workflow
sidebar: bssw_sidebar
permalink: bssw_blogworkflow.html
---

# Editorial Workflow for BSSw.io Blog Content

### Actors
  * Author
  * Editor (e.g., Lois McInnes or David Bernholdt)
    * This role needs to have an understanding of the goals and strategy behind the BSSw.io site and general knowledge of the subject matter and community
  * Editorial Assistant (currently handled by Editors)
    * This role needs to understand the editorial process and the tools being used.  They should not need the level of domain and community knowledge that the Editor needs
  * Technical Editor (e.g., Gail Pieper)
  * Design Advisor (e.g., Matt Stone)
  * Subject Matter Expert (depends on topic)

### Artifacts
  * Blog article
    * States: *draft, final, published*
    * Includes embedded metadata relevant to BSSw site
  * Hero image
    * States: *idea, draft, final, published*

### Tools and Resources
  * Production bssw.io site
    * https://bssw.io/blog_posts
  * Preview bssw.io site
    * https://preview.bssw.io/blog_posts
    * User and password required
  * bssw.io import trigger
    * Not advertised to prevent abuse
  * preview.bssw.io import trigger
    * Not advertised to prevent abuse
  * GitHub repository
    * https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/Articles/Blog

### Boundary Conditions
The process starts when an author delivers a draft blog article and hero image (or suggestion therefore).
<br>The process ends with a published blog article on BSSw.io.

### Process
*Iterations are possible at many points in this process and such “opportunities” should be pretty obvious.  We are not attempting to specifically capture them here.*

1. Author delivers draft article
2. Author delivers idea or draft for hero image 
3. *Need steps for hero image development* 
4. Editorial Assistant converts to Markdown (if required; could be delayed until some of the reviews are completed)
5. Editorial Assistant commits draft article to GitHub repository (if required; could be delayed until some of the reviews are completed)
6. Editor performs initial review of article and metadata
7. Editorial Assistant pulls article onto preview.bssw.io site
8. Editor determines reviews needed and specific reviewers for article. Likely reviews include:
  <br>a. Technical Editor
  <br>b. Design Advisor
  <br>c. Subject Matter Experts
9. Editorial Assistant requests indicated reviews and tracks to completion
10. Editor works with Author to address suggested changes to article, as appropriate
11. Editorial Assistant pulls near-final article onto preview.bssw.io site
12. Editorial Assistant asks Author to review and approve article on preview site
13. Author approves article
14. Editorial Assistant changes article metadata to publish and sets RSS date
15. Editorial Assistant pulls final article onto production bssw.io site
16. Editorial Assistant notifies Author, Editor, and other interested parties of publication

### Author Invite Template

*A template to append to an invitation to a prospective author for a blog article.*

* **Next Steps:**
  If you’d like to pursue writing an article, the first step would be to agree on a date for the draft that we can both put on our calendars.
  Below is some additional information about our process.
  Please feel free to reach out to the BSSw.io editorial staff if you have any questions.
  We look forward to working with you.

  Best, on behalf of the BSSw.io Editorial Board

* **Submission and Publication:**
  * By making a submission, you agree to [BSSw.io content licensing terms](https://github.com/betterscientificsoftware/bssw.io/blob/main/TERMS.md).
  * Blog articles appear here: <https://bssw.io/blog_posts> and are also announced in the monthly BSSw email digest (<https://bssw.io/pages/receive-our-email-digest>).
    You are certainly welcome to draw attention to your article through social media and other opportunities.
  * The BSSw.io site is backended by a GitHub repository.
    Articles are produced in markdown.
    If you're comfortable with git and GitHub, feel free to submit a pull request with the draft of your article.
      - A skeleton blog article that you can copy and customize is: <https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/Articles/Blog/BlogArticleSkeletonA.md>
      - Your PR should add the markdown file for your article as a new file in the blog (`Articles/Blog`) directory:  <https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/Articles/Blog>
  * Or of you prefer, you could instead provide text in some convenient format (e.g., MSWord) via email.
    Some authors prefer that approach.
  * We will work with you on the timeline.
    We sometimes schedule articles to come out in conjunction with some event – in advance, or as follow-up.
    But in the absence of a specific target, we’ll work it into our pipeline.
    Publication dates sometimes need to be revised, since we have multiple blog articles in flight.
  * We like to allow a minimum of three weeks from draft to publication, so that we have time for our review and technical editing process and also work together with our designers to develop an accompanying image (optional).

* **Content:**
  * Length is flexible.
    We generally want to keep these as a light read.
    We suggest length of 500-1,500 words, though both shorter and longer may be perfectly reasonable for some topics.
    You can peruse past blog postings to get a feel for what we’ve published in the past.
  * In the spirit of a *light read*, we ask you to limit your use of figures, tables, and links.
  * At the top of your article, we can include a *hero* image, which is also used as a background to highlight it as the newest article in the list of blog postings.
    This image is *optional*, but if you have ideas for an appropriate image please let us know.
    Many blog articles are published without hero images.
  * Guidelines for a *hero* image:
    - wide rectangular shape; we can crop an image to the required size (1125 x 432 pixels)
    - the design brief for our site focuses on three types of imagery for hero:
      - stock images (we have access to a number of stock photo libraries),
      - data visualizations, or
      - people in trainings, workshops, conferences, or other settings
    - *hero* images should contain no bold text; incidental text (in diagrams, for instance) is OK.
  * We request a brief bio for each of the authors
    - 50-100 words, in paragraph form, can include hyperlinks
    - Mention your current position, employer, a bit about your background
    - Include info about your interests related to software productivity and sustainability
    - Anything else you want to mention
  * We use GitHub profile information (particularly photo and affiliations) to construct our Site Contributors page: <https://bssw.io/items/authors/>.
    Please let us know your GitHub username.
    We encourage you to include a photo and up-to-date institutional affiliation in your GitHub profile.

{% include links.html %}
