# Application Profiles for the IDS Information Model

This document presents design and implementation of the core application profile (AP) for the IDS Information Model - **IDS-AP**. The detailed objectives of the IDS-AP are:

- the provision of more practical guidelines for the implementation of the IDS Information Model,
- the means to validate and check correctness of a IDS self-description
- and, a basis for creating domain-specific derivates, use cases and extensions of the IDS Information Model.

The overall objective is to maximize and improve interoperability within the core IDS Information Model, extensions and other data models. The work is inspired by existing application profiles, such as the widely-used DCAT-AP.


## What is an Application Profile?
The term application profile is defined as "a set of metadata elements, policies, and guidelines defined for a particular application" [cf. Dublic Core Glossary](https://www.dublincore.org/specifications/dublin-core/usageguide/2001-04-12/glossary/). In practice, an application profile covers the following aspects: 

- It clearly defines, which properties are mandatory and which ones are optional.
- The allowed cardinalities of properties.
- Defines clear controlled vocabularies, if applicable. 
- Puts constraints to sub-properties, that are based on well-established ontologies. 

There does exist a strict standard how to document application profiles, but it is highly recommended to apply a machine-readable and expressive specification language, such as SHACL.

### Illustrative Examples in IDS

- `ids:title` - mandatory, 1..n
- `ids:standardLicense` - mandatory, 0..1, [SPDX License List](https://github.com/spdx/license-list-data/tree/master/rdfturtle) must be used
- `ids:publisher` - optional, 0..n, `vcard:Kind`


## Application Profiles

### DCAT

### DCAT-AP

DCAT-AP is a profile for data portals in Europe, based on DCAT. 

### Further Profiles



## IDS-AP

The IDS-AP is based 

## Suggested Usage and Extension


## Acknowledgments

This work has been carried out in the scope of the [Fraunhofer Cluster of Excellence Cognitive Internet Technologies](https://www.cit.fraunhofer.de/), [Research Center Data Spaces](https://www.dataspaces.fraunhofer.de/), project T66.
