# The Industrial Data Space Information Model

The information model of the [Industrial Data Space](https://industrialdataspace.org) is currently under development, and a snapshot is available in [the develop branch](https://github.com/IndustrialDataSpace/InformationModel/tree/develop) of this repository.

A release is roughly planned for Q4 of 2018 and the model is available under the [Apache License 2.0](https://github.com/IndustrialDataSpace/InformationModel/blob/master/LICENSE).

The work on the information model is organized in the sub-working group 4 of the architecture working group of the Industrial Data Space Association.

This Information Model group is chaired by [Jaroslav Pullmann](https://github.com/jpullmann) ([Fraunhofer FIT](https://www.fit.fraunhofer.de/)) and [Sebastian Tramp](https://sebastian.tramp.name) ([eccenca GmbH](https://www.eccenca.com)).

## Directory layout

There are following top-level files and directories:

- `codes`: Shared code lists (IRIs) and enumerations of literal values
- `model`: Core models (T-Box) split into sub-model directories each serving a particular modelling aspect
- `metamodel`: Utility models related to annotation and processing of `model` concepts
- `views`: Individual tailored views defined upon the overall model for a particular purpose
- `Ontology.ttl`: Complete declarative model of the Industrial Data Space containing all of the above sources.

