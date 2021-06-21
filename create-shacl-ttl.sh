#!/bin/bash

write_to_file()
{

    # initialize a local var
    local file="Shacl.ttl"
    local version=$1
    
    if [[ -z "$version" ]] ; then
        echo Warning! No version parameter supplied. >&2
		echo Add version parameter to script. >&2
		echo Example: $'\n\t'sh create-shacl-ttl.sh 4.1.0 $'\n'>&2
		echo Exiting >&2
		exit 1;
    fi
    
    
    # delete old content and add prefixes
    cat > "$file" <<'EOF'
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ids:  <https://w3id.org/idsa/core/> .
@prefix vann: <http://purl.org/vocab/vann/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix voaf: <http://purl.org/vocommons/voaf#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix cc:   <http://creativecommons.org/ns#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#>.
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix shapes: <https://github.com/International-Data-Spaces-Association/InformationModel/tree/master/testing> .

EOF

    # add meta-data
    
    cat >> "$file" <<EOF
# Description of this ontology module
# ----------------------------

shapes:
    a voaf:Vocabulary, owl:Ontology ;
    rdfs:isDefinedBy <https://w3id.org/idsa/core/> ;
    rdfs:label "IDS Information Model"@en ;
    dct:title "The International Data Spaces Information Model"@en ;
    rdfs:comment "This ontology defines classes and properties for describing participants, infrastructure, data and services of the International Data Spaces (formerly known as Industrial Data Space)." ;
    cc:license <http://www.apache.org/licenses/LICENSE-2.0> ;
    dct:creator
       <https://github.com/sebbader> ,
       <https://github.com/Maboeckmann> ,
       <https://github.com/clange> ,
       <https://github.com/HaydarAk> ;
    dct:publisher ids:IDSA ;
    dct:created "2019-10-14"^^xsd:date ;
    dct:modified "$(date +%Y-%m-%d)"^^xsd:date ;
    owl:versionInfo "${version}" ;
    owl:versionIRI <https://github.com/International-Data-Spaces-Association/InformationModel/tree/master/testing/${version}> ;
    vann:preferredNamespaceUri "https://github.com/International-Data-Spaces-Association/InformationModel/tree/master/testing" ;
    vann:preferredNamespacePrefix "shapes" ;
    rdfs:seeAlso <https://international-data-spaces-association.github.io/InformationModel/> ;
    void:vocabulary
       sh: ,
       xsd: ,
       ids: ;
.

<http://www.apache.org/licenses/LICENSE-2.0>
    rdfs:label "Apache License Version 2.0, January 2004" ;
.

ids:IDSA
    a dct:Agent, foaf:Organization ;
    foaf:homepage <https://www.internationaldataspaces.org> ;
    rdfs:label "International Data Spaces Association" ;
.
<https://github.com/sebbader> a dct:Agent, foaf:Person ;
    foaf:name "Sebastian Bader" ;
.
<https://github.com/HaydarAk> a dct:Agent, foaf:Person ;
    foaf:name "Haydar Akyürek" ;
.
<https://github.com/clange> a dct:Agent, foaf:Person ;
    foaf:name "Christoph Lange" ;
.
<https://github.com/Maboeckmann> a dct:Agent, foaf:Person ;
    foaf:name "Matthias Böckmann" ;
.
EOF
    
    # search for files in selected folders
    echo '# ----------------------------' >> "$file"
    echo '# Imports of class files' >> "$file"
    echo 'shapes:' >> "$file"

    # search for files in selected folders (omitting metamodel/)
    for class in $(find \
                       testing/* \
                       -maxdepth 1 -mindepth 1 -name "*.ttl")
    do
        if [[ -f $class ]]; then
            echo "    owl:imports <$class> ;" >> "$file"
        fi
    done
    
    echo ". " >> "$file"
}

# execute it
write_to_file $1
