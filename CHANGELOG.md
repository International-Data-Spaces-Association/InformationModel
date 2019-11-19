# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.0.1] 2019-11-19
Version 2.0.1 of the IDS Information model

### Changed
* Removed property *ids:baseContractOffer* from class *ids:ContractRequestMessage* due to redundancy. By definition *ids:ContractRequestMessage* already requires a contract in its payload. The property is therefore not needed.

### Fixed
* Changed *ids:referingConnector* (class *ids:Token*) from *owl:ObjectProperty* to *owl:DatatypeProperty* with *rdfs:range* *xsd:anyURI*. Allows to reference the connector via an URI.

* Removed *idsm:abstract true* property from *ids:variant* (class *ids:Resource*). Property is invalid, since it is intended to be used by classes only. 

* Minor typo fixes.


## [2.0.0] 2019-10-14
Version 2.0 of the IDS Information model


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
