# Modern Memory Safe C++?

#### Contributed by  [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication Date: March 30, 2026

<!-- begin deck -->
Modern C++ is safer than much of the C++ software written decades ago, but it is still not yet a memory-safe language by default.
This article surveys the practical work now underway in LLVM and the C++ standards process to reduce undefined behavior and that results in security and correctness bugs.
<!-- end deck -->

<img src='../../images/2026-03-modern-memory-safe-cpp-hero-image.jpg' class='page'/>

## Why memory safety matters

Of the CWE Top 25 Most Dangerous Software Weaknesses in 2025,<sup>[1]</sup> six are directly related to memory access errors in unsafe languages like C++: out-of-bounds write (5), use after free (7), out-of-bounds read (8), buffer copy without checking size of input (11), null pointer dereference (13), and stack-based buffer overflow (14).
(However, note that this is a significant reduction from the 2023 list where memory errors take the top three spots: use after free (1), heap-based buffer overflow (2), out-of-bounds write (3).<sup>[2]</sup>)
So while memory safety issues did not dominate the reported memory vulnerabilities in 2025, memory-safety bugs remain one of the most persistent sources of serious software defects and security vulnerabilities.
Even if software security is not a major concern for scientific and high-performance (HPC) codes, software correctness bugs caused by incorrect usage of memory is a major problem with the reliability of HPC software and causes some of the most challenging and expensive bugs to diagnose and fix.
Memory-related bugs in HPC C++ codes can escape testing and lay dormant for some time before causing problems in large/expensive simulation runs.

Large HPC codes are often long-lived, performance-sensitive, and deeply invested in C++ ecosystems and the primary tool for accelerated HPC software NVIDIA CUDA, which is basically an extension of the C++ language.
Rewriting everything in a different safer programming language is rarely realistic and not even viable in many cases due to the lack of tooling and libraries for safer languages.
Yet, continuing to accept unchecked undefined behavior in these HPC C++ codes is becoming harder to justify.

While there is no single switch that turns ISO C++23 (or proposed C++26) into a memory-safe language, there is now a substantial body of work that can make modern C++ materially safer, especially for spatial memory errors such as out-of-bounds access (which account for a substantial number of the reported software security vulnerabilities).
Much of the most concrete progress is happening around the LLVM and Clang compiler toolchain.

## What "modern C++" already provides for memory safety

Before looking at the newest compiler and library work, it is worth noting that the standard C++ library has already moved in a safer direction over several revisions.
C++11 gave developers a better ownership vocabulary with `std::unique_ptr`, `std::shared_ptr`, move semantics, `std::array`, and stronger RAII-based coding styles.
C++14 added `std::make_unique`, which made ownership transfer less error-prone.
C++17 added `std::string_view`, `std::optional`, `std::variant`, and `std::byte`, all of which helped replace ad hoc conventions with explicit types.
C++20 added `std::span`, ranges, and concepts.
C++23 added `std::mdspan` and `std::expected`, both useful for expressing intent more clearly in high-performance and systems code.

While consistent usage of those new classes eliminates many types of memory usage errors at compile time or at runtime, they do eliminate all undefined behavior.
And C++ code can enjoy the advantages of these standard abstractions if it is refactored to use them.
And the C++ standard along does provide the needed safety, compiler and library implementations need to provide the needed checks.

## LLVM Clang: Make existing C++ code safer

Large companies like Google, Apple, and others have made significant contributions to the LLVM Clang compiler stack to improve C++ memory safety.
Apple started the Clang Safe Buffers effort<sup>[3]</sup> where setting the compiler flag `-Wunsafe-buffer-usage` triggers diagnostics that identify pointer arithmetic, unchecked subscripting, and other patterns that often result in out-of-bounds indexing errors and pointer read/write errors.
The intended migration path is to wrap raw buffers in safer abstractions such as `std::span`, `std::vector`, `std::array`, or `std::string_view`, and to preserve bounds information across APIs instead of dropping back to pointer-plus-size pairs.
Clang also provides `[[clang::unsafe_buffer_usage]]` and `#pragma clang unsafe_buffer_usage` so teams can mark compatibility boundaries and adopt the model incrementally.

