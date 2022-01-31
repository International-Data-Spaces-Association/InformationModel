# T60 - Reusability through application profiles

## Introduction
In the IDS Information Model we re-used many classes and properties initially defined in other external ontologies. However, we identified possible redundant local definitions of classes and properties. Therefore, we decided to analyze those definitions and determine suitability of their local definition.
Moreover, based on the performed analysis, we understood that a better approach would be to remove those redundant definitions and directly use the external properties in our SHACL shapes instead.

## Goal
Our main goal was to effectively identify and remove all redundant definitions of classes and properties, and directly use the external definitions from the respective existent ontologies.

## Methodology
First, we created a new branch >"refactorIDSModel-enhancement" by clonating the "develop" branch.
After that, we created a list of every external class and property used in the IDS Information Model and evaluated if the use of the property or class was redundant. For that, we considered the following definitions:
Redundant (r): the internal definition of a class or property not adding any additional information to the already external definition.
Possibly Redundant (pr):  the internal definition of a class or property which redundancy is not clear because it adds some level of specificity.
Non-redundant (nr): the internal definition of a class or property adding new information or more specificity, such as domain and range or further constraints.
Our approach for identifying possible redundant definitions was to search in files by using regular expressions: "subClassOf(?!ids)", and "subPropertyOf(?!ids)". We traversed all the results and ignored copies of ontologies. Moreover, we focused on the .ttl files included in the different model definitions, for example communication, or content.
Once we found these results, we listed each class and property by file, the relation (subClassOf or subPropertyOf), and the external class or property which is referring to. Then, for the evaluation (r, pr, nr) as aforementioned, we analyzed the internal definition, for example which other additional information was introduced by it, and we determined the use of that internal definition in the related files in the models, validations, and testing files. Based on the performed evaluation, we made the decisions to keep the class or property, or remove it. Then we proceeded to the concrete implementation of changes as described in the next section.

We describe some examples here:

- The ids:Agent is defined as an extension of the odrl:Party, indeed ids:Agent is defined as a subClassOf odrl:Party. We took the following notes: "It is not clear why ids:Agent needs to be defined as a subclass of two external classes. Based on the information on the ODRL vocabulary, foaf:Agent needs to be used to describe further details of the party. Additionally to odlr:Party and foaf:Agent, it is defined as a subclass of ids:Described. And adds only rdfs:label and rdfs:comment. It is used in Participant.ttl to define ids:Participant, and to define range for ids:publisher, and ids:sovereign in Resource.ttl, ids:senderAgent and ids:recipientAgent in Message.ttl, and ids:hasAgent in Connector.ttl". Based on those evaluation notes, we decided the definition in the IDS Information Model was redundant, and decided to remove the ids:Agent and replaced it by foaf:Agent


- The ids:contentType is defined as a subPropertyOf dct:type, and it adds rdfs:domain (ids:DigitalContent), and rdfs:range (ids:ContentType). We decided that this definition was probably redundant, but we decided to keep it, as it is more specific than dct:type.


- The ids:includedCertificationLevel is defined as a subPropertyOf dct:isPartOf. It adds rdfs:label, rdfs:comment, rdfs:seeAlso, rdfs:domain (ids:CertificationLevel), and range (ids:CertificationLevel). We noticed that it is only used in codes and in validations.
In codes, it is used to define idsc:PARTICIPANT_ENTRY_LEVEL_MANAGEMENT_SYSTEM, idsc:PARTICIPANT_MEMBER_LEVEL_MANAGEMENT_SYSTEM, and others. And it is used to define validations in CertificationShape.ttl. 

## Implementation 
- For the implementation of the first given example, we modified the following files in the model: Message.ttl, Resource.ttl, Connector.ttl, Participant.ttl, were we added @prefix foaf: <http://xmlns.com/foaf/0.1/>, and replace ids:Agent by foaf:Agent. Moreover, we removed the definition of ids:Agent in Participant.ttl. 
In the testing files, only sh:message was modified and the commented code referencing ids:Agent was removed in MessageShape.ttl, ResourceShape.ttl, and ConnectorShape.ttl. 
- For the second example, as the internal definition was more specific, no changes were implemented.
- Lastly, for the third example, We decided to keep it, and therefore no changes were implemented.

Here we list the issues related to the evaluation and implementation of changes.

The initial requirement was the following:
[Issue #413 - Remove redundant class/property definitions whenever external concepts can be used directly](https://github.com/International-Data-Spaces-Association/InformationModel/issues/413)

For that, first we evaluated the redundant, possible redundant, and non-redundant classes and properties, based on the following issue:

[Issue #461 - List and evaluate every usage of external classes or properties](https://github.com/International-Data-Spaces-Association/InformationModel/issues/461)

For the implementation of changes, we refactor the IDS Information Model, and included all the changes under the following issue:

[Issue #504 - Refactor ids model enhancement (directly reuse external concepts instead of copying)](https://github.com/International-Data-Spaces-Association/InformationModel/pull/504)

Moreover, we included a helper file to support the CodeGen tool. It can be found under the issue: 
[Issue #490 - Refactor identified refactoring options for the IDS information model](https://github.com/International-Data-Spaces-Association/InformationModel/issues/490)


## Impact 
After making the aforementioned evaluation and changes, the results are the following:

- SHACL shapes were revised, in which obsolete IDS classes and properties have been replaced by directly using those from external ontologies. 
Link: [Revised SHACL shapes](https://github.com/International-Data-Spaces-Association/InformationModel/pull/504/files?authenticity_token=XVFNq4XvnDG%2B7RiaW4dajYrPiYhNvJduQR6iBOrESAomY91dmV4lzg2WjUWMB3c3cGYFzHUesT95PDoMD2eqkg%3D%3D&file-filters%5B%5D=.ttl&hide-deleted-files=true&w=1)
- The IDS infomodel has been improved. 
Link: [Revised infomodel](https://github.com/International-Data-Spaces-Association/InformationModel/pull/504/commits) 
- A dedicated helper file, which compensates for the copies deleted from the infomodel and thus makes them available to the CodeGen environment, has been developed. This contains a minimal set of all the resources needed to keep code generation stable and reliable.
Link: [Dedicated helper file](https://github.com/International-Data-Spaces-Association/InformationModel/blob/refactorIDSModel-enhancement/utils/refactor_helper.ttl)

- 103 definitions were evaluated, from which 36 were Classes and 67 were Properties.
- We detected 56 probably redundant (pr) cases, 41 redundant (r) cases, and 6 non redundant (nr) cases.
- In 30 cases we made no changes, from which 6 correspond to non redundant (nr) cases and 24 correspond to probably redundant (pr) cases.
- In 72 cases we made changes by removing the local definitions and replacing them by their external definitions, they all correspond to redundant (r) and probably redundant (pr) cases.
- 1 case is pending, and corresponds to the property >"ids:rightOperand"

## Appendix
[List and evaluation of every usage of external classes and properties](https://github.com/International-Data-Spaces-Association/InformationModel/blob/documentationIDSModel-enhacement/evaluation_external/List%20and%20evaluation%20of%20every%20usage%20of%20external%20classes%20and%20properties.pdf)



