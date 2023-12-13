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

In the following the concepts of an application profile are illustrated in a non-normative way on a selection of Information Model properties. 


| Property | URI | Type | Range | Card. | Vocabulary |
| --- | --- | --- | --- | --- | --- |
| Title | `dct:title` | mandatory |`xsd:string`|1..n| - |
| Standard Licence | `ids:standardLicense` | optional |`spdx:ListedLicense`|0..1| [SPDX License List](https://github.com/spdx/license-list-data/tree/master/rdfturtle) |
| Publisher | `dct:publisher` | optional | `foaf:Agent` |0..n| - |


#### Range Details

| Class | URI | Mandatory Prop. | Recommended Prop. | 
| --- | --- | --- | --- |
| Agent | `foaf:Agent` | `foaf:name` <br /> `foaf:homepage` | `foaf:mbox` |


## Application Profiles

The following specifications and established application profiles constitute the foundation of the IDS-AP. 

### DCAT

The [W3C Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-2/) is a well-established vocabulary for describing data catalogs. The overall objective is to improve the interoperability between data catalogs, enable federated search mechanisms, and (Open) Data on the Web. It is developed by the [Dataset Exchange Working Group (DXWG)](https://www.w3.org/2017/dxwg/wiki/Main_Page). DCAT offers no guidelines about the format of the actual data, but focuses on metadata. The core of the specification consists of three main classes: catalog (`dcat:Catalog`), dataset (`dcat:Dataset`) and distribution (`dcat:Distribution`). One catalog comprises of several datasets and one dataset can include multiple distributions. A distribution represents the actual data. The basis for DCAT is the [Dublin Core](https://www.dublincore.org/specifications/dublin-core/) metadata vocabulary - a general standard for describing digital assets.

### DCAT-AP

The [DCAT Application Profile for data portals in Europe (DCAT-AP)](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe) is an extension of
DCAT for describing public sector data. Its maintenance is led by the European Commission and is established as the standard for the publication of Open Data across Europe - for instance it is applied by the [official portal for European Data](https://data.europa.eu). Correspondent to the definition of application profiles, DCAT-AP applies concrete guidelines for DCAT, including cardinalities, mandatory fields and controlled namespaces. In addition, it adds domain-specific metadata fields to increase the expressiveness. The popularity of DCAT-AP has led to the development of extension and derivates of DCAT-AP itself. DCAT-AP is a viable foundation for the development of an application profile for IDS. Especially the availability of extensive [SHACL shapes](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/210) support the consideration for IDS. 


### Further Profiles

The following application profiles are mostly extensions of DCAT-AP for specific countries or types of data. Some of them are not actively developed any more and are just listed for completeness.


| Profile | Description |
| --- | --- | 
| [GeoDCAT-AP](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/geodcat-application-profile-data-portals-europe) | Extension for describing geospatial datasets. The latest release is from 2016.  | 
| [StatDCAT-AP](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe) | Specifications and tools that enhance interoperability between descriptions of statistical data sets within the statistical domain and between statistical data and open data portals. It adds properties to describe statistical data in more detail, for example data from Eurostat. Latest release is from 2019. | 
| [DCAT-AP.de](https://www.dcat-ap.de) | Profile for Open Data from Germany. | 
| [DCAT-AP-SE](https://docs.dataportal.se/dcat/en/) | Profile for Open Data from Sweden. | 
| [DCAT-BE](http://dcat.be/) | Profile for Open Data from Belgium. | 
| [DCAT-AP-NO](https://data.norge.no/specification/dcat-ap-no/) | Profile for Open Data from Norway. | 
| [DCAT-AP_IT](https://www.dati.gov.it/content/dcat-ap-it-v10-profilo-italiano-dcat-ap-0) | Profile for Open Data from Italy. | 
| [DCAT-AP-CZ](https://ofn.gov.cz/rozhran%C3%AD-katalog%C5%AF-otev%C5%99en%C3%BDch-dat/2021-01-11/) | Profile for Open Data from the Czech Republic. | 


## IDS-AP

The IDS-AP is based 

## Suggested Usage and Extension


## Acknowledgments

This work has been carried out in the scope of the [Fraunhofer Cluster of Excellence Cognitive Internet Technologies](https://www.cit.fraunhofer.de/), [Research Center Data Spaces](https://www.dataspaces.fraunhofer.de/), project T66.
