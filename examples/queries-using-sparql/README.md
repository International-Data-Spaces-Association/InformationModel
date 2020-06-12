# SPARQL Queries
This module illustrates the annotation of IDS resources via Data Cube or VoID, and presents a filtering mechanism based on SPARQL queries.
That is, __given multiple IDS resources along with SPARQL queries, return all matching resources.__

## Motivation and Scenario
Having one or multiple resources, one would like to filter these based on certain criteria such as
- their structure (dimension), in terms of Data Cube
  - dimension count: "has 3 dimensions"
  - dimension usage: "uses time as dimension"
- their terminology, in terms of VoID
  - namespace usage: "uses RDF Schema"
  - class usage: "uses Observation from the Data Cube vocabulary"
  - property usage: "uses sex from SDMX dimensions"
- arbitrary constraints, in terms of SHACL – for example, about the usage of properties (not necessarily globally, but in those _parts_ of the dataset to which certain shapes apply):
  - "`lifeExpectancy` property has datatype `decimal`"
  - "`lifeExpectancy` property is in range 0–150"
  - "`observation` property has to be used at least once"

We therefore extend the IDS information model with additional fields in the Data Cube and VoID vocabularies (cf. https://github.com/International-Data-Spaces-Association/InformationModel/issues/190), and query these via SPARQL for appropriate filtering.

## Requirements
- Java 11
- Maven (for resolving dependencies)
- (optional: Perl for automatically generating VoID metadata, cf. the `Informationmodel/utils` directory)

## Process Overview
Given a [dataset](/examples/queries-using-sparql/SparqlQueries/src/main/resources/0a_LIFE_EXPECTANCY_DATA.xlsx), we create an [information model instance](/examples/queries-using-sparql/SparqlQueries/src/main/resources/1_LIFE_EXPECTANCY_RESOURCE.ttl) containing metadata from the IDS as well as Data Cube and VoID.
In this demonstration, we use a Java program based on Apache Jena for executing a [set of SPARQL queries](SparqlQueries\src\main\resources) that answer the questions mentioned above.
For configuration and further details, please refer to the Java program as well as the SPARQL queries provided.

Given multiple IDS resources along with SPARQL queries, this solution exactly returns all matching resources.
Note that these queries are flexible and therefore could dynamically be used by other tools or programms.
