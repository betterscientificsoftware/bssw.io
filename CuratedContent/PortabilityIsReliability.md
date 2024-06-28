# Portability is Reliability
<!--deck text start-->
Portability can be a means to an end and does not need to be not an end in and of itself.
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")
#### Publication date: May 13, 2024

Resource information | Details 
:--- | :--- 
Article Title | [Portability is Reliability](https://evan.nemerson.com/2021/05/04/portability-is-reliability/)
Author | [Evan Nemerson](https://github.com/nemequ)
Focus | Testing, Software sustainability, Reliability

In this article, the author highlights a number of ways in which compiling and running code with different compilers and architectures improves the quality and reliability of the code.
Different compilers are better at manifesting and catching different kinds of issues.
The article mentions, for example, that clang often catches a larger set of issues than does gcc.
The article also explains that, in spite of challenges in using MSVC, one of the great advantages of compiling with it may be its static analyzer, which, in the author's opinion, may be the best part of the MSVC compiler.

The article also explains the importance of doing development with as many compiler warnings enabled as possible using flags such as `-Wall`, `-Wextra`, `-Weverything` and `-Werror` or `/W4` for MSVC.
By including compilation with strict warningns enabled and with different compilers in CI, it is possible to catch and prevent a lot of issues before they make it into a committed version of the code.

The author also mentions the value in using different architectures such as armv7 (which is more strict about aliasing violations) or s390x (which is a big endian architecture) to help shake out issues with code. Using various available compilers and architectures (as containers for example) on a code base is a great way to take advantage of some available automation to find and prevent issues from creeping into a code base.

<!---
Publish: yes
Topics: Testing, Software sustainability, Reliability
Pinned: no
RSS update: 2024-05-13
--->
