# Generating Software Bill of Materials (SBOMs) in Scientific Software

**Hero Image:**

<img src='../../images/Blog_2312_SecurityB.png' />

#### Contributed by [William Hart](https://github.com/whart222)

#### Publication date: May 28, 2024

Software bills of materials (SBOMs) provide a list of the components, libraries, and modules that are required to build a piece of software. The [United States 2021 Executive Order on Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) highlights the role of SBOMs in supporting risk assessments for newly discovered vulnerabilities.  Further, the U.S. National Institute of Standards and Technology (NIST) released its [Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf), which requires SBOM information to be available for software. Both open-source and commercial software are impacted by these policies.  Consequently, developers of scientific software should expect that the use of their software may be restricted in some contexts unless accurate SBOMs can be generated. 
Conversely, as SBOMs become more widely available for scientific software, developers will also be able to use them to better understand the risks and vulnerabilities of the software on which they depend.

<img src='https://scribesecurity.com/wp-content/uploads/2022/01/sbom-components-scribe-security-768x451.jpeg.webp' class='page' />[Ingredients of a software bill of materials.  From ScribeSecurity.com]

The past few years have seen an industry-wide effort to embrace SBOMs and other software security practices highlighted by the U.S. government (see, for example, [this article](https://thenewstack.io/2023-the-year-open-source-security-supply-chain-grew-up/)).  Many tools have been developed to generate SBOMs for software repositories, filesystems, container images and other execution platforms. The [software bill of materials webpage](https://www.ntia.gov/page/software-bill-materials) maintained by the National Telecommunications and Information Administration provides an extensive set of resources on their creation and use, including the [Survey of Existing SBOM Formats and Standards (2021)](https://www.ntia.gov/sites/default/files/publications/sbom_formats_survey-version-2021_0.pdf) which describes the three widely used SBOM standards that have emerged.
Although SBOMS and other software security practices are not yet widely used in the scientific software community, policies for software security will increasingly impact scientific software too. **Consequently, developers of scientific software should begin learning about SBOMs and their role in software security best practices, and assess out how to provide and use them in their own development activities.**

In recent blog posts, I provide a critique of these capabilities in the context of scientific software libraries written in [Python](https://wehart.blogspot.com/2024/03/sboms-for-scientific-software-python.html) and [C++](https://wehart.blogspot.com/2024/03/sboms-for-scientific-software-c.html). Specifically, I explored whether mature tools exist to automate the generation of SBOMs for scientific software. 
Many of the tools discussed in the blog concerning SBOMs for [C++](https://wehart.blogspot.com/2024/03/sboms-for-scientific-software-c.html) can be used with other compiled scientific software languages, including Fortran and C.

Here is a synopsis of the key points from these blogs:

* Existing tools can easily generate SBOMs for simple Python packages. Simple Python packages without C extensions probably do not need to worry much about generating SBOMs.

* Developers should be clear about the distinction between required and optional dependencies.
  * Optional dependencies may not be captured in SBOMs.
  * Further, optional dependencies may be treated differently in different SBOM tools.

* It is unclear how to capture build dependencies in SBOMs for cython and other compiled software extensions.
  * Compiled dependencies are used in widely used Python libraries (e.g., numpy).
  * However, the SBOM tools I surveyed for Python focused on documenting software dependencies but not software builds.

* The SBOM tool ecosystem is much less mature for C++, Fortran, and other compiled languages used for scientific computing.

* C++ and Fortran developers should explore the use of package managers.
  * These naturally manage the relevant SBOM data, so package managers will likely play a key role in supporting software security practices.
  * However, only a couple of package managers currently automate the generation of SBOMs: vcpkg, conan and spack.
  * Of these, vcpkg has the strongest support for SBOMs (e.g., see [this Microsoft blog article](https://devblogs.microsoft.com/engineering-at-microsoft/generating-software-bills-of-materials-sboms-with-spdx-at-microsoft/)).

* Alternatively, C++ and Fortran developers can automate the generation of SBOMs within their build systems.
  * For example, the [cmake-sbom project](https://github.com/DEMCON/cmake-sbom) automates SBOM generation with build information the developer provides.

### Further information

* [SBOMs for Scientific Software: Python](https://wehart.blogspot.com/2024/03/sboms-for-scientific-software-python.html)
* [SBOMs for Scientific Software: C++](https://wehart.blogspot.com/2024/03/sboms-for-scientific-software-c.html)
* [NTIA Software Bill of Materials](https://www.ntia.gov/page/software-bill-materials)
* [United States Executive Order on Improving the Nation's Cybersecurity](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/)
* [NIST Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)

### Acknowledgment

This work was supported by the Better Scientific Software Fellowship Program, funded by the Exascale Computing Project (17-SC-20-SC), a collaborative effort of the U.S. Department of Energy (DOE) Office of Science and the National Nuclear Security Administration.

### Author bio

William Hart is a 2022 [BSSw Fellow](https://bssw.io/pages/meet-our-fellows) and researcher in the Center for Computing Research at Sandia National Laboratories. He managed the Data Science and Optimization Applications portfolio for the US DOE Exascale Computing Project (ECP). He is an expert in computational operations research, and he has developed solutions for cybersecurity, critical infrastructure protection, engineering design, sensor data analysis, drug design, nuclear nonproliferation and remote sensing applications. Additionally, he has made seminal contributions to a variety of impactful open-source software libraries, including Pyomo (R&D100, INFORMS Computing Prize), Canary (R&D100), IDAES (R&D100), Dakota, and PEBBL.

<!---
Publish: yes
Pinned: no
Track: deep dive
Topics: software engineering, software process improvement
--->
