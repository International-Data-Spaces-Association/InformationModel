# Resource Model

`Resource` is the top level class of the hierarchy of digital assets comprising the `DataAsset` and `DatApp` subclasses.

<!--- ![Resource taxonomy](figures/Resource_taxonomy.jpg) --->
<img src="figures/Resource_taxonomy.jpg" alt="Resource taxonomy" width="250px"></img>

`Resource` content is modeled at 3 abstraction layers defined in the Reference Architecture Document v2:

1. Resource - abstract content
2. Representation - concrete content (syntax)
3. Artifact - materialization

<!--- ![Resource model](figures/Resource.jpg) --->
<img src="figures/Resource.jpg" alt="Resource model" height="250px"></img>

# References
- [Data Catalog Vocabulary (DCAT). W3C Recommendation 16 January 2014](https://www.w3.org/TR/vocab-dcat/)

# Related resources

Listing of auxiliary, informative resources.

## General dataset models
- [Dataset Descriptions: HCLS Community Profile. W3C Interest Group Note 14 May 2015](https://www.w3.org/TR/hcls-dataset/)
- [DDI RDF Vocabularies](http://www.ddialliance.org/Specification/RDF)
- [DDI 3.2 XML Schema Documentation (2014-02-05)](https://www.ddialliance.org/Specification/DDI-Lifecycle/3.2/XMLSchema/FieldLevelDocumentation/)

## Data structures
- [The Statistical Core Vocabulary (scovo)](http://sw.joanneum.at/scovo/schema.html), core statistical structures
- [Metadata Vocabulary for Tabular Data. W3C Recommendation 17 December 2015](https://www.w3.org/TR/tabular-metadata/), metadata for annotation of tabular data at various levels

## Data types, quantities, units etc.
- [Custom Datatypes. Towards a web of Linked Datatypes. Draft 20 March 2018](https://ci.mines-stetienne.fr/lindt/v2/custom_datatypes.html), specification of RDF datatypes for quantity value literals complaint with Code of Units of Measures [UCUM](https://ci.mines-stetienne.fr/lindt/v2/custom_datatypes.html#bib-UCUM)
- [Quantities, Units, Dimensions and Types (QUDT) Schema - Version 2.0](http://www.qudt.org/doc/2017/DOC_SCHEMA-QUDT-v2.0.html)
- [QUDT Schema for Datatypes - Version 2.0](http://www.qudt.org/doc/2017/DOC_SCHEMA-QUDT-DATATYPES-v2.0.html)
- [Meek, B.: A taxonomy of datatypes, 1994](https://dl.acm.org/citation.cfm?id=185042&dl=ACM&coll=DL)
- [ISO/IEC 11404, General Purpose Datatypes](http://standards.iso.org/ittf/PubliclyAvailableStandards/c039479_ISO_IEC_11404_2007%28E%29.zip)
- [Panov, L. Soldatova, and S. Dzeroski: OntoDT - Generic Ontology of Datatypes, 2014](https://www.sciencedirect.com/science/article/pii/S0020025515005800), [homepage](http://www.ontodm.com/doku.php?id=ontodt)


## Media
- [Ontology for Media Resources 1.0. W3C Recommendation 09 February 2012](https://www.w3.org/TR/mediaont-10/)

## Analysis and discussion
- [DXWG GitHub Wiki: Data aspects semantics](https://github.com/w3c/dxwg/wiki/Data-aspects---semantics) 

## Guidelines and methodolgies
- [Data on the Web Best Practices. W3C Recommendation 31 January 2017](https://www.w3.org/TR/dwbp/), best practices related to the publication and usage of data on the Web, making data discoverable and understandable by humans and machines
- [Spatial Data on the Web Best Practices. W3C Working Group Note 28 September 2017](https://www.w3.org/TR/sdw-bp/), best practices related to the publication of spatial data on the Web
- [SDMX Glossary](https://sdmx.org/wp-content/uploads/SDMX_Glossary_Version_1_0_February_2016.docx), concepts and related definitions used in structural and reference metadata of international organisations and national data-producing agencies
- [Modelling Statistical Domains in SDMX, Version 2.0, June 2018](https://sdmx.org/wp-content/uploads/Modelling-statistical-domains-in-SDMX-v2-201806.docx), guideline on design and creation of SDMX information model instances
- [Best Practices for Usage of DDI 3.2 and Future Versions](https://www.ddialliance.org/system/files/DDI%203.2%20Best%20Practices_0.pdf), guideline on identification etc.

## Data type

# Issues/Questions/Ideas

## Content type
- Consider provision of content type-related description templates, e.g. what are the appropriate "audio" vs. "document" metadata?
- Consider discussions on [`type of data`](https://github.com/w3c/dxwg/issues/64)

- https://webgate.ec.europa.eu/CITnet/stash/projects/ODCKAN/repos/datacite-to-dcat-ap/browse/documentation/Mappings.md
- Individual (Linked Data) URIs for DataCite resource types are available here: http://registry.it.csiro.au/def/datacite/resourceType

## Resource

- Consider samples of further relations/types of Resources
    - ISO 19115:StereoMate collection of image datasets (Aggregate) covering the *same subject* from different perspectives *providing a stereo view*
    - ISO19115: Series: collection of resources related by a common heritage adhering to a common specification
        - DS_Series is a subtype of the abstract DS_Aggregate
        - Series has three MD_Metadata objects, each with a different scope
            - object with scope = series contains the metadata shared by the whole collection
            - objects with scope = dimensionGroup are contained in a DS_Dataset, hold the 2D and 3D MD_SpatialRepresentation entities
            
# Recent TODOs

References evaluated in definition of ContentType:

- [DCMI Type Vocabulary](http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary)
    - `Event` - Non-persistent, time-based occurrence, e.g. exhibition, conference
    - `Collection` - Aggregation of resources with parts described separately
    - `Dataset` - Data encoded in a defined structure intended for direct machine processing
    - `Text` - Resource consisting primarily of words for reading, e.g. book, newspaper, article, archives of mailing lists. Readable images of textual material are considered Text
    - `Image`  - Visual, non-textual electronic and physical representation of a static and dynamic graphical content, e.g. image, painting, video
    - `StillImage`  - Static visual representation, e.g. painting, drawing, graphic design
    - `MovingImage` - Subclass of Image, sequence of images imparting an impression of motion, e.g. movie, television program, video
    - `Sound` - Resource primarily intended to be heard, e.g. an recorded speech, sound, music
    - `InteractiveResource` - Resource requiring an interaction from the user, e.g. applets, multimedia learning objects, VR environments
    - `PhysicalObject` - Inanimate, three-dimensional object or substance with digital representations like Image or Text
    - `Service` - System that provides one or more functions, e.g. authentication service, web server etc.
    - `Software` - Computer program in source or compiled form, e.g. C source file, MS-Windows .exe executable, or Perl script

Not considered were `dctype:Image`, an abstract superclass of visual resources, with no concrete use case in IDS. Likewise
`dctype:Service` is a means of provision and generation of Digital Content, instead of being itself mediated as such
(this holds for `Software`). Since IDS deals with digital Resources, `dctype:PhysicalObject` is out of scope.

- [DDI Controlled Vocabulary for General Data Format](http://www.ddialliance.org/Specification/DDI-CV/GeneralDataFormat_2.0.html)

 Collection of abstract data formats (kinds), largely overlapping with DCMI Type Vocabulary.  

- [ISO-19115, B.3.28 MD_ScopeCode](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115_and_19115-2_CodeList_Dictionaries#MD_ScopeCode)

 Classes for a variety of resources and services that that are subject of meta-data modelling by the standard.
 They represent entities of different purposes (`attribute`vs. `attributeType`) and levels of granularity (`attribute`
 vs. `repository`) which only partially match the IDS Digital Content domain.

- [PARSE.Insight content-types recommended for Re3data](http://www.re3data.org/schema http://gfzpublic.gfz-potsdam.de/pubman/item/escidoc:1397899)

- [MARC Genre Term List](http://id.loc.gov/vocabulary/marcgt.html) enumerates intellectual resource types with no immediate relevance for
 IDS, since generally covered by DCMI types or otherwise irrelevant (e.g. physical objects)


## Keyword
- Clarify range of `ids:keyword` (xsd:anyURI), compare: [dcat:keyword](https://www.w3.org/TR/vocab-dcat/#Property:dataset_keyword)


