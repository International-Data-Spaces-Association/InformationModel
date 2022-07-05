# Reference Examples

## Scenario
The reference examples are motivated by a scenario of observing traffic conditions at defined locations along the European highways
for purposes of traffic control, predictive road maintenance, toll fee optimization and so on.

# Resource
A Resource is a single digital content or a coherent set of digital contents exposed at particular conditions via a defined interface. Types of digital content range from structured data, documents, media, software etc. Examples below illustrate the various types and different aspects of resources.


## Example DATA1: Commercial report

Example [DATA1](DATA1.ttl) showcases a download of a simple content, an accident report, elaborated on the basis of a large scale European highway statistics data ([DATA2](DATA2.ttl)) collected within the period 2000 - 2017. The report is provided in two equivalent representations (PDF and MS Word) at the cost of 25 Euro.


## Example TEXT_RESOURCE: 

Example [TEXT_RESOURCE](TEXT_RESOURCE.ttl) is based on the [DATA1](DATA1.ttl) example with minor differencences, contains more comments and explanations and is modelled using InformationModel v1.0.3 architecture


## Example DATA2: Free download of raw, historical data

The resource example [DATA1](DATA1.ttl) illustrates an easy, non-interactive access to historical data provided by the participant [PART1](PART1.ttl). The monthly traffic statistics collected during a year since 2000 are exposed for download as individual files (“artifacts”) via the Trusted Connector [CONN2](CONN2.ttl). The file names (e.g., `E1_20000101.csv`) encode by convention the discriminating parameters, i.e. the highway (e.g., `E37`), year (e.g., `2018`), month (e.g., `01`). The reports comprise tabular data in CSV format. The data may be used free of charge, the policy requires a credits
attribution though.

## Example DATA3: On-line data query

Example [DATA2](DATA2.ttl) introduces simple interactive features allowing the consumer to selectively retrieve content beyond the constraints of server-defined contents as in example [DATA1](DATA1.ttl) (e.g. statistics for a highway section across several years).

## Example APP1: Data App for content integration (system adapter)

The photographs taken by a surveillance camera are injected into the mobile Connector environment [CONN1](CONN1.ttl) by means of the Data App [APP1](APP1.ttl) serving as a technology adapter. It implements a camera driver that accesses the raw digital content and exposes still images in various representations via a defined interface.

## Example APP2: Data App for image anonymization

