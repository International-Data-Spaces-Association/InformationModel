#!/bin/bash

write_to_file()
{

     # initialize a local var
     local file="Ontology.ttl"
	 local version=$1
	 if [ -z "$version" ] ; then
		echo "Warning! No version parameter supplied. Assuming version 1.0.2"
		version="1.0.2"
	 fi


	#delete old content and add prefixes
	echo "@prefix owl: <http://www.w3.org/2002/07/owl#> ." > "$file"
	echo "@prefix dct: <http://purl.org/dc/terms/> ." >> "$file"
	echo "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> ." >> "$file"
	echo "@prefix prov: <http://www.w3.org/ns/prov#> ." >> "$file"
	echo "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> ." >> "$file"
	echo "@prefix ids: <https://w3id.org/idsa/core/> ." >> "$file"
	echo "@prefix vann: <http://purl.org/vocab/vann/> ." >> "$file"
	echo "@prefix void: <http://rdfs.org/ns/void#>." >> "$file"
	echo "@prefix voaf: <http://purl.org/vocommons/voaf#>." >> "$file"
	echo "@prefix foaf: <http://xmlns.com/foaf/0.1/>." >> "$file"
	echo "@prefix cc: <http://creativecommons.org/ns#>. " >> "$file"
	echo "@prefix xsd: <http://www.w3.org/2001/XMLSchema#>." >> "$file"
	echo "" >> "$file"

	#add meta-data
	
	echo '# Description of this ontology' >> "$file"
	echo '# ----------------------------' >> "$file"
	echo '' >> "$file"
	echo 'ids:' >> "$file"
	echo '    a voaf:Vocabulary, owl:Ontology ;' >> "$file"
	echo '    rdfs:isDefinedBy <https://w3id.org/idsa/core/> ;' >> "$file"
	echo '    rdfs:label "IDS Information Model"@en;' >> "$file"
	echo '    dct:title "The Industrial Dataspace Information Model"@en;' >> "$file"
	echo '    rdfs:comment "This ontology defines classes and properties for describing participants, infrastructure, data and services of the Industrial Dataspace.";' >> "$file"
	echo '    cc:license <http://www.apache.org/licenses/LICENSE-2.0> ;' >> "$file"
	echo '    dct:creator <https://github.com/cmader> ;' >> "$file"
	echo '    dct:creator <https://github.com/jpullmann> ;' >> "$file"
	echo '    dct:creator <http://sebastian.tramp.name> ;' >> "$file"
	echo '    dct:contributor _:AndreasMueller ;' >> "$file"
	echo '    dct:contributor _:AnnaKasprzik ;' >> "$file"
	echo '    dct:publisher ids:IDSA ;' >> "$file"
	echo '    dct:created "2017-09-26"^^xsd:date;' >> "$file"
	echo '    dct:modified "'$(date +%Y-%m-%d)'"^^xsd:date;' >> "$file"
	echo '    owl:versionInfo "'$version'";' >> "$file"
	echo '    owl:versionIRI "https://w3id.org/idsa/core/'$version'>";' >> "$file"
	echo '    vann:preferredNamespaceUri "https://w3id.org/idsa/core/";' >> "$file"
	echo '    vann:preferredNamespacePrefix "ids" ;' >> "$file"
	echo '    void:vocabulary' >> "$file"
	echo '       <http://purl.org/vocab/vann/> ,' >> "$file"
	echo '       <http://rdfs.org/ns/void#> ,' >> "$file"
	echo '       <http://purl.org/vocommons/voaf#> ,' >> "$file"
	echo '       <http://purl.org/dc/terms/> ,' >> "$file"
	echo '       <http://purl.org/vocab/vann/> ,' >> "$file"
	echo '       <http://xmlns.com/foaf/0.1/> ;' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo '<http://www.apache.org/licenses/LICENSE-2.0>' >> "$file"
	echo '    rdfs:label "Apache License Version 2.0, January 2004" ;' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo 'ids:IDSA' >> "$file"
	echo '    a dct:Agent, foaf:Organization;' >> "$file"
	echo '    foaf:homepage <https://www.internationaldataspaces.org> ;' >> "$file"
	echo '    rdfs:label "International Data Spaces Association" ;' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo '<http://sebastian.tramp.name>' >> "$file"
	echo '    a dct:Agent, foaf:Person ;' >> "$file"
	echo '    foaf:name "Sebastian Tramp";' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo '<https://github.com/cmader>' >> "$file"
	echo '    a dct:Agent, foaf:Person ;' >> "$file"
	echo '    foaf:name "Christian Mader";' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo '<https://github.com/jpullmann>' >> "$file"
	echo '    a dct:Agent, foaf:Person ;' >> "$file"
	echo '    foaf:name "Jaroslav Pullmann";' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo '_:AndreasMueller' >> "$file"
	echo '    a dct:Agent, foaf:Person ;' >> "$file"
	echo '    foaf:name "Andreas Müller"' >> "$file"
	echo '.' >> "$file"
	echo '' >> "$file"
	echo '_:AnnaKasprzik a dct:Agent, foaf:Person ;' >> "$file"
	echo '    foaf:name "Anna Kasprzik";' >> "$file"
	echo '.' >> "$file"
	
	# "open the file to edit" ... not required. echo will do

	# search for files in selcted folders
	echo '# ----------------------------' >> "$file"
	echo '# Imports of class files' >> "$file"
	echo 'ids:' >> "$file"
	for class in $(find model/* -name "*.ttl")
	do
		if [[ -f $class ]]; then
			echo "    owl:imports <$class> ; " >> "$file"
		fi
	done
	# search for files in selcted folders
	echo '# ----------------------------' >> "$file"
	echo '# Imports of class files' >> "$file"
	echo 'ids:' >> "$file"
	for class in $(find taxonomies/* -name "*.ttl")
	do
		if [[ -f $class ]]; then
			echo "    owl:imports <$class> ; " >> "$file"
		fi
	done
	
	echo ". " >> "$file"
 }

# execute it
write_to_file $1