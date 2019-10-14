# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.0.0] 2019-10-14
Version 2.0 of the IDS Information model

### Added
- ids:DynamicAttributeToken, subclass of ids:Token
- ids:ParIS
- Additional SHACL Shapes for testing

### Changed
 * Connector is now SubClass of InfrastructureComponent (Broker, ParIS, DAPS, IP, AppStore)

 * ids:SecurityProfile is now used for pre-defined security profiles. Removed ids:CustomSecurityProfile:

 * Messages: Additional classes / properties for the ids:Message taxonomy to further specify and distinguish different messages types
     * Update of notification messages related to (in-)avalibility and changes of a component or it's certification
     * ids:QueryMessage now uses codes for message targets (e.g.  BROKER, APPSTORE, ANY) and scopes (ALL, ACTIVE_ONLY, INACTIVE_ONLY)
     * New class ids:ContractSupplementMessage to exchange information to access a resource of a contract
     * New class LogNotification, which is intended for logging messages

- Policies: LeftOperand, Operator more restrictive.  Additional operands and operators for different constraint types. 

### Removed

- Removing plural forms for properties: A catalog can have can have several “ids:offer” triples but must not have any with “ids:offer*s*”