The second major piece is libc++ hardening<sup>[4]</sup> which was also started by Apple with major support from Google.
This hardening adds default always-on runtime checks to important standard-library operations so that some classes of undefined behavior become reliably diagnosed failures.
In today's libc++, hardened support already covers important facilities including `std::span`, `std::string_view`, `std::vector`, `std::string`, `std::mdspan`, `std::optional`, and `std::expected`, with several iterator checks available when ABI settings permit bounded iterators.
LLVM's C++ Safe Buffers documentation explicitly treats hardened libc++ and compiler diagnostics as complementary pieces of one programming model.

The third piece is static checking via the LLVM tool clang-tidy<sup>[5]</sup>.
Clang-tidy's `cppcoreguidelines` checks line up with the C++ Core Guidelines<sup>[6]</sup> and enforce proper usage of modern C++ types instead of raw pointers.
Those checks operationalize the Core Guidelines' bounds rules: avoid pointer arithmetic, avoid array-to-pointer decay, prefer `span`, and make ownership explicit.

While this is significant improvement over the usage of raw C++ pointers, this is not yet full memory safety.
But it is increasingly a real engineering path instead of just advice.
And existing unsafe C++ code can be incrementally refactored to use modern safe C++ types and eliminate the majority of undefined behavior that cases

## How these LLVM is being used to improve memory safety

Apple has become one of the most visible contributors and deployers of LLVM C++ memory safety work.
Its C++ language support page<sup>[7]</sup> documents that Xcode 16 added C++ standard library hardening for Apple Clang and `libc++`, with production-oriented modes such as `Yes (fast)` and `Yes (extensive)` as well as a stricter debug mode.
Apple's WWDC25 session *Safely mix C, C++, and Swift*<sup>[8]</sup> is especially revealing because it connects several strands into one developer workflow.

Google is pursuing the same LLVM direction at much larger deployment scale, and it has published some of the best public evidence that the approach can pay off.
In November 2024, Google reported on retrofitting spatial safety to hundreds of millions of lines of C++<sup>[9]</sup>.
After enabling hardened libc++ and rolling it out carefully, Google reported more than 1,000 bugs found, an estimated prevention of 1,000 to 2,000 new bugs per year at its current development rate, and a 30% reduction in its baseline segmentation-fault rate across production.
The same post claimed that LLVM hardened libc++ had already disrupted an internal red-team exercise and would have prevented another exploit path that predated deployment.
The WG21 paper P3471,<sup>[15]</sup> authored by Apple libc++ maintainers, cites Google's deployment experience and notes performance impact as low as 0.3%.

Google is not stopping with library hardening.
The company is expanding checking beyond the standard library and migrating code toward Clang Safe Buffers<sup>[3]</sup>.
Hardened containers catch misuse at access sites, while Safe Buffers aims to move APIs and data flow away from raw pointers so that bounds information is preserved instead of constantly discarded.

At the same time, Google has conceded that more work needs to be done.
In its March 2024 *Secure by Design* perspective on memory safety,<sup>[10]</sup> Google made the case that retrofitting protections into C++ is valuable but not sufficient.
In Android 13, for example, Google reported that annual memory-safety vulnerabilities had dropped from 223 in 2019 to 85 in 2022, and from 76% to 35% of Android's total vulnerabilities, while new native code increasingly moved to Rust and other memory-safe languages.

## The Core Guidelines and the standards pipeline

The C++ Core Guidelines<sup>[6]</sup> provide the best practices in the usage of newer C++ standards and standard library types to eliminate C++ memory errors.
Their bounds-safety profile says to not use pointer arithmetic, do not rely on array-to-pointer decay, prefer `span`, and avoid standard-library facilities that are not bounds-checked.
The guidelines also separate bounds safety, type safety, and lifetime safety.

