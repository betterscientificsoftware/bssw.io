# Software Engineers and Scientific Software

#### Contributed by [Roger A. Rubio](https://github.com/TheSnapman)

#### Publication date: March 12, 2025

<!--deck start-->
To work together more effectively, software engineers and scientists should know a few things about each others' business.
<!--deck end-->

(This article is based on a presentation given at NLIT 2024.)

*Scientific software* is software that models and simulates real-world phenomena.  This type of software is often written by scientists, engineers, analysts, and mathematicians (SEAMs).  These professionals often find themselves in charge of writing code, even though software development isn't their desired area of expertise.

Barring formal training in software engineering, SEAMs often approach coding scientifically: they use an iterative and experimental approach to code and its functionality.  While this approach is valuable, it's insufficient for creating sustainable and user-friendly software.

Software engineers leverage established principles and practices -- much like scientists use physical laws and mathematical theorems -- to build robust and reliable software.  But if they fail to comprehend the true reasons for the existence of the software in the first place, they can appear dogmatic and unreasonable to SEAMs who may see software as only one part of addressing a real-world problem.

SEAMs must understand that there is more to creating sustainable software than meets the eye, and software engineers must understand the science behind the software and the users that use it.

### What SEAMs should understand

Software engineers focus on creating code that not only meets user needs but remains maintainable and adaptable over time.  Software engineers use the following principles to make sure their code is effective and sustainable:

- Modularity
- Cohesion
- Information hiding and abstraction
- Managing coupling
- Separation of concerns

#### Modularity

Software should be organized as modules -- or distinct packages of code -- that can easily interact with other modules through well-defined interfaces.  Theoretically, software modules can be taken from one area of the code and be used in another area without major changes.  SEAMs should strive to create modular code with either conventions or standard interfaces so that simpler components can be used to build complex software applications.

An e-commerce application provides a simple, widely-understood non-science example.  In this case, it is a good idea to create modules that handle the following functions:

- User authentication
- Product catalog
- Shopping cart
- Payment gateway
- Order management

The payment gateway code will be different from the user authentication code.  But there should be a well-defined interface between these two modules, as users who are not authenticated should not have access to the payment gateway.

#### Cohesion

Cohesion is when materials stick to similar materials, such as when water droplets cohere to other water droplets.  Cohesion is achieved in software when code has a common purpose.  SEAMs should place code that performs similar functions in the same physical or logical area.

Math libraries, such as finite element solvers, vectors and matrices, statistics, and others, often provide good examples of cohesion in the scientific software context. Finite element methods like the Galerkin method, Euler's method, and the Runge-Kutta method can be placed with other methods into one library to achieve cohesion.  But other aspects of an application will be more readily understood and used if they're also arranged in a cohesive manner.

#### Information hiding and abstraction

Information hiding and abstraction involves obscuring internal implementation details from the outside world.  Instead, a contract or promise is provided that programmers can focus on instead.  This strategy ensures that dependencies are not created on internal implementations of code.  In theory, code can be removed and replaced without breaking code that uses it as long as the replacement code provides the same abstraction.

For example, a driver need not understand how automotive braking systems work in order to stop a car.  Behind the scenes, the braking system employs the pedal, a master cylinder, calipers or drums, brake shoes, rotors, motion sensors, computer chips, and in the case of hybrids, the engine itself.  A significant amount of information is involved in braking in modern-day cars, and all of it is hidden from the driver.  The brake pedal is the abstraction for the car's braking system.

#### Managing coupling

Coupling measures the degree of dependency amongst disparate software components.  If a component depends on another component to a high degree, the coupling is tight.  If a dependency is low degree, then it is loose.  Tight coupling makes software hard to change, test, and reuse.  Loose coupling does not solve dependency problems outright, but the looser the coupling, the easier it is to deal with.  This is why coupling is always managed, not completely eliminated.

For example, JSON and XML are common data-interchange formats used on the web.   Imagine a user authentication module uses XML internally to format user data.  If this module needs to process a JSON message, it would have to translate JSON into XML in order to do its work.  The user authentication module is tightly coupled to XML as a data representation.  To loosen the coupling, the module could be modified to only accept the user data it needs in the programming language's basic data types, allowing the XML (and JSON) modules to be futher separated from the authentication module.

#### Separation of concerns

In software design, separation of concerns organizes code by major function, such as security, networking, logging, or storage. While cohesion groups related code within a component, separation of concerns ensures each component has a distinct responsibility.  SEAMs should apply loose coupling, high cohesion, and high modularity to the design of the major functional areas of their software.

In a simple web application, for example, the concerns are usually the user interface, the business logic, and persistent storage:

- The user interface deals with the user
- The business logic contains the core logic of the application
- The persistent storage contains code to create, read, update, and delete data from a persistent source of storage

### What software engineers need to understand

Software engineers working on scientific software can't focus only on the code.  They must understand the fundamental science and models behind the software to at least some degree in order to effectively collaborate with SEAMs and create truly sustainable software.

A SEAM is typically focused on the following concerns:

- Developing discretized *models*
- Translating models into *algorithms*
- Coding algorithms using a programming language
- Performing validation to ensure that the model is correctly modeling the physical phenomena of interest
- Performing verification to ensure that the computational model is working correctly
- Improving performance on different computing platforms

Since the major concerns of SEAMs *include* software but are *not exclusively*  software, software engineers need to understand the the context of their work.

### Models

Models form the heart of scientific software and are responsible for reproducing reality as accurately as possible.  How the software will be used depends greatly on the accuracy and credibility of the model and its implementation, so SEAMs spend a lot of time and effort trying to get the model right.

