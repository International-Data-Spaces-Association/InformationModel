# SHACL validation

## Scenario
The reference examples show, how RDF instances can be validated with SHACL on the CLI and using existing programming libraries.

## Contents

The [java](./java/) subdirectory contains a code example of a small SHACL validator implementation, based on Java and Apache Jena.

The [cli](./cli/) subdirectory demonstrates the validation using CLI tools.

Below, the basic functionality of SHACL and how it's intended usage is described.


********

### Description
The IDS Information Model is a domain-agnostic RDF/OWL ontology and an essential agreement shared by the participants and components of the International Data Space. Participants of the IDS use the RDF vocabulary provieded by the Information Model as the common language in the IDS.
To ensure the correct usage and understanding of the vocabulary, we provide validation structures in the Shapes Constraint Language (SHACL). These, so called SHACL shape graphs, can be used to validate self-generated RDF statements against the Information Model and check, if, e.g,  :
- a Connector self-description is valid
- a ids:Resource is described using the right IDS terms
- a HTTP multipart message provides the necessary information

The SHACL shapes can be found in the [testing](../testing) subdirectory of the IDS Information Model.

The tools and methods provided here demonstrate the validation of JSON-LD RDF statements, since JSON-LD is currently the most widely used RDF serialization in the IDS.




### Basic Functionality of SHACL
SHACL shapes formulate constraints on IDS Information Model classes and properties. For example, the following Connector SHACL shape states, that a Connector must have exactly one property called `ids:securityProfile`, which additionally refers to an instance of class `ids:SecurityProfile`. If this constraint is not satisfied, it is treated as a violation. Using the tools and frameworks described below, one can validate a RDF instance of the ids:Connector class, which is basically equivalent to the Connector's self-description, class against this shape. The [W3C documentation of SHACL](https://www.w3.org/TR/shacl/) provides additional information on the functionality of SHACL.
```
shapes:ConnectorShape
	a sh:NodeShape ;
	sh:targetClass ids:Connector ;

sh:property [
  a sh:PropertyShape ;          
  sh:path ids:securityProfile ;
  sh:class ids:SecurityProfile ;
  sh:minCount 1 ;
  sh:maxCount 1 ;
  sh:severity sh:Violation ;
] ;
```

## Validating RDF instances using SHACL

Before a RDF instance (also called data graph) can be validated against SHACL shapes, two main conditions must be fullfilled.

#### 1. Preparing the SHACL Shapes
To fully validate a data graph against SHACL, one needs to get all relevant SHACL shapes for that particular instance. The provided SHACL shape files are class-specific, therefore each class in the IDS Information Model has a corresponding file with SHACL shapes. Class-specific SHACL files leads to a better overall structure and enables easy expansion in the future.

To validate a, e.g., Connector self-description, one needs the corresponding SHACL shapes for that RDF instance. In this example, one would have to retrieve the SHACL shapes for the ids:Connector class, it's superclasses as well as all classes which are in relation to the Connector class via RDF properties.

To solve this issue, we _recommend_ to concatenate all SHACL shapes in the _testing_ subdirectory of the respository into a single shapes graph or file respectively.

#### 2. Preparing the RDF instance
In addition to the preparations of the the SHACL shapes graph, the RDF instance may need some additional semantic informationen such as `rdfs:subClassOf` class inheritance informations. For example, the`Connector` class is a subclass of the `ManagedEntity` class. To enable SHACL to validate the properties, which the `Connector` instance inherits from the superclass `ManagedEntity` which the `Connector` class inherits, the correct axioms must be added to the data graph, this is due to the fact that SHACL shapes do not cover these kind of semantics.

A simple solution is to append the whole IDS ontology to the RDF instance. This ensures that the data graph contains all necessary relational information.