The image content provided by [APP1](APP1.ttl) have to be anonymized prior to being forwarded to a Data Consumer. The Data App [APP2](APP2.ttl) accepts images of standard traffic scenarios in various file formats (e.g. PNG, JPG) recorded in compliance with the international norm [IEC 62676-4:2014](https://webstore.iec.ch/publication/7353). It is trained to locate particular personal information (e.g., the license plate of a car) and to apply image
processing techniques to irreversibly obfuscate this information. The Data App is likewise deployed within the Mobile Connector [CONN1](CONN1.ttl), i.e. at the source of image recording, in order to prevent the disclosure of unprocessed content.

# Infrastructure components

## Example CONN1: Mobile, base connector

Connectors are the central building blocks, the edge nodes of the IDS network. The example Connector [CONN1](CONN1.ttl) is deployed on a mobile sensor platform located close to a traffic hot spot. It hosts a data processing pipeline where image data received form APP1 is fed into APP2.

## Example CONN2: Trusted connector

The Trusted Connector [CONN2](CONN2.ttl) represents a hardened version of the Connector runtime, a certified platform for data integration, processing and publishing maintained by the participant [PART1](PART1.ttl) as part of its data provisioning infrastructure.  


## Example TRUSTED_CONNECTOR: Trusted connector

The TRUSTED_CONNECTOR [TRUSTED_CONNECTOR](TRUSTED_CONNECTOR.ttl) is based on the [CONN2](CONN2.ttl) example with additional comments.


## Example BROKER1: Logistics broker

Because of the vast amount of resources a dedicated Broker for the "logistics domain" is operated by the service provider [PART2](PART2.ttl). Next to a customer-oriented GUI the data registry exposes a series of service interfaces (APIs) for lif-cycle management (publication,updated, removal) and search of content offerings.  

## Example APPSTORE1: General purpose AppStore

The example AppStore [APPSTORE1](APPSTORE1.ttl) maintains metadata and software resources across IDS communities and providers. The software company PART2 advertises and distributes
its Data Apps (e.g. APP2) via that registry.   

# Participants

## Example PART1: European traffic data provider)

The hypothetical "Highway monitoring and statistics agency" acts as a data provider [PART1](PART1.ttl). It maintains a large-scale infrastructure for monitoring, analysis and prediction of highway utilization statistics in European context. The agency has deployed a range of mobile connectors (e.g. CONN1) for distributed collection and publication of geotagged, regional sensor data, likewise a secure connector (CONN2) for sharing valuable statistics
reports and predictions.


## Example PART2: Software development and service provision

The participant App4Traffic GmbH ([PART2](PART2.ttl)) provides a wide range of software development, consultancy and data hosting services and thus implements multiple roles within the IDS ecosystem. Based in Switzerland (Musterstraße 2, Zürich) the SME develops and distributes IDS Data Apps (e.g. APP1) and serves
customers like PART3 with advanced analytics services based upon data from PART1.   

## Example PART3: Global logistics company

The international "Supercargo Logistics" company provides services around the globe with subsidiaries in a number of countries, among others Supercargo GmbH - headquarters - (Musterstraße 5, Köln, Deutschland), Supercargo OOO (Yлица пример 120, Москва), and Supercargo Ltd. (Sample Road 15c, Hongkong).
Their businesses are thus subject to international, national and optionally some custom regulations (legal areas). The organization complies with the ISIC classification rev. 4 and has ISIC code 4923 (freight transport via road). The company retrieves live traffic monitoring data, in order to supply its drivers with up-to-date traffic information, efficient routing and timely hazard warnings.

# Interactions

In the following examples of business interactions among participants are given. The realization of the core IDS value propositions (secure data transfer between standardized components while ensuring data sovereignty) is supported by interactions (e.g. data transfer) annotated with metadata (instances of the `Message` class in the header part). Metadata descriptions of content being exchanged are mandatory. Therefore, the IDS infomodel introduces a concise set of message types specifying metadata fields that must/should/can be given in order to
facilitate the business interactions.

## Example INTER1: Connector registration at Broker (stable)

The example [INTER1](INTER1.ttl) showcases the publication of Resources as part of the overall "self-description" of a Connector.
Connector CONN2 registers at the Broker INFRA1 by dispatching a dedicated message to the generic Message-API of the Broker (`ConnectorAvailable`). Next to the mandatory fields, the message header identifies the consumer connector (Broker). The message payload comprises the complete "self-description"
document of the registering Connector, i.e., the content of [CONN2](CONN2.ttl) in JSON(-LD) format (default).

## Example INTER2: Broker search and identification of content offerings (stable)

Later on the Connector CONN2 may issue queries on the Broker to learn about Resources available ([INTER2](INTER2.ttl)). For this purpose it dispatches a dedicated request message (`BrokerQuery`), indicating the target scope of the query ("all", or only "active", i.e. live connectors) and the query language
type. The respective query string is supplied as the literal payload. In case of a SPARQL this might be a DESCRIBE_QUERY, e.g. ```DESCRIBE ?content WHERE { ?content a ids:Content  }``` retrieving information about any content available. Upon request completion, a Result message is sent back to the issuing connector CONN2. The Result message is fairly minimal containing only the mandatory fields and a correlation attibute referring to the previously sent request. The resultant payload is an RDF graph serialized as a default or client-selected Representation.  

## Example INTER3: Contract negotiation of the selected contents
Example [INTER3](INTER3.ttl) illustrates the message exchange in order to negotiate a usage contract.