For example, weather models are used to create forecasts.  They rely on initial conditions, boundary conditions, physical processes, and numerical methods.  They depend on thermodynamics, fluid dynamics, and mass conservation.  Observations are combined with the model's predictions to improve accuracy.  Some models are global, while others are regional.  Meteorologists often vary the initial conditions to see how the forecast changes.  They are usually aware of the strengths and weaknesses of each model, as well as their biases, so they use their experience to choose the most likely forecast.

Software engineers should be aware of any and all issues related to the model's use and credibility in order to do their job effectively.

### Performance

SEAMs worry more about the platform the software will run on than software engineers do.  Scientific calculations are very often complicated and time-consuming (even for computers), so SEAMs try to squeeze out as much performance as they can.  Enhancing performance often involves taking advantage of specialized computer architectures.  Customizing code to work well on one computer architecture can make it hard to port it to other architectures.  SEAMs find themselves repeating this exercise when technology breaks backward compatibility.  Forward-looking SEAMs try to create software that is as future-resistant as possible.

Before the El Capitan supercomputer was made available to developers, scientific code had been designed to work with separate CPU and GPU devices, each with separate memory spaces.  El Capitan introduced accelerated processing units (APU's), which combine a CPU, GPU, and  shared memory onto one architecture.  Code that performed well with separate memory spaces could perform better with the APU's shared memory space.  So SEAMs found themselves rewriting code again.

#### Verification and validation (V&V)

Verification and validation (V&V) are complementary processes that work together to ensure the quality and reliability of scientific software.  V&V ensures accuracy, reliability, safety, compliance, and reproducibility.  Many aspects of V&V overlap with software engineering testing principles, such as functional testing, usability testing, and performance testing.  But software engineers need to be aware that V&V relates to the science behind the code as well as the code itself.  Verification ensures that the code does what it was intended to do -- that it implements the scientific model as intended.  Validation ensures that the model appropriately matches the real-world phenomena it was intended to represent.

#### Uncertainty quantification (UQ)

Uncertainty quantification (UQ) is a process of assessing and managing uncertainties in computational models and simulations.  UQ aims to determine how likely certain outcomes are when some aspects of the system or model are not completely known, subject to stochastic fluctuations, or when only incomplete information is available for certain aspects of the system.  UQ is essential for validating and verifying computer models, enabling scientists to make precise statements about the degree of confidence they have in their simulation-based predictions.  Software engineers need to able to help SEAMs generate a healthy level of confidence in the software by reducing uncertainty in the code and guiding SEAMs on.

### Users

SEAMs deal with a higher class of user than software engineers do: a user that understands the science behind the software and how it should behave.  Scientific software builds a reputation for trustworthiness as it is used and re-used to formulate and evaluate scientific conclusions.  If scientific software produces one result in one version and a different result in another version, its trustworthiness can be questioned, and its reputation can suffer.

Software engineers cannot assume scientific software is for the general public or for users who do not know (or care) how the software works.

### Conclusion

While SEAMs bring invaluable knowledge of the real-world phenomena being modeled, software engineers contribute the crucial skills needed to build maintainable, scalable, and testable code. By fostering collaboration, embracing core software engineering principles, and recognizing the shared emphasis on rigor and validation within their respective domains, SEAMs and software engineers can work together to create software that not only advances scientific discovery but also stands the test of time. Ultimately, this collaborative approach is essential for ensuring the trustworthiness and long-term impact of scientific software in addressing the complex challenges facing our world.

### Resources

The following resources provide more information on modern software engineering:

- [Modern Software Engineering](https://www.pearson.com/en-us/subject-catalog/p/modern-software-engineering-doing-what-works-to-build-better-software-faster/P200000009466/9780137314867)
- [The Pragmatic Programmer](https://www.pearson.com/en-us/subject-catalog/p/pragmatic-programmer-the-your-journey-to-mastery-20th-anniversary-edition/P200000000337/9780135956915)
- [Software Engineering at Google](https://www.oreilly.com/library/view/software-engineering-at/9781492082781/?_gl=1*pr4dlv*_ga*MTE5NjQ1OTU4NC4xNzQxNjIwNzU3*_ga_092EL089CH*MTc0MTYyMDc1Ny4xLjEuMTc0MTYyMDgzMi41OS4wLjA.)
- [A Philosophy of Software Design](https://a.co/d/hR5AEA5).

For more information about scientific software, read:

- [Software Engineering for Science](https://www.routledge.com/Software-Engineering-for-Science/Carver-ChueHong-Thiruvathukal/p/book/9780367574277), and 
- Diane Kelly's paper on [Scientific software development viewed as knowledge acquisition](https://doi.org/10.1016/j.jss.2015.07.027).

### Author bio

Roger A. Rubio has been an employee of Sandia National Laboratories for 5 years.  He holds a Bachelor's of Science in Computer Engineering, has 25 years of experience as a Software Engineer, and 8 years experience as a Scrum Master.  Roger has worked for large corporations, government organizations, as well as small businesses.  His primary expertise is in engineering web applications from the ground up, and has experience with monolithic, modular, and microservices-based software applications.  He currently works in the CompSim group with the Advanced Simulation & Computing (ASC) program, which provides trustworthy scientific software to both government and strategic partners.  He is a huge movie buff, and loves music, reading, and spicy (hot) food.

<!---
Publish: Yes
Track: deep dive
Topics: software engineering, strategies for more effective teams
--->