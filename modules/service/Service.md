@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dct: <http://purl.org/dc/terms/> .

@prefix ids_int: <https://schema.industrialdataspace.org/interface/> .
@prefix ids_rel: <https://schema.iais.fraunhofer.de/ids/helper/relation/> .
@prefix ids_trans: <https://schema.iais.fraunhofer.de/ids/helper/transformation/> .
@prefix ids_doc: <https://schema.iais.fraunhofer.de/ids/helper/documentation/> .
@prefix ids_contr: <https://schema.industrialdataspace.org/contract/> .
@prefix ids_da: <https://schema.industrialdataspace.org/dataAsset/> .

# Classes
# -------


ids_int:Service a owl:Class;
    rdfs:label "Service"@en;
    rdfs:comment "Service implements an Interface with regard to a communication Protocol."@en
    .

ids_int:DataService rdfs:subClassOf ids_int:Service ;
    rdfs:label "DataService"@en;
    rdfs:comment "Service that processes, stores or otherwise handles data (in contrast to controlling machines etc.)"@en;
    ids_rel:validation [
        ids_rel:forProperty ids_int:binding;
        ids_rel:constraint ids_rel:NotNull;
    ].


# Properties for describing a DataService
# ---------------------------------------

ids_int:binding a owl:ObjectProperty;
    rdfs:domain ids_int:DataService;
    rdfs:range ids_int:ProtocolBinding;
    rdfs:label "binding"@en;
    rdfs:comment "Links to the protocol bindings which define how to technically invoke the Service."@en.

