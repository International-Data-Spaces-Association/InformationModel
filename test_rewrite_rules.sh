#!/bin/bash

echo "This script executes a set of http requests in order to test the linked data compliance of our hosted IDS ontology files."
echo ""

# basic check
echo "1. Redirects to https://www.internationaldataspaces.org/?"
curl -k https://localhost/idsa/
echo ""

# check for content type HTML
echo "2. Redirects to https://industrialdataspace.github.io/InformationModel/?"
curl -k -H "Accept: text/html" https://localhost/idsa/core/
echo ""

# check for content type Turtle
echo "3. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/turtle" https://localhost/idsa/core/
echo ""

# check for content type RDF/XML
echo "4. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.xml?"
curl -k -H "Accept: application/rdf+xml" https://localhost/idsa/core/
echo ""

# check for content type JSON-LD
echo "5. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.json?"
curl -k -H "Accept: application/ld+json" https://localhost/idsa/core/
echo ""

# check for content type n-triples
echo "5. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.nt?"
curl -k -H "Accept: application/n-triples" https://localhost/idsa/core/
echo ""



# check for requesting ids:Resource (HTML)
echo "6. Redirects to https://industrialdataspace.github.io/InformationModel/docs/index.html#/Resource?"
curl -k -H "Accept: text/html" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (Turtle)
echo "7. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/turtle" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (RDF/XML)
echo "8. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.xml"
curl -k -H "Accept: application/rdf+xml" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (JSON-LD)
echo "9. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.json?"
curl -k -H "Accept: application/ld+json" https://localhost/idsa/core/Resource
echo ""

# check for requesting ids:Resource (n-triples)
echo "10. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.nt?"
curl -k -H "Accept: application/n-triples" https://localhost/idsa/core/Resource
echo ""

# check for hash (#) URIs
echo "11. Redirects to https://industrialdataspace.github.io/InformationModel/"
curl -k https://localhost/idsa/core#
echo ""

# check for hash (#) URIs (turtle)
echo "12. Redirects to https://industrialdataspace.github.io/InformationModel/docs/serializations/ontology.ttl?"
curl -k -H "Accept: text/turtle" https://localhost/idsa/core#Resource
echo ""

# check for JSON-LD context
echo "13. Redirects to https://jira.iais.fraunhofer.de/stash/projects/ICTSL/repos/ids-infomodel-commons/raw/jsonld-context/2.0.1/context.jsonld?"
curl -k -H "Accept: application/ld+json" https://w3id.org/idsa/contexts/context.jsonld
echo ""

# check for JSON-LD context
echo "14. Redirects to https://jira.iais.fraunhofer.de/stash/projects/ICTSL/repos/ids-infomodel-commons/raw/jsonld-context/2.0.1/context.jsonld?"
curl -k https://w3id.org/idsa/contexts/2.0.1/context.jsonld
echo ""