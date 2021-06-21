
# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## [4.1.0] 2021-05-26
Version 4.1.0 of the IDS Information Model

### Added

* `ids:ConfigurationManager` can refer to the configured App Resources, Brokers, App Stores and Clearing Houses represented as catalogs.
* `ids:AppRoute` can refer to Broker and Clearing House instances (via `ids:appRouteClearingHouse` and `ids:appRouteBroker`), which are used for publishing and logging related communication.
* `ids:GenericEndpoint` for non-IDS endpoints.
* Catalog subclasses for Broker, AppStore, AppResource and ClearingHouse instances. Check the [Catalog.ttl](model/infrastructure/Catalog.ttl) class for details.
* Additional properties for Participants for identification and classification, e.g., legal name, business identifier, legal form and VAT ID (addressing requirements to participants in Gaia-X)
* Additional properties for `ids:DataApp` and `ids:AppRepresentation` to express supported usage policies as well as app-related runtime, configuration and deployment information.

### Changed:
* `ids:ParticipantRequestMessage` and `ids:ParticipantResponseMessage` are deprecated and will be removed in the next release. Using `ids:DescriptionRequestMessage` and `ids:DescriptionReponseMessage` is advised.


### Removed
* `idsm:` metamodel annotations, which were used to annotate cardinalities of properties. The property cardinalities and restrictions are now exclusively represented via the corresponding SHACL shapes found in the [testing subdirectory](testing/)


## [4.0.0] 2020-08-04
Version 4.0.0 of the IDS Information Model

### Added

* `ids:ConfigurationModel` class for Connector configuration and deployment related information.
  * Several complementary classes, including `ids:Proxy`, `ids:LogLevel`, `ids:AppRoute`, `ids:UserAuthentication`.
* Redesign of `ids:DataApp` class.
  * `ids:DataApp` as superclass of `ids:OrchestrationApp`, `ids:SmartDataApp`, `ids:SystemAdapterApp` .
  * New properties `ids:appDocumentation` with range `xsd:string` and `ids:appEndpoint` with range `ids:AppEndpoint` to enable app and app endpoint documentation.
* `ids:AppEndpoint`, a subclass of `ids:Endpoint` to describe data app endpoints, such as path suffixes, ports and endpoint documentation.
* Languages for `ids:Representation` via the `ids:language` property.
* `ids:ResourceCatalog`, `ids:ConnectorCatalog` and `ids:ParticipantCatalog` as subclasses of `ids:Catalog` to enable infrastructure components, e.g., Broker and ParIS, to present Connector- and Participant-specific catalogs.
* New messages:
  * Messages for app-related communication between App Provider and App Store.
  * `ids:UploadMessage` and `ids:UploadResponseMessage` to allow data upload to a recipient.

### Changed

