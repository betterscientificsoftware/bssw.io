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

## How companies and organizations are using LLVM to improve memory safety

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
Bjarne Stroustrup's P3274, *A framework for Profiles development*,<sup>[11]</sup> argues for portable, tool-supported profiles that can offer guarantees rather than just style advice, while related papers such as P3081,<sup>[12]</sup> P3402,<sup>[13]</sup> and P3446<sup>[14]</sup> explore specific safety directions.
The most concrete C++26 proposal with existing deployment experience is P3471, *Standard library hardening*,<sup>[15]</sup> which standardizes "hardened implementations" and "hardened preconditions" so that operations such as out-of-range indexing on containers, `std::string_view`, `std::span`, and `std::mdspan` become contract violations instead of silent undefined behavior.

P3608, *Contracts and profiles: what can we reasonably ship in C++26*,<sup>[16]</sup> argued for a minimalist package: ship the Contracts MVP, ship library hardening, and use a standardized profile mechanism to enable that hardening.
As of March 2026, after the February 2025 Hagenberg meeting and later review, the draft standard adopted the first two pieces but not the third.
C++26 now includes the Contracts MVP with `pre`, `post`, and `contract_assert`, while deliberately leaving out contracts on virtual functions and function pointers to keep the feature set narrow.
It also includes library hardening via hardened preconditions checked at runtime in hardened implementations.
What did not make C++26 is the profiles framework itself: broader profiles work, including the framework and core safety profiles, has been deferred to later standardization work, likely C++29.
In practice, that means C++26 hardening is enabled by implementation-defined mechanisms such as compiler flags rather than standard `profile` syntax.
P3608 also argued for termination-oriented behavior; in the draft, hardening failures are specified as contract violations, so the exact handling follows the selected contract semantics.

## How this compares with Rust

Discussions about C++ memory safety do not exist in a vacuum and almost always involves arguments for and against migrating C++ software to *The Rust Programming Language*.<sup>[18]</sup>
In Rust, ownership, borrowing, and slices are presented as core language mechanisms that enforce memory safety at compile time without need for runtime garbage collection.
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

## Potential for memory-safe C++ in the future?

One useful way to think about current strategies for C++ memory safety is as a stack of complementary defenses, each aimed at a different source of memory-related undefined behavior.
Clang Safe Buffers and Core-Guidelines-oriented `clang-tidy` checks can drive raw-pointer buffer manipulation out of ordinary code and replace it with standard C++ containers and views that preserve bounds information across APIs.<sup>[3],[5],[6]</sup>
The libc++ hardening already turns many out-of-range operations on standard-library types into diagnosed failures rather than silent undefined behavior,<sup>[4],[15]</sup> and a future stronger runtime (debug) checking mode could plausibly go further by tracking the lifetime of views and iterators in the style of the Teuchos `ArrayRCP` and `ArrayView` debug-mode checking, which demonstrated that dangling-view and invalidated-reference errors can be caught reliably at runtime with tolerable development-time overhead.<sup>[22]</sup>

The C++ standards work suggests how the remaining major categories could be addressed more systematically.
A future profiles framework could combine `std::bounds` to inject bounds checks, `std::lifetime` to reject manual `delete` and `free` and to check null dereference, and `std::initialization` to verify that objects are initialized before use.<sup>[11],[12],[13]</sup>
That same direction could then be extended with a `std::type` profile to restrict unsafe casts and wrong-type access, plus an invalidation profile to prevent use of iterators, pointers, references, and views after a container mutation or destruction.<sup>[14],[17]</sup>
Together with custom `clang-tidy` checks that disallow persisting raw C++ references and with future LLVM lifetime and invalidation analysis, that points to a subset of single-threaded C++ that could come reasonably close to being memory safe in practice even if the full language remains outside that guarantee.<sup>[5],[6],[11]</sup>

