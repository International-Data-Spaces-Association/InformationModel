# The International Data Spaces Information Model

The Information Model is an RDFS/OWL-ontology covering the fundamental concepts of the [Industrial Data Space](https://www.internationaldataspaces.org), i.e. the types of *digital contents* that are exchanged by *participants* by means of the Industrial Data Space *infrastructure components*. The ontology and its documentation are published at [https://w3id.org/idsa/core](https://w3id.org/idsa/core). The model development is led by the [Fraunhofer Institutes for Applied Information Technology FIT](https://www.fit.fraunhofer.de/en) and [Intelligent Analysis and Information Systems IAIS](https://www.iais.fraunhofer.de/en) with support by members of the [International Data Spaces Association](https://www.internationaldataspaces.org/) in context of the *Information Model* sub-working group (SWG4). The group is chaired by [Christoph Lange](https://github.com/clange/) ([Fraunhofer FIT](https://www.fit.fraunhofer.de/)) and [Sebastian Tramp](https://sebastian.tramp.name) ([eccenca GmbH](https://www.eccenca.com)). 

The model development is based on [GitHub](https://github.com/IndustrialDataSpace/InformationModel), following a [defined branching model](CONTRIBUTING.md). Contributions and community feedback are maintained via the GitHub [ticketing system](images/Issue_Lifecycle.jpg). The [release process](images/Release_process.jpg) is aligned with the International Data Spaces Association architecture
working group meetings, i.e. there are roughly 2 releases scheduled per year with intermediary updates to the development branch. The currently stable version is *3.0.0*. The Information Model and associated resources published on GitHub are available under the [Apache License 2.0](https://github.com/IndustrialDataSpace/InformationModel/blob/master/LICENSE).

## Authors and contributors

The Information Model was originally created by 

- Jaroslav Pullmann, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en) now with Stardog Union and succeeded by Dr. Christoph Lange
- Dr. Christian Mader, [Fraunhofer IAIS](https://www.iais.fraunhofer.de/en) and
- Dr. Sebastian Tramp, [eccenca GmbH](https://www.eccenca.com)

with significant contributions, comments and support by (in alphabetical order):

- Haydar Akyürek, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en)
- Sebastian Bader, [Fraunhofer IAIS](https://www.iais.fraunhofer.de/en)
- Matthias Böckmann, [Fraunhofer IAIS](https://www.iais.fraunhofer.de/en) 
- Dr. Sandra Geisler, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en)
- Dr. Anna Kasprzik, [TIB](https://www.tib.eu/en)
- Dr. Christoph Lange, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en)
- Andreas W. Müller, [Schaeffler](https://www.schaeffler.de/content.schaeffler.de/en/)
- Dr. Michael Theß, [Signal Cruncher GmbH](https://signal-cruncher.com/)

Likewise the authors would like to thank numerous colleagues at Fraunhofer, active participants of the [International Data Spaces Association](https://www.internationaldataspaces.org/en/), the members of the W3C [Dataset Exchange Group](https://www.w3.org/2017/dxwg/wiki/Main_Page) and [Data Market Austria](https://datamarket.at/en/) for illuminating conversations and support in shaping the Information Model.

## Directory layout

There are following top-level files and directories:

- `codes`: Code lists of enumerated *literal values* and unique, *singleton concept instances*. Code lists are the preferred way to encode and reference re-usable instances of a homogeneous value range.
- `docs`: Documentation of the latest release of the Information Model and its classes.
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

Additional resources are provided:

- Latest information about IDS and all related resources: The [IDS-G](https://github.com/International-Data-Spaces-Association/IDS-G)

- Releases are provided in the Industrial Data Space [Github Repository](https://github.com/IndustrialDataSpace/InformationModel/releases/)

- Overview on IDS Messages, descriptions and attribute explanations: [Message Overview](http://htmlpreview.github.io/?https://github.com/IndustrialDataSpace/InformationModel/blob/feature/message_taxonomy_description/model/communication/Message_Description.htm)

- Java representation of the Information Model, a mapping to a POJO domain model with no reference to graph or ontology constructs. 
Instances of the Information Model might such conveniently by created, validated and (de)serialized in a strongly-typed way using 
any common development environment without requiring in-depth knowledge of RDF and related Semantic Web standards. 
The Java Information Model is provided as a single JAR library via the [Maven Repository](https://maven.iais.fraunhofer.de/artifactory/eis-ids-public/)
operated by Fraunhofer [IAIS](https://www.iais.fraunhofer.de/):

```xml
<repositories>
    <repository>
        <id>snapshots</id>
        <name>maven-snapshots</name>
        <url>https://maven.iais.fraunhofer.de/artifactory/eis-ids-public</url>
    </repository>
</repositories>
```

The dependency to the Java representation is as follows (replace <code>${infomodel.version}</code> with the latest version):
```xml
<dependency>
    <groupId>de.fraunhofer.iais.eis.ids.infomodel</groupId>
    <artifactId>java</artifactId>
    <version>${infomodel.version}</version>
</dependency>
```

For automated validation of the Information Model POJOs (via the builder classes) you can include:
```xml
<dependency>
    <groupId>de.fraunhofer.iais.eis.ids.infomodel</groupId>
    <artifactId>validation-serialization-provider</artifactId>
    <version>${infomodel.version}</version>
</dependency>
```

- UML-based visualization of the Information Model, its classes, properties and relations, including their cardinalities. It is available as part of the Nightly and Release Packages on [GitHub](https://github.com/IndustrialDataSpace/InformationModel/releases).

- [Webinar of November 2018, giving a technical overview of the Information Model](https://www.internationaldataspaces.org/wp-content/uploads/2019/07/IDS-Information-Model.pdf)

For members of the International Data Spaces Association only:
- [Working document](https://industrialdataspace.jiveon.com/docs/DOC-1817), explaining
the usage of the Information Model for data exchanges in the IDS.
