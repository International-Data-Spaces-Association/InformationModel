#defined schemas and data files you want to test as filenames separated by whitespace
#schemas are ontology files, instances contain individuals instantiating ontology resources
#manualtests in form of RDFUnit testcase definitions can be added as well
MANUALSRC=$(wildcard testing/*.rdfunit.ttl)
INSTANCESRC=$(wildcard examples/*.ttl)
##include files which should be used for widoco generation
DOCSRC=Ontology.ttl isDefinedBy.ttl $(wildcard model/*/*.ttl)
SCHEMASRC=Ontology.ttl isDefinedBy.ttl $(wildcard model/*/*.ttl) $(wildcard codes/*.ttl) $(wildcard taxonomies/*.ttl)

#XML file containing the uncompressed XML export of a drawio ontology diagram
#DRAWIOSRC=$(wildcard schema/*.xml)

#disable manual and/or automatic tests. default: don't skip tests (=false)
#SKIPAUTOTESTS=true
#SKIPMANUALTESTS=true

# disable image generation, e.g. for other turtle assets such as the query catalog
# SKIPOWL2DOT=true

# the dataplatform where "make publish" will publish the schema graph
# SCHEMASRC_PUBLISH_DP=https://vocab.eccenca.com/
# the graph into which "make publish" will publish the schema graph
SCHEMASRC_PUBLISH_GRAPH=https://w3id.org/idsa/core/
ONTOLOGY_URI=${SCHEMASRC_PUBLISH_GRAPH}

BUILDPREFIX=IDS-InformationModel
