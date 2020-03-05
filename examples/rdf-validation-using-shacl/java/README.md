### Code Example: Validate RDF instance (JSON-LD) using SHACL and the IDS Information Model

The Java code provided here demonstrates an implementation of a SHACL validator using Java and the Open Source [Apache Jena](https://jena.apache.org/) framework. Note that there is no extensive error handling etc., since this code only serves as a minimalistic example.
The application expects following inputs as program arguments:
- path to the IDS Information Model ontology file in RDF / Turtle.
- path to the root directory of the SHACL shapes folder
- path to the file containing the JSON-LD RDF instance, which has to be validated

The arguments may look like this (please note that spaces in the paths might be a problem):
````
"C:\Users\myAccount\Documents\Code\SHACL_Test\resources\ontology.ttl"
"C:\Users\myAccount\Documents\Code\SHACL_Test\resources\shapes"
"C:\Users\myAccount\Documents\Code\SHACL_Test\resources\rdf_instance.jsonld"
````

A failed validation logs the error to console.

````shell
Total RDF triples 	5708
Total SHACL shapes 	300
Feb 17, 2020 3:18:53 PM SHACL_Validator validateRDF
SEVERE: failed
Feb 17, 2020 3:18:53 PM SHACL_Validator validateRDF
SEVERE: [Node=<https://w3id.org/idsa/autogen/artifactRequestMessage/a5afaed2-a69b-41ed-bb6f-363b8f63478f>
  Path=<https://w3id.org/idsa/core/issued>
  <https://raw.githubusercontent.com/IndustrialDataSpace/InformationModel/master/testing/communication/MessageShape.ttl> (MessageShape): An ids:Message must have exactly one xsd:dateTime linked through the ids:issued property, Node=<https://w3id.org/idsa/autogen/artifactRequestMessage/a5afaed2-a69b-41ed-bb6f-363b8f63478f>
  Path=<https://w3id.org/idsa/core/issuerConnector>
````

### Dependencies

Following Maven dependencies are required to get the code running:

```
<dependency>
    <groupId>org.topbraid</groupId>
    <artifactId>shacl</artifactId>
    <version>1.3.1</version>
</dependency>
```

```
<dependency>
    <groupId>org.apache.jena</groupId>
    <artifactId>apache-jena-libs</artifactId>
    <version>3.14.0</version>
    <type>pom</type>
</dependency>
```

```
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-jdk14</artifactId>
    <version>1.7.25</version>
</dependency>
```