That same separation is now showing up in WG21 (i.e. the ISO Working Group 21 for C++ standards) proposals.
Bjarne Stroustrup's P3274, *A framework for Profiles development*,<sup>[11]</sup> argues that the industry needs portable, tool-supported profiles that can offer guarantees rather than just style advice.
Related work includes Herb Sutter's P3081, *Core safety profiles for C++26*,<sup>[12]</sup> the initialization-focused P3402,<sup>[13]</sup> and Stroustrup's invalidation proposal P3446<sup>[14]</sup> for reducing dangling-pointer bugs.

The most concrete proposal with existing field experience is P3471, *Standard library hardening*.<sup>[15]</sup>
It proposes standardizing the idea of "hardened preconditions" so that operations such as out-of-range indexing on containers, `std::span`, and `std::mdspan` can become contract violations in hardened implementations rather than latent undefined behavior.

What does that mean for C++26 and C++29?
The answer, as of March 2026, is still evolving.
The committee discussion is active enough that it is safer to speak in terms of direction than guarantees.
One important paper, P3608, *Contracts and profiles: what can we reasonably ship in C++26*,<sup>[16]</sup> explicitly argues for a limited C++26 scope which includes a general profiles framework, standard library hardening, and a simple concrete profile that enables it, while postponing more ambitious profile machinery to post-C++26 work and likely C++29.
Newer papers such as Stroustrup's P3984<sup>[17]</sup> show that broader profile design is still moving.

So the likely near-term picture is incremental.
C++20 and C++23 already delivered safer vocabulary types such as `std::span` and `std::mdspan`.
C++26 may standardize more of the hardening framework around them.
C++29 is a plausible target for more mature C++ safety profiles if implementation experience arrives in time.

## How this compares with Rust

