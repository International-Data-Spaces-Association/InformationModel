# SHACL Validation using CLI

## Scenario
The reference examples show how an Information Model RDF instance can be validated on the CLI against the IDS Information Model using SHACL.

## Description
This reference example demonstrates the SHACL validation of a Connector self-description. A IDS Connector provides its self-description as a JSON-LD document. The self-description can be validated using the corresponding SHACL shapes, which can be found in the _/testing/_ directory.

This example demonstrates the validation of a single RDF instance without considering its relations to other classes and their corresponding SHACL validity. Please check the [README.md in the parent directory](../README.md) for more information regarding this.


## Files

###### [conn_self_description.jsonld](conn_self_description.jsonld)
An example of a Connector self-description in JSON-LD.

###### [conn_self_description.pretty.jsonld](conn_self_description.pretty.jsonld)
The Connector self-description in better human-readable JSON-LD .

###### [conn_self_description.ttl](conn_self_description.ttl)
The Connector self-description in RDF/Turtle .

###### [Makefile](Makefile)
Makefile with a similar example as described below.

###### [Makefile.vars.template](Makefile.vars.template)
Template file for Makefile. Used in Makefile. See comments in file for details.
## Validate Connector Self-description

The example provided here uses Linux shell with existing tools to convert, pretty-print and validate a Connector self-description.  In this example, the JSON-LD self-description needs slight adjustments due to tool compatibility reasons.

The procedure is as follows:
1.  Retrieve Connector self-description (usually as JSON-LD). For this example, we assume that it is named `conn_self_description.jsonld`.

2. (*Optional*) Use [jq](https://stedolan.github.io/jq/) tool to pretty-print the JSON-LD document. E.g.:  
```shell
./jq . conn_self_description.jsonld > conn_self_description.pretty.jsonld
```

3. Convert `conn_self_description.jsonld` to RDF/Turtle using [Apache Jena](https://jena.apache.org/documentation/io/) as follows:
```
$(PATH_TO_JENA_bin)/riot --strict --check --output=Turtle conn_self_description.jsonld > conn_self_description.ttl
```
This is needed because the TopBraid SHACL tool, which is used for validation in this example, only supports RDF/Turtle notation.

4. Retrieve the corresponding SHACL shape for the Connector self-description. The *ConnectorShape.ttl* is located in the [testing/infrastructure](../../testing/infrastructure) subfolder of the IDS Information Model. Alternatively, one can download the SHACL shape using following command, if there is no local copy of the IDS Information Model repository.
```
wget -N https://github.com/IndustrialDataSpace/InformationModel/raw/master/testing/infrastructure/ConnectorShape.ttl
```

5. Add following RDF triple to `conn_self_description.ttl` file.
```
ids:BaseConnector rdfs:subClassOf ids:Connector .
```
This is required for classes such as the Connector, where the superclass (ids:Connector) is not intended to be used as an instance, but for property inheritance. The *ConnectorShape.ttl* SHACL shape validates ids:Connector instances. Usually Connectors are insntaces of a Connector subclass, e.g., *ids:BaseConnector* or *ids:TrustedConnector*. Adding the above stated triple to the self-description allows validating ids:Connector subclass with the ConnectorShape.

6. Validate `conn_self_description.ttl` file with [TopBraid SHACL API](https://github.com/TopQuadrant/shacl) and the corresponding SHACL shape using following command
```
$(PATH_TO_JENA_SHACL_bin)/shaclvalidate.sh -datafile conn_self_description.ttl -shapesfile ConnectorShape.ttl
```
