# The Industrial Data Space Information Model

The Information Model is an RDFS/OWL-ontology covering the fundamental concepts of the [Industrial Data Space](https://industrialdataspace.org), i.e. the types of *digital contents* that are exchanged by *participants* by means of the Industrial Data Space *infrastructure components*. The model development is led by Fraunhofer [FIT](https://www.fit.fraunhofer.de/en) and [IAIS](https://www.iais.fraunhofer.de/en) with support by members of the [International Data Spaces Association](https://www.internationaldataspaces.org/) in context of the *Information Model* sub-working group (SWG4). The group is chaired by [Jaroslav Pullmann](https://github.com/jpullmann) ([Fraunhofer FIT](https://www.fit.fraunhofer.de/)) and [Sebastian Tramp](https://sebastian.tramp.name) ([eccenca GmbH](https://www.eccenca.com)).

The model development is based on [GitHub](https://github.com/IndustrialDataSpace/InformationModel), following a [defined branching model](CONTRIBUTING.md). Contributions and community feedback are maintained via the GitHub [ticketing system](images/Issue_Lifecycle.jpg). The [release process](images/Release_process.jpg) is aligned with the International Data Spaces Association architecture
working group meetings, i.e. there are 2 releases scheduled per year with intermediary updates to the development branch. The Information Model and associated resources published on Github are available under the [Apache License 2.0](https://github.com/IndustrialDataSpace/InformationModel/blob/master/LICENSE).


## Authors and contributors

The Information Model was created by Jaroslav Pullmann, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en), Dr. Christian Mader, [Fraunhofer IAIS](https://www.iais.fraunhofer.de/en) and Dr. Sebastian Tramp, [eccenca GmbH](https://www.eccenca.com) with significant contributions, comments and support by (in alphabetical order):

- Sebastian Bader [Fraunhofer IAIS](https://www.iais.fraunhofer.de/en)
- Dr. Sandra Geisler, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en)
- Dr. Anna Kasprzik, [TIB](https://www.tib.eu/en)
- Andreas W. Müller, [Schaeffler](https://www.schaeffler.de/content.schaeffler.de/en/)
- Dr. Michael Theß, [Signal Cruncher GmbH](https://signal-cruncher.com/)

Likewise the authors would like to thank numerous colleagues at Fraunhofer, active participants of the [International Data Spaces Association](https://www.internationaldataspaces.org/en/), the members of the W3C [Dataset Exchange Group](https://www.w3.org/2017/dxwg/wiki/Main_Page) and [Data Market Austria](https://datamarket.at/en/) for illuminating conversations and support in shaping the Information Model.

## Overview

The RDFS/OWL-ontology maintained in Github is the normative, *declarative representation* of the IDS Information Model. It is framed by the *conceptual representation* laid down in the *Reference Architecture Model* ([RAM v2](https://www.internationaldataspaces.org/publications/idsa-ram/)) and mapped to *programmatic representations* supporting a native development within a programming language, e.g. Java. The overall purpose of this formal model is to enable a (semi)automated exchange of digital assets within a network of distributed parties while maintaining their sovereignty on those assets. Given such a broad functional scope intersected with respective business domains (logistics, agriculture, energy etc.) the Information Model is a subject to perpetual evolution and refinement lead by clear design principles. These are, among others:
- *reuse*: body of existing work (standards, ontologies, scientific publications etc.) is evaluated and re-used. It either informs or is effectively used in the development of the Information Model, e.g. by extending classes and properties of vocabularies like [DCAT](https://www.w3.org/TR/vocab-dcat/).
- *re-usability*: model constituents are designed for re-usability within different contexts, thus reducing model extent and complexity
- *separation of concerns*: as a prerequisite to re-usability each constituent or set of constituents is modeled according to a dedicated concern addressed.

The mnemonic hexagonal arrangement of **C**arbon atoms was reused to depict main **C**oncerns of the Information Model: 

<div align="center"><img alt="Concerns hexagon" src="https://raw.githubusercontent.com/IndustrialDataSpace/InformationModel/develop/images/Hexagon_simple.jpg" width="90%" /></div>

## Directory layout

There are following top-level files and directories:

- `codes`: Code lists of enumerated *literal values* and unique, *singleton concept instances*. Code lists are the preferred way to encode and reference re-usable instances of a homogeneous value range.
- `examples`: Example instances providing a guidance on recommended model usage and best practices.
- `images`: Figures supporting the understanding and documentation of the Information Model
- `metamodel`: Utility models related to annotation and processing of `model` concepts.
- `model`: Core model split into sub-model directories each serving a particular modeling aspect.
- `references`: Versioned sources of relevant 3rd party models used as a reference (informative or effective, i.e. via concept import)
- `taxonomies`: Hierarchical arrangement of concepts (classes) extending a base concept defined by the core `model`.
- `testing`: Test resources (e.g. RDFUnit) used by tools and the build process to ensure the syntactic validity and semantic consistence of the Information Model
- `utils` : Utility scripts used for Information Model development and testing
- `views`: Individual tailored views defined upon the overall model for a particular purpose, e.g. the selection of Glossary terms
- `Ontology.ttl`: Detailed metadata of the Industrial Data Space Information Model.

## Related resources

Additional resources are provided for the members of the International Data Spaces Association:

- Java representation of the Information Model, a mapping to a POJO domain model with no reference to graph or ontology constructs. Instances of the Information Model might such conveniently by created, validated and (de)serialized in a strongly-typed way using any common development environment without requiring in-depth knowledge of RDF and related Semantic Web standards. The Java Information Model is provided as a single JAR library via the [Maven Repository](https://mvn.isst.fraunhofer.de/nexus/#browse/browse:ids-local:de%2Ffraunhofer%2Fiais%2Feis%2Fids%2Finfomodel)
operated by Fraunhofer [ISST](https://www.isst.fraunhofer.de/).

- UML-based visualization of the Information Model, its classes, properties and relations, including their cardinalities. It is available on the Maven Repository mentioned above, under the same base path (visualization component).

- Working [document](https://industrialdataspace.jiveon.com/docs/DOC-1817), on the association's Jive platform, explaining
the usage of the Information Model for communication on the Industrial Data Space.
