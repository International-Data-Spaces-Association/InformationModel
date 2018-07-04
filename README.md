# The Industrial Data Space Information Model

The Information Model of the [Industrial Data Space](https://industrialdataspace.org) is currently under development, and a snapshot is available in [the develop branch](https://github.com/IndustrialDataSpace/InformationModel/tree/develop) of this repository.

A release is roughly planned for Q4 of 2018 and the model is available under the [Apache License 2.0](https://github.com/IndustrialDataSpace/InformationModel/blob/master/LICENSE).

The work on the information model is organized in the sub-working group 4 of the architecture working group of the Industrial Data Space Association.

This Information Model group is chaired by [Jaroslav Pullmann](https://github.com/jpullmann) ([Fraunhofer FIT](https://www.fit.fraunhofer.de/)) and [Sebastian Tramp](https://sebastian.tramp.name) ([eccenca GmbH](https://www.eccenca.com)).

## Contributors

This work has benefited from significant contributions, comments and support by (in alphabetical order):

- Dr. Sandra Geisler, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en)
- Dr. Anna Kasprzik, [TIB](https://www.tib.eu/en)
- Dr. Christian Mader, [Fraunhofer IAIS](https://www.iais.fraunhofer.de/en)
- Andreas W. Müller, [Schaeffler](https://www.schaeffler.de/content.schaeffler.de/en/)
- Jaroslav Pullmann, [Fraunhofer FIT](https://www.fit.fraunhofer.de/en)
- Dr. Michael Theß, [Signal Cruncher GmbH](https://signal-cruncher.com/)
- Sebastian Tramp, [eccenca GmbH](https://www.eccenca.com)

Likewise the chairs would like to thank numerous colleagues at Fraunhofer, active participants of the
[International Data Spaces Association](https://www.internationaldataspaces.org/en/), the members of the
W3C [Dataset Exchange Group](https://www.w3.org/2017/dxwg/wiki/Main_Page) and [Data Market Austria](https://datamarket.at/en/) for
illuminating conversations and support in shaping the Information Model. 

## Directory layout

There are following top-level files and directories:

- `codes`: Shared code lists (IRIs) and enumerations of literal values
- `model`: Core models (T-Box) split into sub-model directories each serving a particular modelling aspect
- `metamodel`: Utility models related to annotation and processing of `model` concepts
- `views`: Individual tailored views defined upon the overall model for a particular purpose
- `Ontology.ttl`: Complete declarative model of the Industrial Data Space linking all of the above sources.
   This file is intended for *internal purposes only*, the normative version will be published as result of
   a build-process at [https://w3id.org/ids/core/](ttps://w3id.org/ids/core/) by Q4/2018.

Further resources (directories) may optionally augment the above contents:

- `examples`: Example instances providing a guidance on recommended model usage and best practices
- `references`: Versioned source of external models used as a reference