Discussions about C++ memory safety do not exist in a vacuum and almost always involves arguments for and against migrating C++ software to *The Rust Programming Language*.<sup>[18]</sup>
In Rust, ownership, borrowing, and slices are presented as core language mechanisms that enforce memory safety at compile time for safe Rust.
Unsafe operations are still possible, but they are pushed into explicitly marked `unsafe` regions.
Rust software is memory safe by construction if it compiles, but still requires runtime checks for certain operations like array bounds indexing (where the values of the indexes can't be proven to be in bounds at compile-time).

C++, by contrast, is assembling a layered system of safer library types, compiler diagnostics, runtime hardening, static analysis, and opt-in profiles.
Those layers are useful, but they do not make the language uniformly memory-safe, and they are easier to bypass accidentally or intentionally.

However, C++ has an advantage Rust does not in that it can be improved in place inside enormous deployed systems while preserving existing ABIs, interoperability, and performance envelopes.
That is why the LLVM work matters so much.
It offers a realistic migration path for codebases that will still be largely C++ for years.

For greenfield components that parse untrusted input or sit on critical attack surfaces, Rust often offers the cleaner answer.
For established scientific and HPC codebases, modern C++ plus LLVM hardening and guideline-driven cleanup may be the most feasible way to remove a large fraction of today's risk.

## Why pressure for memory safety is increasing

This technical work is happening in a government policy environment that is now openly focused on memory safety.
In the United States, Executive Order 14028, *Improving the Nation's Cybersecurity*,<sup>[19]</sup> signed on May 12, 2021, pushed federal attention toward software security and secure development practices.
That direction continued through the White House's 2023 National Cybersecurity Strategy, Executive Order 14144, *Strengthening and Promoting Innovation in the Nation's Cybersecurity*,<sup>[20]</sup> signed on January 16, 2025, and the June 6, 2025 amendment to that order.

The policy conversation has also become more explicit about language choice.
CISA's *Secure by Design* effort<sup>[21]</sup> now includes guidance such as *The Case for Memory Safe Roadmaps*.
That does not mean every C++ codebase must be rewritten.
It does mean the burden of proof has shifted.
Organizations are increasingly expected to show a credible plan for reducing memory-unsafe attack surface, whether by migration, hardening, safer subsets, or some combination of the three.

## A practical takeaway for scientific software teams

For research software groups, the most useful stance is probably neither denial nor panic.
Modern C++ can be made significantly safer today, but that requires conscious toolchain and API choices.

If you maintain a C++ codebase, a practical starting point is to target at least C++20 where feasible, prefer containers and views such as `std::vector`, `std::array`, `std::span`, `std::string_view`, and `std::mdspan`, enable `libc++` hardening in development and CI before wider deployment, and run `clang-tidy` with the relevant `cppcoreguidelines` bounds and ownership checks.
For code that still depends on raw pointers, Clang's `-Wunsafe-buffer-usage` offers a concrete migration path.
And for especially high-risk new components, it is increasingly reasonable to ask whether Rust is the better default.

The most honest answer to "Modern Memory Safe C++?" is therefore: not yet, and not completely, but substantially safer C++ is becoming practical.
The interesting part of the current moment is that this is no longer just a language-design conversation.
Apple and Google are shipping it, LLVM is enabling it, and the C++ standards process is trying to catch up.

## Author bio

Roscoe A. Bartlett earned a PhD in chemical engineering from Carnegie Mellon University, researching numerical approaches for solving large-scale constrained optimization problems applied to chemical process engineering.
At Sandia National Laboratories and Oak Ridge National Laboratory, he continued research and development in constrained optimization, sensitivity methods, and large-scale numerical software design and integration for computational science and engineering (CSE).
Dr. Bartlett currently focuses on software engineering challenges in CSE as well as the development of build, test, and integration software and processes for CSE.

<!---
 Publish: yes
 Track: Deep Dive
 Pinned: no
 Topics: programming languages, development tools
 RSS update: 2026-03-30
 --->


<!--- References --->

[cwe-top25-2025-sfer-ezikiw]: https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html "CWE Top 25 Most Dangerous Software Weaknesses in 2025"
[cwe-top25-2023-sfer-ezikiw]: https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html "CWE Top 25 Most Dangerous Software Weaknesses in 2023"
[clang-safe-buffers-sfer-ezikiw]: https://clang.llvm.org/docs/SafeBuffers.html "Clang Safe Buffers"
[libcpp-hardening-sfer-ezikiw]: https://releases.llvm.org/19.1.0/projects/libcxx/docs/Hardening.html "libc++ Hardening Modes"
[clang-tidy-sfer-ezikiw]: https://clang.llvm.org/extra/clang-tidy/ "clang-tidy"
[cpp-core-guidelines-sfer-ezikiw]: https://isocpp.github.io/CppCoreGuidelines/ "C++ Core Guidelines"
[apple-cpp-support-sfer-ezikiw]: https://developer.apple.com/xcode/cpp/ "Apple C++ language support in Xcode"
[wwdc25-safe-mix-sfer-ezikiw]: https://developer.apple.com/videos/play/wwdc2025/311/ "Safely mix C, C++, and Swift"
[google-spatial-safety-sfer-ezikiw]: https://security.googleblog.com/2024/11/retrofitting-spatial-safety-to-hundreds.html "Retrofitting spatial safety to hundreds of millions of lines of C++"
[google-secure-by-design-sfer-ezikiw]: https://security.googleblog.com/2024/03/secure-by-design-googles-perspective-on.html "Secure by Design: Google's perspective on memory safety"
[p3274-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3274r0.pdf "P3274R0"
[p3081-sfer-ezikiw]: https://isocpp.org/files/papers/P3081R2.pdf "P3081R2"
[p3402-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3402r2.html "P3402R2"
[p3446-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3446r0.pdf "P3446R0"
[p3471-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3471r4.html "P3471R4"
[p3608-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3608r0.html "P3608R0"
[p3984-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf "P3984R0"
[rust-book-slices-sfer-ezikiw]: https://doc.rust-lang.org/stable/book/ch04-03-slices.html "The Rust Programming Language: Slices"
[eo14028-sfer-ezikiw]: https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity "Executive Order 14028: Improving the Nation's Cybersecurity"
[eo14144-sfer-ezikiw]: https://www.federalregister.gov/documents/2025/01/23/2025-01548/strengthening-and-promoting-innovation-in-the-nations-cybersecurity "Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity"
[cisa-secure-by-design-sfer-ezikiw]: https://www.cisa.gov/securebydesign "CISA Secure by Design"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "CWE Top 25 Most Dangerous Software Weaknesses in 2025"
[2]: #sfer-ezikiw-2 "CWE Top 25 Most Dangerous Software Weaknesses in 2023"
[3]: #sfer-ezikiw-3 "Clang Safe Buffers"
[4]: #sfer-ezikiw-4 "libc++ Hardening Modes"
[5]: #sfer-ezikiw-5 "clang-tidy"
[6]: #sfer-ezikiw-6 "C++ Core Guidelines"
[7]: #sfer-ezikiw-7 "Apple C++ language support in Xcode"
[8]: #sfer-ezikiw-8 "Safely mix C, C++, and Swift"
[9]: #sfer-ezikiw-9 "Retrofitting spatial safety to hundreds of millions of lines of C++"
[10]: #sfer-ezikiw-10 "Secure by Design: Google's perspective on memory safety"
[11]: #sfer-ezikiw-11 "P3274R0"
[12]: #sfer-ezikiw-12 "P3081R2"
[13]: #sfer-ezikiw-13 "P3402R2"
[14]: #sfer-ezikiw-14 "P3446R0"
[15]: #sfer-ezikiw-15 "P3471R4"
[16]: #sfer-ezikiw-16 "P3608R0"
[17]: #sfer-ezikiw-17 "P3984R0"
[18]: #sfer-ezikiw-18 "The Rust Programming Language: Slices"
[19]: #sfer-ezikiw-19 "Executive Order 14028: Improving the Nation's Cybersecurity"
[20]: #sfer-ezikiw-20 "Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity"
[21]: #sfer-ezikiw-21 "CISA Secure by Design"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[CWE Top 25 Most Dangerous Software Weaknesses in 2025](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[CWE Top 25 Most Dangerous Software Weaknesses in 2023](https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Clang Safe Buffers](https://clang.llvm.org/docs/SafeBuffers.html)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[libc++ Hardening Modes](https://releases.llvm.org/19.1.0/projects/libcxx/docs/Hardening.html)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[clang-tidy](https://clang.llvm.org/extra/clang-tidy/)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Apple C++ language support in Xcode](https://developer.apple.com/xcode/cpp/)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Safely mix C, C++, and Swift](https://developer.apple.com/videos/play/wwdc2025/311/)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[Retrofitting spatial safety to hundreds of millions of lines of C++](https://security.googleblog.com/2024/11/retrofitting-spatial-safety-to-hundreds.html)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[Secure by Design: Google's perspective on memory safety](https://security.googleblog.com/2024/03/secure-by-design-googles-perspective-on.html)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[P3274R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3274r0.pdf)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[P3081R2](https://isocpp.org/files/papers/P3081R2.pdf)
* <a name="sfer-ezikiw-13"></a><sup>13</sup>[P3402R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3402r2.html)
* <a name="sfer-ezikiw-14"></a><sup>14</sup>[P3446R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3446r0.pdf)
* <a name="sfer-ezikiw-15"></a><sup>15</sup>[P3471R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3471r4.html)
* <a name="sfer-ezikiw-16"></a><sup>16</sup>[P3608R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3608r0.html)
* <a name="sfer-ezikiw-17"></a><sup>17</sup>[P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)
* <a name="sfer-ezikiw-18"></a><sup>18</sup>[The Rust Programming Language: Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
* <a name="sfer-ezikiw-19"></a><sup>19</sup>[Executive Order 14028: Improving the Nation's Cybersecurity](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity)
* <a name="sfer-ezikiw-20"></a><sup>20</sup>[Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity](https://www.federalregister.gov/documents/2025/01/23/2025-01548/strengthening-and-promoting-innovation-in-the-nations-cybersecurity)
* <a name="sfer-ezikiw-21"></a><sup>21</sup>[CISA Secure by Design](https://www.cisa.gov/securebydesign)
