include Makefile.vars

# Validate against SHACL shape
# Validator: https://github.com/TopQuadrant/shacl
all: conn_self_description.ttl
	$(SHACL)/shaclvalidate.sh -datafile $< -shapesfile shapes/infrastructure/ConnectorShape.ttl

# Obtain individual shapes from infomodel repository
# Source: https://github.com/IndustrialDataSpace/InformationModel/
%Shape.ttl:
	wget -N https://github.com/IndustrialDataSpace/InformationModel/raw/master/$(subst shapes/,testing/,$@)

# convert JSON-LD to Turtle using, e.g., http://jena.apache.org/documentation/io/
conn_self_description.ttl: conn_self_description.jsonld
	$(JENA)/riot --strict --check --output=Turtle $< > $@

# pretty-print JSON-LD for better readability (optional)
# https://stedolan.github.io/jq/
conn_self_description.pretty.jsonld: conn_self_description.jsonld
	./jq . $< > $@

# get the latest connector self-description from the connector (works from Fraunhofer networks)
conn_self_description.jsonld:
	wget -O $@ $(CONNECTOR)
