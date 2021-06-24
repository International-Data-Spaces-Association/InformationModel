#!/bin/bash

echo "This script executes a set of http requests in order to test the linked data compliance of our hosted IDS ontology files."
echo ""

# basic check
echo "1. curl -k https://localhost/idsa/ redirects to https://www.internationaldataspaces.org/?"
curl -k https://localhost/idsa/
echo ""

# check for content type HTML
echo "2. curl -k -H "Accept: text/html" https://localhost/idsa/core/ redirects to https://international-data-spaces-association.github.io/InformationModel/?"
curl -k -H "Accept: text/html" https://localhost/idsa/core/
echo ""

# check for content type Turtle
echo "3. curl -k -H "Accept: text/turtle" https://localhost/idsa/core/ redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/turtle" https://localhost/idsa/core/
echo ""

# check for content type RDF/XML
echo "4. curl -k -H "Accept: application/rdf+xml" https://localhost/idsa/core/ redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.xml?"
curl -k -H "Accept: application/rdf+xml" https://localhost/idsa/core/
echo ""

# check for content type JSON-LD
echo "5. curl -k -H "Accept: application/ld+json" https://localhost/idsa/core/ redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.json?"
curl -k -H "Accept: application/ld+json" https://localhost/idsa/core/
echo ""

# check for content type n-triples
echo "5. curl -k -H "Accept: application/n-triples" https://localhost/idsa/core/ redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.nt?"
curl -k -H "Accept: application/n-triples" https://localhost/idsa/core/
echo ""



# check for requesting ids:Resource (HTML)
echo "6. curl -k -H "Accept: text/html" https://localhost/idsa/core/Resource redirects to https://international-data-spaces-association.github.io/InformationModel/docs/index.html#/Resource?"
curl -k -H "Accept: text/html" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (Turtle)
echo "7. curl -k -H "Accept: text/turtle" https://localhost/idsa/core/Resource redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/turtle" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (RDF/XML)
echo "8. curl -k -H "Accept: application/rdf+xml" https://localhost/idsa/core/Resource redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.xml"
curl -k -H "Accept: application/rdf+xml" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (JSON-LD)
echo "9. curl -k -H "Accept: application/ld+json" https://localhost/idsa/core/Resource redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.json?"
curl -k -H "Accept: application/ld+json" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (n-triples)
echo "10. curl -k -H "Accept: application/n-triples" https://localhost/idsa/core/Resource redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.nt?"
curl -k -H "Accept: application/n-triples" https://localhost/idsa/core/Resource
echo ""

# check for hash (#) URIs
echo "11. curl -k https://localhost/idsa/core# redirects to https://international-data-spaces-association.github.io/InformationModel/"
curl -k https://localhost/idsa/core#
echo ""

# check for hash (#) URIs (turtle)
echo "12. curl -k -H "Accept: text/turtle" https://localhost/idsa/core#Resource redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/turtle" https://localhost/idsa/core#Resource
echo ""

# check for JSON-LD context
echo "13. curl -k -H "Accept: application/ld+json" https://localhost/idsa/contexts/context.jsonld redirects to https://jira.iais.fraunhofer.de/stash/projects/ICTSL/repos/ids-infomodel-commons/raw/jsonld-context/4.0.0/context.jsonld?"
curl -k -H "Accept: application/ld+json" https://localhost/idsa/contexts/context.jsonld
echo ""

# check for JSON-LD context
echo "14. curl -k https://w3id.org/idsa/contexts/2.0.1/context.jsonld redirects to https://jira.iais.fraunhofer.de/stash/projects/ICTSL/repos/ids-infomodel-commons/raw/jsonld-context/2.0.1/context.jsonld?"
curl -k https://w3id.org/idsa/contexts/2.0.1/context.jsonld
echo ""

# check for content type N3
echo "15. curl -k -H "Accept: text/n3" https://localhost/idsa/core redirects to https://international-data-spaces-association.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/n3" https://localhost/idsa/core
echo ""

# check for testings
echo "16. curl -k https://localhost/idsa/shacl redirects to https://github.com/International-Data-Spaces-Association/InformationModel/releases/download/v4.0.0/ValidationShapesv400.zip?"
curl -k https://localhost/idsa/shacl
echo ""

# check for testings
echo "16. curl -k https://localhost/idsa/shacl/content/ArtifactShape redirects to https://raw.githubusercontent.com/International-Data-Spaces-Association/InformationModel/master/testing/content/ArtifactShape.ttl?"
curl -k https://localhost/idsa/shacl/content/ArtifactShape
echo ""

# check for IDS-G
echo "17. curl -k https://localhost/idsa/ids-g redirects to https://github.com/International-Data-Spaces-Association/IDS-G/tree/master/?"
curl -k https://localhost/idsa/ids-g
echo ""

# check for message docu table
echo "18. curl -k https://localhost/idsa/ids-messages redirects to http://htmlpreview.github.io/?https://github.com/International-Data-Spaces-Association/InformationModel/blob/feature/message_taxonomy_description/model/communication/Message_Description.htm?"
curl -k https://localhost/idsa/ids-messages
echo ""