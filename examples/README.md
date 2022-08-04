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

The resource example [DATA1](DATA1.ttl) illustrates an easy, non-interactive access to historical data provided by the participant [PARTICIPANT_1](PARTICIPANT_1.ttl). The monthly traffic statistics collected during a year since 2000 are exposed for download as individual files (“artifacts”) via the Trusted Connector [CONNECTOR_2](CONNECTOR_2.ttl). The file names (e.g., `E1_20000101.csv`) encode by convention the discriminating parameters, i.e. the highway (e.g., `E37`), year (e.g., `2018`), month (e.g., `01`). The reports comprise tabular data in CSV format. The data may be used free of charge, the policy requires a credits
attribution though.

## Example DATA3: On-line data query

Example [DATA3](DATA3.ttl) introduces simple interactive features allowing the consumer to selectively retrieve content beyond the constraints of server-defined contents as in example [DATA1](DATA1.ttl) (e.g. statistics for a highway section across several years).

## Example APP_RESOURCE: Data App for image anonymization

The Data App [APP_RESOURCE](APP_RESOURCE.ttl) accepts images of standard traffic scenarios in various file formats (e.g. PNG, JPG) recorded in compliance with the international norm [IEC 62676-4:2014](https://webstore.iec.ch/publication/7353). It is trained to locate particular personal information (e.g., the license plate of a car) and to apply image
processing techniques to irreversibly obfuscate this information. The Data App is likewise deployed within the Mobile Connector [CONNECTOR_1](CONNECTOR_1.ttl), i.e. at the source of image recording, in order to prevent the disclosure of unprocessed content.

# Infrastructure components

## Example CONNECTOR_1: Mobile, base connector

Connectors are the central building blocks, the edge nodes of the IDS network. The example Connector [CONNECTOR_1](CONNECTOR_1.ttl) is deployed on a mobile sensor platform located close to a traffic hot spot.

## Example CONNECTOR_2: Trusted connector

The Trusted Connector [CONNECTOR_2](CONNECTOR_2.ttl) represents a hardened version of the Connector runtime, a certified platform for data integration, processing and publishing maintained by the participant [PARTICIPANT_1](PARTICIPANT_1.ttl) as part of its data provisioning infrastructure.  


## Example TRUSTED_CONNECTOR: Trusted connector

The TRUSTED_CONNECTOR [TRUSTED_CONNECTOR](TRUSTED_CONNECTOR.ttl) is based on the [CONNECTOR_2](CONNECTOR_2.ttl) example with additional comments.


## Example BROKER: Logistics broker

Because of the vast amount of resources a dedicated Broker for the "logistics domain" is operated by the service provider [PARTICIPANT_2](PARTICIPANT_2.ttl). Next to a customer-oriented GUI the data registry exposes a series of service interfaces (APIs) for lif-cycle management (publication,updated, removal) and search of content offerings.  

## Example APPSTORE: General purpose AppStore

The example AppStore [APPSTORE](APPSTORE.ttl) maintains metadata and software resources across IDS communities and providers. The software company PARTICIPANT_2 advertises and distributes
its Data Apps (e.g. APP_RESOURCE) via that registry.   

# Participants

## Example PARTICIPANT_1: European traffic data provider)

The hypothetical "Highway monitoring and statistics agency" acts as a data provider [PARTICIPANT_1](PARTICIPANT_1.ttl). It maintains a large-scale infrastructure for monitoring, analysis and prediction of highway utilization statistics in European context. The agency has deployed a range of mobile connectors (e.g. CONNECTOR_1) for distributed collection and publication of geotagged, regional sensor data, likewise a secure connector (CONNECTOR_2) for sharing valuable statistics
reports and predictions.


## Example PARTICIPANT_2: Software development and service provision

The participant App4Traffic GmbH ([PARTICIPANT_2](PARTICIPANT_2.ttl)) provides a wide range of software development, consultancy and data hosting services and thus implements multiple roles within the IDS ecosystem. Based in Switzerland (Musterstraße 2, Zürich) the SME develops and distributes IDS Data Apps and serves
customers like PARTICIPANT_3 with advanced analytics services based upon data from PARTICIPANT_1.   

## Example PARTICIPANT_3: Global logistics company

The international "Supercargo Logistics" company provides services around the globe with subsidiaries in a number of countries, among others Supercargo GmbH - headquarters - (Musterstraße 5, Köln, Deutschland), Supercargo OOO (Yлица пример 120, Москва), and Supercargo Ltd. (Sample Road 15c, Hongkong).
Their businesses are thus subject to international, national and optionally some custom regulations (legal areas). The organization complies with the ISIC classification rev. 4 and has ISIC code 4923 (freight transport via road). The company retrieves live traffic monitoring data, in order to supply its drivers with up-to-date traffic information, efficient routing and timely hazard warnings.

# Interactions

In the following examples of business interactions among participants are given. The realization of the core IDS value propositions (secure data transfer between standardized components while ensuring data sovereignty) is supported by interactions (e.g. data transfer) annotated with metadata (instances of the `Message` class in the header part). Metadata descriptions of content being exchanged are mandatory. Therefore, the IDS infomodel introduces a concise set of message types specifying metadata fields that must/should/can be given in order to
facilitate the business interactions.
