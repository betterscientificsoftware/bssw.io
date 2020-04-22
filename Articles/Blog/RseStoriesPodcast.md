# Research Software Engineer Stories

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_RseStoriesPodcast.png' />
 
#### Contributed by [@vsoch](https://github.com/vsoch "@vsoch on GitHub")

#### Publication date: April xx, 2020

### We look to experts for knowledge, but do they know the whole picture?

I woke up one morning in September 2019 with something on my mind. I have read several
papers and heard talks and other "academically approved" presentation formats that purport to define what
a research software engineer (RSE) is. But the definitions don't reflect my experience.
Nor do they reflect the experiences of many of my peers. Instead, they present a  narrow
understanding of a role that is immensely rich and changing. I have seen RSEs working at national and academic labs, involved in everything from documentation and user support to high-performance computing and
open source development. 
What I see in the real world
doesn't reflect what the experts are advocating -- research software engineers do not
always exist on some dimension between software engineer and researcher.

### If there is missing information, where can we find it?

This of course isn't a new problem.  I have been chewing on it for a few months now.
How can we best define what an RSE is --  not from some select pool of experts, but 
from RSEs themselves? I first ventured into tool building: I \ created the 
[RSE Phenotype Generator](https://rseng.github.io/rse-phenotype/) and tried to
encourage people to use it. They largely didn't. I also tried encouraging them to write
stories about their work, but people just didn't have the time to sit down and write a small article.
I then spent a few weeks writing down all the different kinds of research software
engineers that I knew about, and I created a video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/trAfA9VWLTQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

That still reflected my oen narrow life experience -- I could never imagine the stories
that I'm just not familiar with. It wasn't good enough. 
I needed a mechanism that allows the research software engineers to tell their own stories without 
requiring much of their time. And I wanted a format in which the stories would be easy to digest, not overewhelming
us with yet more reading material. Then the answer hit me -- and it was such a simple idea. 
Whether we go for a run
or embark on a daily commute, the podcast is  music
for our ears. And so I decided -- without much thought about
the immense amount of work it takes to devise, manage, and maintain a podcast, 
schedule people, edit audio, and edit it again -- that I would create such a podcast.

### How do we do something we've never done before?

When in doubt, ask the internet, and look to the tools that you already know and use.
I figured that I could post the podcast as a static site on [GitHub](https://github.com/usrse/rse-stories), 
deployed via GitHub pages to render at [https://us-rse.org/rse-stories/](https://us-rse.org/rse-stories/).
I needed to do a small amount of searching to figure out what kind of feed was needed for itunes
and then how to register it. For recording technology, I went to the tools that I had
and wound up using a Zoom meeting to record the audio and  [Audacity](https://www.audacityteam.org/) to edit it.
And that largely was it! I follow the guideline "Do one's best and stay away from striving
for perfection, especially with audio recording and editing." The RSE Stories podcast,
being dobne entirely  by one software engineer, is not going to be on the same
level as some of my favorite (professionally created) podcasts, but this is OK. 

### So what is a research software engineer?

To me, being a research software engineer 
isn't about being handed a script to optimize, a container to build, or a package to write tests for. Being an RSE is about
predicting the future. It was what motivated me, back in 2014, when I realized that Docker was an amazing container technology and that I needed
to do whatever was necessary to get it working on high-performance computers. Yes, being an RSE is hugely about open source development
and taking charge of even the tiniest of bugs that you see hindering the communities that you serve.
But it's also  taking the risk to get involved with new communities that you see might be beneficial for making discoveries in science. 
It's about understanding the human element and putting time into undervalued resources like documentation. It's about making
experiences fun and teaching people that it's okay to ask for help. It's about being okay that 98 out of the 100 things you
try will not change how people think. Given the current state of the world, it's also about advocating for yourself,
taking care of yourself, and knowing when to say no or step away from something that is no longer meaningful to your
community or to you personally. If you have a vision for how you want the world to be, you have to be proactive -- and passionate. 
It's easy to get distracted by the trending technologies of the moment and trying to fit into a mold for how
you think you are expected to be. I know that these hard-working engineers, dreamers, and advocates are out 
there, and this is what I find so inspiring and what compells me to continue the podcast.

### Where is the podcast?

The episodes are released via a feed that plugs right into itunes, so you can
find it on [Apple Podcasts](https://podcasts.apple.com/us/podcast/rse-stories/id1481504497)
or discover it using your favorite podcast subscription service. The episodes are also
available on the main [RSE Stories](https://us-rse.org/rse-stories/) website,
and announced at time of publication on [@vsoch](https://twitter.com/vsoch/)'s Twitter,
and often the US-RSE and UK-RSE slack channels.

### What I've learned about producing podcasts

Along with hugely expanding my understanding of what an RSE is, I've learned a lot of
technical and social tidbits by way of working on the RSE Stories podcast. I'd like
to share a few of them quickly here:

 - Being social can produce anxiety, but I've learned that if I regularly expose myself to recording, it actually gets easier and I enjoy it. Introverts of the world, listen up! Adding a routine that puts you slightly out of your comfort zone can have unexpected positive benefits.
 - It's good to know a little in advance about the person you are interviewing, so that you are ready to ask questions. Some people can speak fluidly about their work, while others will provide only short answers, making your ability to ask good questions hugely important.
 - Every endeavor takes time. Here's another guidelingeI follow: "You have to make time for the things that you care about." This podcast falls into that bin for me, and I hope that in time others might be interested in helping and recording episodes.
 - For software, you don't need much more than [Audacity](https://www.audacityteam.org/) and a [episode feed](https://github.com/USRSE/rse-stories/blob/master/pages/episodes.rss) to give your podcast life.  
 - Regarding technology, it's best for both to record in a quiet, and small room, with minimally a headset with mic.

If you are interested in being featured on RSE Stories, you can read more information about
the podcast and express interest [here](https://us-rse.org/rse-stories/about/). What are you waiting for?
Let's share your story!


### Author bio

Vanessa Sochat is a research software engineer for the Stanford Research Computing Center. She received her Ph.D. in biomedical informatics in 2016 at Stanford and stayed at Stanford to focus on open source software development for scientific reproducibility. Her work includes development of container technologies, workflow software, and recipes for continuous integration. She is passionate about programming and system design and continues to run the Singularity Hub container registry and maintain a large set of open source libraries. When not programming, Vanessa can be found eating avocados, recording podcast episodes or  videos, making dinosaur noises, and running outside in the snow.


<!---
Publish: No
Categories: reliability
Topics: rseng
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
