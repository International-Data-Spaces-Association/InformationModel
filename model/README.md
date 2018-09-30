# Model

## Introduction

This is the normative, *declarative representation* of the IDS Information Model as an RDFS/OWL-ontology. It is framed by the *conceptual representation* laid down in the *Reference Architecture Model* (RAM v2) and mapped to *programmatic representations* supporting a native development within a programming language, e.g. Java. The overall purpose of this formal model is to enable a (semi)automated exchange of digital assets within a network of distributed parties while maintaining their sovereignty on those assets. Given such a broad functional scope intersected with respective business domains (logistics, agriculture, energy etc.) the Information Model is a subject to perpetual evolution and refinement lead by clear design principles. These are, among others:
- *reuse*: body of existing work (standards, ontologies, scientific publications etc.) is evaluated and re-used. It either informs or is effectively used in the development of the Information Model (e.g. by extending classes and properties of vocabularies like DCAT)
- *re-usability*: model constituents are designed for re-usability within different contexts, thus reducing model extent and complexity
- *separation of concerns*: as a prerequisite to re-usability each constituent is modeled according to a dedicated concern it addresses

## Directory layout
Each of the sub-models represents an individual modeling facet:
- `communication`: Interaction with data sources, data sinks and data processing applications
- `content`: Layered modeling of various types of `Digital Content`
- `context`: References to time, space (geometry) and world entities
- `contract`: Digital contracts determining conditions of data retrieval, subscription and usage
- `goverance`: Concepts of certification, governance, and data sovereignty
- `infrastructure`: Building blocks of the Data Space (Connector, Broker, AppStore etc.)
- `participant`: Participants involved in Data Space interactions and operations
- `quality`: Quality aspects of data and services
- `security`: Security features of the components and their communication
- `shared`: Generic, re-usable models
- `traceability`: Provenance and logging of Data Space resources and events
