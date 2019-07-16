# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased] - 2019-05-24
- Changes applied according to issue [#55](https://github.com/IndustrialDataSpace/InformationModel/issues/55),  authorized by the WG.

### Added
- Class `ids:SecurityGuarantee` added in `model/SecurityProfile.ttl` representing a formalized "guarantee" given by a Connector. Specific subclasses (service isolation guarantee) define a closed, enumerated set of reference values within `codes/SecurityGuarantee.ttl`.
- To deal with OWA the *absence of a guarantee is explicitly indicated* by a type-specific "none" value (`idsc_sec:SERVICE_ISOLATION_NONE`). Validation should ensure no other contradicting value is set for a given guarantee type when assigned to "none".
- The generic object property `ids:securityGuarantee` was added in `model/SecurityProfile.ttl` to link a profile to instances of `ids:SecurityGuarantee` subclasses.    

### Changed

### Removed
- Class `ids:PredefinedSecurityProfile` removed in `model/SecurityProfile.ttl`, since only  a marker with no added benefit - standard, "predefined" profiles have to be identified by a well-known, permanent URI.
- Object property `ids:parentSecurityProfile` removed in `model/SecurityProfile.ttl` to prevent profile composition. Inherited/composed profiles would require a custom interpretation involving issues of evaluation (aggregation vs. overriding), cardinality (single or multiple inheritance) etc. making it overly complex and incompatible with standard RDF/OWL reasoning. Profiles are considered self-contained, no custom logic nor context should be required for their interpretation. 
- Number of object properties derived from the generic  `ids:securityGuarantee`, such as `ids:integrityGuarantee`, was removed since the semantics of the respective guarantee is completely defined by the object value (instance of a `ids:SecurityGuarantee`subclass), e.g.,  `idsc_sec:INTEGRITY_PROTECTION_LOCAL`.

 