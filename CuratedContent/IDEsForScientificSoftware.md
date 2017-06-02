# Integrated Development Environments (IDEs) for Scientific Sofware Development

IDEs have been used extensively for software development for many years, and in most software engineering domains, 
are considered best practice. However, their uptake for scientific software development, and in particular, high
performance computing (HPC), has been much slower. Nevertheless, IDEs are quite widely used, particularly where software
engineering professionals are actively involved in the development of scientific software.

When choosing an IDE for scientific software development, some important considerations include:

- Provides support for multiple languages, in particular, C/C++, Fortran, and Python.
- Does not interfere with existing build practices and toolchains.
- Integrates simply and smoothly with existing tools and systems.
- Is easily customizable to suit individual or team requirements.
- Works on a variety of platforms (Windows, Mac, Linux).
- Allows remote development.

The following sections describe IDEs that meet one or more of the requirements for scientific code development. 

## Free IDEs

### Eclipse CDT

### Eclipse PTP

### Code::Blocks

## Commercial/Proprietary IDEs

### CLion

### Visual Studio.NET

### Netbeans

## Language Support

| IDE               | C/C++ | Fortran | Python             |
|-------------------|:-----:|:-------:|:------------------:|
| Eclipse CDT       |   Y   |    N    |   Y<sup>1</sup>    |
| Eclipse PTP       |   Y   |    Y    |   Y<sup>1</sup>    |
| Visual Studio.NET |   Y   |    N    |   N                |
| Netbeans          |   Y   |    N    |   Y (since 8.1)    |
| CLion             |   Y   |    N    |   Y                |
| XCode             |   Y   |    N    |   Y<sup>2</sup>    |
| Code::Blocks      |   Y   |    N    |   Y<sup>3</sup>    |

1. Requires PyDev
2. Requires manual configuration
3. Requires 3rd party plugin

## Build Systems

| IDE               | Makefile | CMake              | autotools          |
|-------------------|:--------:|:------------------:|:------------------:|
| Eclipse CDT       |   Y      |    Y               |   Y                |
| Eclipse PTP       |   Y      |    Y               |   Y                |
| Visual Studio.NET |   Y      |    Y (since 2017)  |   N                |
| Netbeans          |   Y      |    Y<sup>1</sup> (since 8.2)   |   Y<sup>2</sup>  |
| CLion             |   Y      |    N               |   Y<sup>1</sup>    |
| XCode             |   Y      |    N               |   Y<sup>2</sup>    |
| Code::Blocks      |   N      |    N<sup>3</sup>   |   N    |

1. [Requires manual configuration](http://www.frankliuao.com/blogs/how-to-work-with-cmake-and-netbeans-8-2-or-newer-on-os-x/)
2. Requires 3rd party plugin
3. CMake can be used to generate Code::Blocks project files

## Platforms

## Misc