* Major changes on the IDS Usage Policy Language. See section [IDS Usage Policy Language – Updates and major Changes](#usagepolicy-4.0.0) below.

* `ids:MediaType`. Removed instances for `ids:IANAMediaType`.
    * Media types via `ids:mediaType` with range `ids:IANAMediaType` should be used with the corresponding [IANA URLs](https://www.iana.org/assignments/media-types/media-types.xhtml), as these have complete coverage. E.g., for JSON-LD:
    ```JSON
    "ids:mediaType": {
      "@id":   "https://www.iana.org/assignments/media-types/application/ld+json",
      "@type": "ids:IANAMediaType"
    }
    ```
    * For custom media types (`ids:CustomMediaType`), it is advised to use a recognizable unique identifier.

* Renamed property `ids:catalog` of Connector to `ids:resourceCatalog` and changed range to `ids:ResourceCatalog`.
* Connectors can now present multiple catalogs via the `ids:resourceCatalog` property.
* Switched range of `ids:standardLicense` property from `ids:License` to `xsd:anyURI`. There is no vocabulary with a complete, regularly updated list of software and data licenses which we can provide as instances of the `ids:License` class, to the best of our knowledge. Users should provide the IRI of the correct license. We recommend using sources such as [Wikidata](http://www.wikidata.org/) to search for most common licenses.
* `ids:contentStandard` properties of class `ids:DigitalContent` and `ids:representationStandard` properties of class `ids:Representation` now have range `xsd:anyURI`.
* Redesign of `ids:Endpoint` class.
  * Removed `ids:InteractiveEndpoint`.
  * `ids:StaticEndpoint` is now called `ids:ConnectorEndpoint`. `ids:ConnectorEndpoint` contains additional properties, especially for endpoint description and documentation.
  * `ids:Host` information is now part of the `ids:Endpoint`.
  * New property: `ids:endpointInformation` with range `xsd:string` and `ids:endpointDocumentation` with range `xsd:anyURI` for endpoint description and documentation.
* Core classes for digital content (`ids:Resource`, `ids:DigitalContent`, `ids:Representation`, `ids:Artifact`) now aligned with W3C [DCAT 2](https://www.w3.org/TR/vocab-dcat-2/)

### Removed
* Classes related to runtime related interaction, such as `ids:Operation`, `ids:Activity`, `ids:Interface`, `ids:Parameter`.
* `ids:Host`. Information are now part of the `ids:Endpoint` itself.
* `ids:transportCertsSha256` from Connector class. Property should only be part of the `ids:Token` class.
* Some `ids:Resource` and `ids:Representation` subclasses, such as `ids:SchemaResource` and `ids:SimpleResource`.
* Some unused classes, e.g., `ids:Audio`, `ids:Video`, `ids:Text`
* Refactoring of `ids:Message` subclasses:
    * Removed `ids:...AvailableMessage` notifications for `ids:Resource`, `ids:Connector` and `ids:Participant`. The corresponding update messages, e.g., `ids:ResourceUpdateMessage`, should now be used to announce availability and updates.



## <a name="usagepolicy-4.0.0">IDS Usage Policy Language – Updates and major Changes</a>


The first version of the IDS Usage Policy Language has been created by the end of 2019 and presented the combined state of discussion of the IDS community. As such, it of course reflected the best intentions and views at that time. However, the following developments, examinations and the deeper understanding of the topic now requires a major update, which is provided with this document and implemented as an integral part into the IDS Information Model version 4.0.0. Obviously, it is still unlikely that the language itself is already finished and no further updates will become necessary. Nevertheless, the significant improvements and lessons learned since 2019 certainly justify this rework of the Usage Policy Language.

At the core, the usage policy classes and the closely related templates have been affected most. The IDS community has understood the deficiencies of the original set and therefore developed the current classifications. Integrating several perspectives – legal, data modelling, business-driven, and from an enforcement perspective – the current proposals should be mature and expressive enough to reflect most use cases.

In addition, the Actions, LeftOperands, and BinaryOperators have been further restricted and defined in order to minimize the uncertainty about their meaning, requirements and implications. An IDS Contract must not be interpreted differently by different systems, while both claim a correct implementation of the language. For instance, the operators for ‘Time’ now have defined datatypes, and a clear semantics of how temporal entities are compared.

The intended communication process for improvements, new use cases or bug reports is aligned with the IDS Information Model in general. Deficiencies and/or errors can be discussed with the responsible working group through GitHub Issues in the IDS Information Model GitHub Repository.

---


## [3.1.0] 2020-04-30
Version 3.1.0 of the IDS Information Model


### Added

* `ids:created` and `ids:modified` properties with range `xsd:dateTimeStamp` for `ids:Resource` and `ids:Representation`
* `ids:hasEndpoint` property for `ids:Connector` with range `ids:Endpoint`


### Fixed

* `ids:rightOperand` and `ids:rightOperandReference` (class `ids:Constraint`) changed range to `rdfs:Resource`. Even though both properties allow similar values, their inteded usage differs (cf. the specification of the underlying [ODRL ontology](https://www.w3.org/ns/odrl/2/ODRL20.html)). `ids:rightOperand` values should be interpreted directly, while `ids:rightOperandReference` values _must_ be dereferenced beforehand.

* An `ids:Constraint` is only valid, if either `ids:rightOperandReference` _or_ `ids:rightOperand` is used. Using both properties is not permitted by the corresponding SHACL shape. This behaviour is once more suggested by [ODRL](https://www.w3.org/ns/odrl/2/ODRL20.html).

* Dynamic Attribute Token (DAT) aligned to current specification in the IDS Communication Guide. DAT is now represented by the `ids:DatRequestPayload` and `ids:DatPayload` classes. While `ids:DatRequestPayload` represents the content of the token (a.k.a. claims) a clients sends to the DAPS, the `ids:DatPayload` represents the content of the token a DAPS issues after validation.

* SHACL shapes for properties with IRI ranges. Property values written as defined by the RDF serialisations should now be correctly validated.

---

## [3.0.0] 2020-03-04
Version 3.0.0 of the IDS Information Model

### Added

* Request- and ResponseMessages for the ParIS service.

* Revised Usage Control model based on the [Open Digital Rights Language (ODRL)](https://www.w3.org/TR/odrl-model/)

* Templates for Usage Control using the [SPARQL Inferencing Notation (SPIN)](https://www.w3.org/Submission/spin-overview/)

* New Connector property `ids:hasAgents`. A Connector can now publish its agents as part of the self-description.

* [RDF validation with SHACL](examples/rdf-validation-using-shacl) documentation with examples using CLI tools and the Apache Jena Framework for Java.

* [Perl script](utils/rdf_void_annotation.pl) as an example for extracting metadata from RDF data resources using the [Vocabulary of Interlinked Datasets (VoID)](https://www.w3.org/TR/void/) ontology.


### Changed

* Redesign of the DynamicAttributeToken (DAT) based on the new Dynamic Attribute Provisioning Service (DAPS) version. Check the corresponding [Token](model/security/Token.ttl) class as well as the [DAT payload example](examples/DAT_PAYLOAD.jsonld) for more information.

* `ids:RequestMessage`, `ids:ResponseMessage`, `ids:NotificationMessage` not _abstract_ any more. These messages can now be used directly for non-core IDS communication.

* `ids:DescriptionRequestMessage`(previously called `ids:SelfDescriptionRequest`) now accepts an optional URI. This can be used to either retrieve a component's self-description (by providing its own URI or nothing) or to retrieve metadata about a specific element by providing the element's URI.

* Renamed some existing `ids:Message`s. Check the [Documentation Table of the ids:Message taxonomy](http://htmlpreview.github.io/?https://github.com/IndustrialDataSpace/InformationModel/blob/feature/message_taxonomy_description/model/communication/Message_Description.htm) for the current naming.

### Fixed

* `ids:Message` now correctly labelled as _abstract_ since it is not intended to be used directly.

---

## [2.1.0] 2019-12-02
Version 2.1.0 of the IDS Information Model

### Added

* New class *ids:VocabularyData*. Partial mapping of the [Vocabulary of Interlinked Datasets (VoID)](https://www.w3.org/TR/void/) in the IDS Information Model. It can be used to reference domain-specific vocabularies and terminologies.

* New class *ids:DescribedSemantically*. Superclass of *ids:Resource* and *ids:Representation*. *ids:DescribedSemantically* introduces two new properties:
    - *ids:domainVocabulary* with range *ids:VocabularyData*. Allows using instances of class *ids:VocabularyData* to reference domain-specific terminologies used in *ids:Resource* /  *ids:Representation* .
    - *ids:shapesGraph* (an import of *[sh:shapesGraph](https://www.w3.org/TR/shacl/#sh-shapes-graph)*) with range *xsd:anyURI*. URI should refer to an RDF graph containing SHACL shapes, which describes the domain-specific semantics of a Resource / Representation.

* Travis CI script for validating correctness of Turtle files in Pull Requests.

* SHACL Shapes for the new RDF classes and properties.

* Example of *ids:Resource* (in JSON-LD and RDF/TTL) and corresponding SHACL shapes to describe (temperature) sensor data with domain-specific semantics. Example and README can be found in the /*examples/domain-specific semantics using SHACL* directory.

---

## [2.0.1] 2019-11-19
Version 2.0.1 of the IDS Information Model

### Changed
* Removed property *ids:baseContractOffer* from class *ids:ContractRequestMessage* due to redundancy. By definition *ids:ContractRequestMessage* already requires a contract in its payload. The property is therefore not needed.

### Fixed
* Changed *ids:referingConnector* (class *ids:Token*) from *owl:ObjectProperty* to *owl:DatatypeProperty* with *rdfs:range* *xsd:anyURI*. Allows to reference the connector via an URI.

* Removed *idsm:abstract true* property from *ids:variant* (class *ids:Resource*). Property is invalid, since it is intended to be used by classes only.

* Minor typo fixes.

---

## [2.0.0] 2019-10-14
Version 2.0 of the IDS Information Model


### Added
- ids:DynamicAttributeToken, subclass of ids:Token
- ids:ParIS
- Additional SHACL Shapes for schema validation
- ids:contentVersion property. Version identifier for ids:Message payload, indicates the version of the description of the information in the payload.


### Changed
 * Connector is now subClass of InfrastructureComponent (Broker, ParIS, DAPS, IP, AppStore)

 * ids:SecurityProfile is now used for pre-defined security profiles. Removed ids:CustomSecurityProfile.

 * Messages: Additional classes / properties for the ids:Message taxonomy to further specify and distinguish different message types
     * Update of notification messages related to (un-)availability and changes of a component or its certification
     * ids:QueryMessage now uses codes for message targets (e.g., BROKER, APPSTORE, ANY) and scopes (ALL, ACTIVE_ONLY, INACTIVE_ONLY)
     * New class ids:ContractSupplementMessage to exchange information to access a resource of a contract
     * New class ids:LogNotification, which is intended for logging messages

 * Policies: LeftOperand, Operator more restrictive.  Additional operands and operators for different constraint types.

 * Reduced namespace: ids_ for core model classes / properties, idsc_ for codes and idsm_ for metamodel classes / properties

### Removed

- Removing plural forms for properties: A catalog can have can have several “ids:offer” triples but must not have any with “ids:offer*s*”
