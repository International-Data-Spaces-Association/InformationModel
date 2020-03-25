# SPARQL Queries
This module illustrates the annotation of IDS resources via  

## Motivation and Scenario
Having one or multiple resources, one would like to filter these based on certain criteria such as
- their structure (dimension)
  - dimension count: "has 3 dimension"
  - dimension usage: "uses time as dimension"
- their terminology
  - namespace usage: "uses RDF-Schema"
  - class usage: "uses Observation from the Data Cube vocabulary"
  - property usage: "uses sex from SDMX dimensions"
- arbitrary constraints
  - "file size > 10MB"
  - "optional field X not present"
  - "custom license URI contains a German domain"

We therefore extend the IDS information model with additional fields in the Data Cube and VoID languages, and query these via SPARQL for appropriate filtering.

## Requirements
- Java 11 (optional Java 8)
- Maven (for resolving dependencies)
- (optional: Perl for automatically generating VoID metadata, cf. the `Informationmodel/utils` directory)

## Process Overview
Given a [dataset](/SparqlQueries/src/main/resources/0a_LIFE_EXPECTANCY_DATA.xlsx), we create an [information model instance](/SparqlQueries/src/main/resources/1_LIFE_EXPECTANCY_RESOURCE.ttl) containing metadata from the IDS as well as Data Cube and VoID.
In this demonstration, we use a Java program based on Apache Jena for executing a [set of SPARQL queries](SparqlQueries\src\main\resources) that answer the questions mentioned above.

Note that these queries are flexible and therefore could dynamically be used by other tools or programms. 
