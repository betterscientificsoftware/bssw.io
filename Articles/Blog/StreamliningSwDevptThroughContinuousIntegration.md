# Streamlining Software Development through Continuous Integration

#### Contributed by [Glenn Hammond](https://github.com/ghammond86 "Glenn Hammond's Github.io Profile")

#### Publication date: April 26, 2019

**Hero Image:**
- <img src="../../images/Blog_0419_SDwithCI.png" />[PFLOTRAN simulation of Iodine-129 migrating downgradient from a nuclear waste repository.  Image courtesy of Emily Stein, Sandia National Laboratories.]


Continuous integration facilitates sustainable software development when properly utilized.  Through continuous integration, source code and documentation can be automatically downloaded, compiled, tested, and deployed; and steps requiring human intervention are eliminated.  One potential challenge with continuous integration is the ongoing maintenance of supporting software and hardware infrastructure, which may be routine for IT specialists but bothersome for domain scientists. Within cloud computing, however, frameworks exist that greatly facilitate continuous integration, many of which are free to open source code development projects.

### Continuous integration within the PFLOTRAN project

The PFLOTRAN project has leveraged continuous integration since 2012, when automated unit and regression testing were implemented through Buildbot using pFUnit for unit testing and a custom Python-based regression testing framework.  PFLOTRAN is an open source, massively parallel reactive multiphase flow and transport simulator employed to simulate physical and chemical processes in the Earth's subsurface (https://www.pflotran.org).  Although PFLOTRAN unit and regression testing could be run locally from the command line by the developer, Buildbot was employed to ensure that all commits to the PFLOTRAN Bitbucket repository were tested.  A Buildbot daemon monitored the PFLOTRAN Bitbucket repository and launched a build/test sequence for all new commits.  However, Buildbot relied on access to dedicated local machines that required continual support (e.g., a Linux box residing in a researcher's office), and maintaining these machines was cumbersome.

In 2017, the PFLOTRAN project migrated its automated build/test sequence from Buildbot to Travis CI, a free service that eliminated hardware maintenance through the use of virtual machines in the cloud.  Today, all commits to the master branch of PFLOTRAN on Bitbucket are automatically built and tested by Travis CI (https://travis-ci.org/pflotran/pflotran), and errors are reported immediately to developers by email.  In addition, code coverage for the unit and regression tests is reported through Codecov (https://codecov.io/gh/pflotran/pflotran), which integrates seamlessly with Travis CI.  

### Eliminating manual updates for documentation

Another challenge for the project was the manual approach to updating the development version of PFLOTRAN's documentation hosted online (e.g., theory guide, user guide).  Documentation is written in reStructuredText and compiled to HTML (or PDF) using Sphinx.  Prior to fall 2018, each update to the documentation required a manual Sphinx compilation and upload to the cloud-based server hosting the PFLOTRAN website.  Because of the manual steps for updating, the development version of documentation continually lagged behind the implemented functionality in the code.  In order to resolve this issue, continuous integration was implemented through CodeShip and Docker.  All commits to the master branch of the PFLOTRAN documentation repository on Bitbucket spawn builds on CodeShip; and upon successful completion, the documentation is automatically uploaded to the PFLOTRAN website.  Failures are reported to the developer.  PFLOTRAN’s development version of the quality assurance (QA) framework functions similarly with the building of PFLOTRAN and running of QA tests executed prior to the build and deployment of QA documentation.

### Leveraging open source options

The various cloud-based continuous integration frameworks utilized above have their tradeoffs for open source projects.  For instance, currently Travis CI is linked only to GitHub but provides unlimited free builds, whereas CodeShip is linked to Bitbucket, GitHub, and Gitlab but is limited to 100 free builds per month.  For Bitbucket users, CodeShip may be preferable because of its linkage with Bitbucket.  However, we chose to continue unit and regression testing with Travis CI because of the unlimited builds (documentation requires far fewer than 100 builds per month).

The use of cloud-based continuous integration within the PFLOTRAN project has greatly increased confidence in code robustness and reduced the time spent manually uploading documentation to the code's website.

This approach is summarized in a poster presented at the SIAM CSE19 conference, titled 
<a href="https://doi.org/10.6084/m9.figshare.7761950.v1">_A look at PFLOTRAN's cloud-based continuous integration_</a>.

### Resource summary for this work

* Bitbucket: https://bitbucket.org 
* Codecov: https://codecov.io
* CodeShip: https://codeship.com
* PFLOTRAN: https://www.pflotran.org
* Travis CI: https://travis-ci.org

### Author bio

Glenn is a computational geohydrologist and one of the principal developers of PFLOTRAN, a massively parallel simulator for modeling reactive multiphase flow and transport processes in the subsurface.  He earned a B.S. in civil engineering from Brigham Young University and an M.S. and Ph.D. in civil and environmental engineering from the University of Illinois at Urbana-Champaign, where he was a U.S. Department of Energy Computational Science Graduate Fellow.  Glenn is a principal member of the technical staff at Sandia National Laboratories and has worked at DOE national laboratories his entire professional career. 


<!---
Publish: yes
RSS update: 2019-04-26
Track: experience
Topics: testing, continuous integration testing, documentation
Pinned: no
---!>

<!---
SAND #: SAND2019-4553 S
Image owned or licensed by Sandia

Sandia National Laboratories is a multimission laboratory managed and operated by National Technology & Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of Honeywell International Inc., for the U.S. Department of Energy's National Nuclear Security Administration under contract DE-NA0003525.
--->
