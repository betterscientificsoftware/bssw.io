# Software Versioning
<!--deck text start-->
Most software changes over time.  An explicit versioning scheme is a key way to communicate to your users about those changes.
<!--deck text end-->

#### Contributed by [David E. Bernholdt](https://github.com/bernhold)

#### Publication date: September 30, 2021

Resource information | Details
:--- | :--- 
Wikipedia article  | [Software versioning](https://en.wikipedia.org/wiki/Software_versioning)
Web site | [Semantic Versioning](https://semver.org/)
Web site | [Calendar Versioning](https://calver.org/)

Versioning is the process of assigning unique identifiers to instances of a product. It is commonly applied to computer software, but similar ideas are also used in other contexts. In software, it is typically used to mark points in the evolution of a software product as it is developed (new features added) and maintained (bugs fixed). Versioning is often an important communication tool between the providers and users of a software package. Assuming adequate documentation, versioned releases can be associated with changes in the features provided and bug fixes included. This allows users to better evaluate the benefits and consequences of updating to a newer version, facilitates support and bug reporting, and other interactions between users and producers.

As the Wikipedia article describes, there are many different versioning schemes used by different projects, organizations, and companies. Two of the most common forms are *sequence-based* and *release date-based*. *Semantic Versioning* (see web site) is a sequence-based approach where a set of identifiers is used to differentiate different types of changes. A common implementation uses the form `major`.`minor`.`patch`.  Numerical identifiers in each position are incremented depending on the type of change being made based on a set of rules (semantics). For example, often the major version number is incremented for API changes that break backward compatibility, the minor version is changed for new features that do not break backward compatibility, and the patch number is incremented for bug fixes. *Calendar Versioning* (see web site) typically uses a date-based identifier, for example `YY`.`MM`, denoting the two-digit year and month of the release. In these and other versioning schemes, there are often additional conventions used to denote preparatory releases (e.g., alpha, beta, release candidates) and other common practices.

While you may find arguments in some communities over the relative merits of one versioning scheme over another, the best practice is to *have* a versioning scheme, document it, and use it.  It is possible to change versioning schemes if you feel that another approach would suit the situation better.  Though such changes should be rare.

<!---
Publish: yes
Pinned: no
Topics: documentation, revision control, release and deployment
RSS update: 2021-09-30
--->
