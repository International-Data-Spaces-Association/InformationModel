# Reference examples to describe domain-specific semantics of content

## Scenario
The reference examples show how the IDS Information Model can be used to describe digital content, in the IDS, with domain-specific semantics. The examples provided here use a pre-defined [JSON Schema](https://json-schema.org) for temperature data.

## SHACL Shapes for Content Description and Data Validation

The [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) is a W3C recommended language to describe and validate RDF graphs against a set of conditions.
The IDS Information Model already provides SHACL shapes to validate RDF instances against the model. The SHACL shapes for validation can be found in the folder _testing_. 

#### Describe Domain-specific Semantics of Contents

The Information Model is domain-independent; it contains generic properties for _ids:Resource_ and _ids:Representation_. SHACL shapes can be used to add domain-specific semantics to _ids:Resource_ and _ids:Representation_, without the need for extending the Information Model itself; in other words, this document does not present extended functionality of the Information Model, but it presents best practices for using the Information Model together with related standards, each for its purpose.

The [TEMP_SHACL.ttl](TEMP_SHACL.ttl) contains a SHACL shape, which describes the schema of a JSON temperature dataset. The [TEMP_DATA_SCHEMA.json](TEMP_DATA_SCHEMA.json) file contains the corresponding JSON schema, from which the SHACL shape is derived.

[TEMP_RESOURCE.ttl](TEMP_RESOURCE.ttl) and [TEMP_RESOURCE.json](TEMP_RESOURCE.json), show an exemplary modelling of a temperature dataset as an _ids:Resource_ using the [RDF/Turtle](https://www.w3.org/TR/turtle/) or [JSON-LD](https://www.w3.org/TR/2014/REC-json-ld-20140116/) RDF serialization. The aforementioned [TEMP_SHACL.ttl](TEMP_SHACL.ttl) SHACL shape can be referenced by its URI in the _ids:Resource_ (or _ids:Representation_) using the _ids:shapesGraph_ property, an import of _sh:shapesGraph_ into the IDS namespace. In this way, domain-specific semantics can be supplemented to a _ids:Resource / ids:Representation_.  

```
ids:shapesGraph "<URI of an RDF graph containing SHACL shapes>";
```

##### Validate data using SHACL
With a SHACL validator, such as the Open Source [TopBraid SHACL API](https://github.com/TopQuadrant/shacl) tool or the [SHACL Playground](https://shacl.org/playground/) website, one can validate RDF / JSON-LD data using SHACL shapes.

The following examples show a temperature dataset in RDF/TTL and JSON-LD, which comply with the [TEMP_SHACL.ttl](TEMP_SHACL.ttl) SHACL shape, as well as the corresponding JSON Schema. The corresponding files can be found here, in [RDF / Turtle](TEMP_SAMPLE_DATA.ttl) and [JSON](TEMP_SAMPLE_DATA.json) 

```
@prefix data: <http://example.org/data#> .
@prefix ex: <http://example.org/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

data:47649009-11b0-4b1b-a192-b7305d86a2bc
    a ex:SensorMeasurement ;
    ex:value 20.5 ;
    ex:unit  "F" ;
    ex:timestamp "2019-10-28T13:00Z"^^xsd:datetime ;
    ex:location [
         ex:lon 120.05 ;
         ex:lat 160.20 ;
    ].
```
```JSON
{
    "@context": {
        "ex": "http://example.org/ns#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
        "@id": "data:47649009-11b0-4b1b-a192-b7305d86a2bc",
        "@type": "ex:SensorMeasurement",
        "ex:location": {
            "ex:lat": {
                "@type": "xsd:decimal",
                "@value": 160.20
            },
            "ex:lon": {
                "@type": "xsd:decimal",
                "@value": 120.05
            }
        },
        "ex:timestamp": {
            "@type": "xsd:datetime",
            "@value": "2019-10-28T13:00Z"
        },
        "ex:unit": "F",
        "ex:value": {
            "@type": "xsd:decimal",
            "@value": "20.5"
        }
}
```