What would still remain are the places where C++ must deliberately escape that checked subset: low-level runtime and library internals, interoperability layers with C, Fortran, CUDA, and operating-system APIs, custom allocators and raw-storage manipulation, and any code that explicitly suppresses safety checks for compatibility or performance reasons.<sup>[11],[22]</sup>
In that sense, the most plausible future is not that every corner of ISO C++ becomes uniformly memory safe, but that tool-enforced safe regions become large enough that most scientific application code can be written in a style where memory-related undefined behavior is rare, diagnosable, and mostly confined to trusted boundary code.

But in the end, it is impossible for complex general programs to both be 100% safe and also run at the maximum possible performance.
Even many Rust programs contain some `unsafe` code in order to achieve the necessary performance.<sup>[23]</sup>
And there will always be the need to hand-off data between different libraries that increases the surface area for adding memory-related defects.
Therefore, there will always be a tradeoff between features, performances, and safety.
And from a correctness and security perspective, even if you eliminate all memory errors, you still are left with 19 of the CWE Top 25 Most Dangerous Software Weaknesses in 2025.<sup>[1]</sup>

## A practical takeaway for scientific software teams

For research software groups, the most useful stance is probably neither denial nor panic.
Modern C++ can be made significantly safer today, but that requires conscious toolchain and API choices.

If you maintain a C++ codebase, a practical starting point is to target at least C++20 where feasible, prefer containers and views such as `std::vector`, `std::array`, `std::span`, `std::string_view`, and `std::mdspan`, enable `libc++` hardening in development and CI before wider deployment, and run `clang-tidy` with the relevant `cppcoreguidelines` bounds and ownership checks.
For code that still depends on raw pointers, Clang's `-Wunsafe-buffer-usage` offers a concrete migration path.

The most honest answer to "Modern Memory Safe C++?" is therefore: not yet, and not completely, but substantially safer C++ is becoming practical.
The interesting part of the current moment is that this is no longer just a language-design conversation.
Apple and Google are shipping it, LLVM is enabling it, and the C++ standards process is trying to catch up.

## The impact of artificial intelligence

