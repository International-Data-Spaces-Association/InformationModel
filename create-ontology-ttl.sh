#!/bin/bash

write_to_file()
{

    # initialize a local var
    local file="Ontology.ttl"
    local version=$1
    
    if [[ -z "$version" ]] ; then
        version="2.0.1"
        echo "Warning! No version parameter supplied. Assuming version ${version}" >&2
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

EOF

    # add meta-data
    
    cat > "$file" <<EOF
# Description of this ontology
# ----------------------------

ids:
    a voaf:Vocabulary, owl:Ontology ;
    rdfs:isDefinedBy <https://w3id.org/idsa/core/> ;
    rdfs:label "IDS Information Model"@en ;
    dct:title "The International Data Spaces Information Model"@en ;

    rdfs:comment "This ontology defines classes and properties for describing participants, infrastructure, data and services of the International Data Spaces (formerly known as Industrial Data Space)." ;
    cc:license <http://www.apache.org/licenses/LICENSE-2.0> ;
    dct:creator
       <https://github.com/cmader> ,
       <https://github.com/jpullmann> ,
       <http://sebastian.tramp.name> ;
    dct:contributor
       _:AndreasMueller ,
       _:AnnaKasprzik ,
       <https://github.com/sebbader> ,
       <https://github.com/Madmatti/> ,
       <https://github.com/HaydarAk> ;
    dct:publisher ids:IDSA ;
    dct:created "2017-09-26"^^xsd:date ;
    dct:modified "$(date +%Y-%m-%d)"^^xsd:date ;
    owl:versionInfo "${version}" ;
    owl:versionIRI "https://w3id.org/idsa/core/${version}>" ;
    vann:preferredNamespaceUri "https://w3id.org/idsa/core/" ;
    vann:preferredNamespacePrefix "ids" ;
    rdfs:seeAlso <https://industrialdataspace.github.io/InformationModel/> ;
    void:vocabulary
       <http://purl.org/vocab/vann/> ,
       <http://rdfs.org/ns/void#> ,
       <http://purl.org/vocommons/voaf#> ,
       <http://purl.org/dc/terms/> ,
       <http://purl.org/vocab/vann/> ,
       <http://xmlns.com/foaf/0.1/> ;
.

<http://www.apache.org/licenses/LICENSE-2.0>
    rdfs:label "Apache License Version 2.0, January 2004" ;
.

ids:IDSA
    a dct:Agent, foaf:Organization ;
    foaf:homepage <https://www.internationaldataspaces.org> ;
    rdfs:label "International Data Spaces Association" ;
.

<http://sebastian.tramp.name>
    a dct:Agent, foaf:Person ;
    foaf:name "Sebastian Tramp" ;
.
<https://github.com/cmader>
    a dct:Agent, foaf:Person ;
    foaf:name "Christian Mader" ;
.
<https://github.com/jpullmann>
    a dct:Agent, foaf:Person ;
    foaf:name "Jaroslav Pullmann" ;
.
_:AndreasMueller
    a dct:Agent, foaf:Person ;
    foaf:name "Andreas Müller"
.
_:AnnaKasprzik a dct:Agent, foaf:Person ;
    foaf:name "Anna Kasprzik" ;
.
<https://github.com/sebbader> a dct:Agent, foaf:Person ;
    foaf:name "Sebastian Bader" ;
.
<https://github.com/HaydarAk> a dct:Agent, foaf:Person ;
    foaf:name "Haydar Akyürek" ;
.
<https://github.com/Madmatti> a dct:Agent, foaf:Person ;
    foaf:name "Matthias Böckmann" ;
.
EOF
    
    # "open the file to edit" ... not required. echo will do

    # search for files in selected folders
    echo '# ----------------------------' >> "$file"
    echo '# Imports of class files' >> "$file"
    echo 'ids:' >> "$file"

    for class in $(find model/* -maxdepth 1 -name "*.ttl")
    do
        if [[ -f $class ]]; then
            echo "    owl:imports <$class> ; " >> "$file"
        fi
    done
    

    # search for files in selected folders
    #for class in $(find metamodel/* -name "*.ttl")
    #do
    #    if [[ -f $class ]]; then
    #        echo "    owl:imports <$class> ; " >> "$file"
    #    fi
    #done
    
    # search for files in selected folders
    for class in $(find taxonomies/* -maxdepth 1 -name "*.ttl")
    do
        if [[ -f $class ]]; then
            echo "    owl:imports <$class> ; " >> "$file"
        fi
    done


    for class in $(find codes/* -maxdepth 1 -name "*.ttl")
    do
        if [[ -f $class ]]; then
            echo "    owl:imports <$class> ; " >> "$file"
        fi
    done
    
    echo ". " >> "$file"
 }

# execute it
write_to_file $1

#  LocalWords:  ttl fi EOF dct rdfs rdf vann voaf foaf xsd EOF voaf
#  LocalWords:  rdfs isDefinedBy rdfs dct Dataspace rdfs Dataspace
#  LocalWords:  dct dct dct dct AndreasMueller dct AnnaKasprzik dct
#  LocalWords:  dct dct dct IDSA dct xsd dct xsd versionInfo vann dct
#  LocalWords:  versionIRI preferredNamespaceUri vann rdfs seeAlso
#  LocalWords:  preferredNamespacePrefix rdfs IDSA foaf foaf rdfs dct
#  LocalWords:  foaf foaf dct foaf foaf Mader dct foaf foaf Jaroslav
#  LocalWords:  Pullmann AndreasMueller dct foaf foaf Andreas Müller
#  LocalWords:  AnnaKasprzik dct foaf foaf Kasprzik dct foaf foaf dct
#  LocalWords:  Bader foaf