As this article is being written, it is impossible to ignore the impact that artificial intelligence (AI), large language models (LLMs), and AI coding agents will have in this area.
It is likely that in the next few years, improved AI models and coding agents will automate much of the work to flesh out the tooling for memory-safe C++ and incrementally refactor existing legacy C++ codebases to use memory-safe C++ idioms.
While any changes to existing software can be risky, the incremental approach to refactor existing C++ code is likely much lower risk that trying to completely rewrite large complex codebases (e.g. from C++ to Rust).
It will likely take artifical super intelligence (AGI) to rewrite complete legacy codebases from C++ to Rust, but much less capable AI models and tools can likely incrementally refactor C++ code.
We may not even need complete artifical general intelligence (AGI) to achieve that.
It will be fascinating to see what is possible in the next few years to automate away memory safety issues in legacy C++ codes.

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
[p3274-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3274r0.pdf "P3274R0: A framework for Profiles development"
[p3081-sfer-ezikiw]: https://isocpp.org/files/papers/P3081R2.pdf "P3081R2: Core safety profiles for C++26"
[p3402-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3402r2.html "P3402R2: A Safety Profile Verifying Initialization"
[p3446-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3446r0.pdf "P3446R0: Profile invalidation - eliminating dangling pointers"
[p3471-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3471r4.html "P3471R4: Standard library hardening"
[p3608-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3608r0.html "P3608R0: Contracts and profiles: what can we reasonably ship in C++26"
[p3984-sfer-ezikiw]: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf "P3984R0: A type-safety profile"
[rust-book-slices-sfer-ezikiw]: https://doc.rust-lang.org/stable/book/ch04-03-slices.html "The Rust Programming Language: Slices"
[eo14028-sfer-ezikiw]: https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity "Executive Order 14028: Improving the Nation's Cybersecurity"
[eo14144-sfer-ezikiw]: https://www.federalregister.gov/documents/2025/01/23/2025-01548/strengthening-and-promoting-innovation-in-the-nations-cybersecurity "Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity"
[cisa-secure-by-design-sfer-ezikiw]: https://www.cisa.gov/securebydesign "CISA Secure by Design"
[teuchos-memory-management-sfer-ezikiw]: https://bartlettroscoe.github.io/publications/TeuchosMemoryManagementSAND.pdf "Teuchos Memory Management Classes paper"
[against-the-void-rust-unsafe-sfer-ezikiw]: https://arxiv.org/pdf/2404.02230v1 "'Against the Void': An Interview and Survey Study on How Rust Developers Use Unsafe Code"
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
[11]: #sfer-ezikiw-11 "P3274R0: A framework for Profiles development"
[12]: #sfer-ezikiw-12 "P3081R2: Core safety profiles for C++26"
[13]: #sfer-ezikiw-13 "P3402R2: A Safety Profile Verifying Initialization"
[14]: #sfer-ezikiw-14 "P3446R0: Profile invalidation - eliminating dangling pointers"
[15]: #sfer-ezikiw-15 "P3471R4: Standard library hardening"
[16]: #sfer-ezikiw-16 "P3608R0: Contracts and profiles: what can we reasonably ship in C++26"
[17]: #sfer-ezikiw-17 "P3984R0: A type-safety profile"
[18]: #sfer-ezikiw-18 "The Rust Programming Language: Slices"
[19]: #sfer-ezikiw-19 "Executive Order 14028: Improving the Nation's Cybersecurity"
[20]: #sfer-ezikiw-20 "Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity"
[21]: #sfer-ezikiw-21 "CISA Secure by Design"
[22]: #sfer-ezikiw-22 "Teuchos Memory Management Classes paper"
[23]: #sfer-ezikiw-23 "'Against the Void': An Interview and Survey Study on How Rust Developers Use Unsafe Code"
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
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[P3274R0: A framework for Profiles development](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3274r0.pdf)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[P3081R2: Core safety profiles for C++26](https://isocpp.org/files/papers/P3081R2.pdf)
* <a name="sfer-ezikiw-13"></a><sup>13</sup>[P3402R2: A Safety Profile Verifying Initialization](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3402r2.html)
* <a name="sfer-ezikiw-14"></a><sup>14</sup>[P3446R0: Profile invalidation - eliminating dangling pointers](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3446r0.pdf)
* <a name="sfer-ezikiw-15"></a><sup>15</sup>[P3471R4: Standard library hardening](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3471r4.html)
* <a name="sfer-ezikiw-16"></a><sup>16</sup>[P3608R0: Contracts and profiles: what can we reasonably ship in C++26](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3608r0.html)
* <a name="sfer-ezikiw-17"></a><sup>17</sup>[P3984R0: A type-safety profile](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)
* <a name="sfer-ezikiw-18"></a><sup>18</sup>[The Rust Programming Language: Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
* <a name="sfer-ezikiw-19"></a><sup>19</sup>[Executive Order 14028: Improving the Nation's Cybersecurity](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity)
* <a name="sfer-ezikiw-20"></a><sup>20</sup>[Executive Order 14144: Strengthening and Promoting Innovation in the Nation's Cybersecurity](https://www.federalregister.gov/documents/2025/01/23/2025-01548/strengthening-and-promoting-innovation-in-the-nations-cybersecurity)
* <a name="sfer-ezikiw-21"></a><sup>21</sup>[CISA Secure by Design](https://www.cisa.gov/securebydesign)
* <a name="sfer-ezikiw-22"></a><sup>22</sup>[Teuchos Memory Management Classes paper](https://bartlettroscoe.github.io/publications/TeuchosMemoryManagementSAND.pdf)
* <a name="sfer-ezikiw-23"></a><sup>23</sup>['Against the Void': An Interview and Survey Study on How Rust Developers Use Unsafe Code](https://arxiv.org/pdf/2404.02230v1)
