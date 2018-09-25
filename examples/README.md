# Reference Examples

## Scenario
The reference examples are motivated by a scenario of observing traffic conditions at defined locations along the European highways 
for purposes of traffic control, predictive road maintenance, toll fee optimization and so on.

# Resource
A Resource is a single digital content or a coherent set of digital contents exposed at particular conditions via a defined interface. 
Types of digital content range from structured data, documents, media, software etc. Examples below illustrate the various types and 
different aspects of resources.

## Example DATA1: Free, historical data download
 
The resource example DATA1 showcases an easy, non-interactive access to historical data provided 
by the participant PART1. Monthly traffic statistics collected during a year since 2010 are exposed for download 
as individual files (“artifacts”) via the Trusted Connector CONN2.  The file names (e.g., E37_2018_01.csv) encode 
by convention the discriminating parameters, i.e. the highway (e.g., “E37”), year (e.g., “2018”), month (e.g., “01”).
The reports comprise tabular data in CSV format. The data may be used free of charge, the policy requires a credits 
citation for a commercial use. An example of a verbose ([DATA1a](DATA1a.ttl)) and a more streamlined modelling 
([DATA1b](DATA1b.ttl)) of repetitive artifacts is given.   

## Example DATA2: On-line, commercial data query

Example DATA2 introduces interactive features allowing the consumer to introspect and accordingly operate services 
providing access to complex and/or dynamic resources of the Connector CONN2. In order to start exploring, the Data 
Consumer may request the value range of enumerable parameters by means of meta-queries (e.g. highway identifiers available)
and selectively retrieve content beyond the boundaries of server-defined contents in example DATA1 (e.g. statistics for a 
highway section across several years). Depending on consumer’s request behavior, various payment models may be applied 
(pay-per-use, volume or time-based subscription, etc.). The usage policies of this sample prohibit resale of the commercial 
data parts. 

## Example DATA3: Preprocessed, live data subscription

While data exchange in the previous examples was driven by the Data Consumer (pull-pattern), example DATA3 showcases a pro-active 
delivery serving the Data Consumer with content on the basis of a previously made subscription (push-pattern). An appropriate 
communication protocol (MQTT) is selected to convey the notifications. In the context of the traffic monitoring scenario, a Data Consumer 
subscribes to traffic parameters, which live values match a particular complex event pattern (CEP) deployed on Data Provider in form 
of the APP3, supplied as annex to the subscription contract. 

## Example MEDIA1: Media content

Augmenting the above mentioned resource offerings of structured data this example illustrates the provision of media content. 
Anonymized images of a surveillance camera observing traffic hot spots are updated on a minute base and made available for download 
for monitoring purpose only.

## Example APP1: Data App for content integration (system adapter)

The photographs taken by the surveillance camera in example MEDIA1 are injected into the Connector environment CONN1 by means of 
the Data App APP1 serving as a technology adapter. It implements a camera driver that accesses the raw digital content and exposes 
still images in various representations via a defined interface. 

## Example APP2: Data App for image anonymization

The image content provided by APP1 have to be anonymized prior to being forwarded to a Data Consumer. The Data App APP2 
accepts images of standard traffic scenarios in various file formats (e.g. PNG, JPG) recorded in compliance with the international 
norm EN 50132-7. It is trained to locate particular personal information (e.g., the license plate of a car) and to apply image 
processing techniques to irreversibly obfuscate this information. The Data App is likewise deployed within the Mobile Connector CONN1, 
at the source of image recording, in order to prevent the disclosure of unprocessed content. 

## Example APP3: Data App Plugin for advanced image processing

There are scenarios that impose advanced privacy constraints and require a plugin to augment the aforementioned example APP2 with a 
capability of advanced image processing, e.g., face anonymization. The plugin depends on a particular version (range) of the host Data App 
which governs its integration, configuration and life-cycle. 

## Example APP4: Data App Asset as interpreted CEP rule

The Data Consumer in the traffic scenario might define complex event processing (CEP) rules as part of a data subscription in order 
to shift the task of processing and monitoring live data at the edge of the network (edge computing). One such rule may request a notification 
sent every time the average speed in a critical area dropped below 10 km/h within the last 5 minutes (risk of congestion). The content of the 
notification message, the communication protocol (MQTT), the quality of the service parameters  (at-least-once delivery), and other details are 
defined by the rule as part of the subscription.

# Infrastructure components

## Example CONN1: Mobile, base connector

Connectors are the central building blocks, the edge nodes of the IDS network. The example Connector CONN1 is deployed on a mobile sensor platform 
located close to a traffic hot spot. It hosts a data processing pipeline where image data received form APP1 is fed into APP2, optionally cached 
and exposed as example resource MEDIA1.

## Example CONN2: Trusted connector

The Trusted Connector CONN2 represents a hardened version of the Connector runtime, a certified platform for data integration, processing and publishing 
maintained by the participant PART1 as part of its data provisioning infrastructure.  
       
## Example INFRA1: Logistics broker

Because of the vast amount of resources a dedicated Broker for the "logistics domain" is operated by the service provider PART2. Next to a customer-oriented 
GUI the data registry exposes a series of service interfaces (APIs) for lif-cycle management (publication,updated, removal) and search of content offerings.  

## Example INFRA2: General purpose AppStore

The example AppStore INFRA2 maintains metadata and software resources across IDS communities and providers. The software company PART2 advertises and distributes 
its Data Apps (e.g. APP2) via that registry.   

# Participants

## Example PART1: European traffic data provider

The hypothetical "Highway monitoring and statistics agency" acts as a data provider. It maintains a large-scale infrastructure for monitoring, 
analysis and prediction of highway utilization statistics in European context. The agency has deployed a range of mobile connectors (e.g. CONN1) 
for distributed collection and publication of geo-tagged, regional sensor data, likewise a secure connector (CONN2) for sharing valuable statistics 
reports and predictions.
  

## Example PART2:
 
App4Traffic GmbH provides a wide range of software development, consultancy and data hosting services and thus implements multiple roles 
within the IDS ecosystem. Based in Switzerland (Musterstraße 2, Zürich) the SME develops and distributes IDS Data Apps (e.g. APP1) and serves 
customers like PAT3 with advanced analytics services based upon data from PART1.   

## Example PAT3: Global logistics company

The international "Supercargo Logistics" company provides services around the globe with subsidiaries in a number of countries, among others 
Supercargo GmbH (Musterstraße 5, Köln, Deutschland), Supercargo LLC (Yлица пример 120, Moscow), and Supercargo Ltd. (Sample Road 15c, Hongkong).
Their businesses are thus subject to international, national and optionally some custom regulations (legal areas). The organization complies 
with the ISIC classification rev. 4 and has ISIC code 4923 (freight transport via road). The company retrieves live traffic monitoring data, 
in order to supply its drivers with up-to-date traffic information, efficient routing and timely hazard warnings. 

# Interactions

In the following examples of business interactions among participants are given. The realization of the core IDS value propositions 
(secure data transfer between standardized components while ensuring data sovereignty) is supported by interactions (e.g. data transfer) 
annotated with metadata (instances of the Message class in the header part). Metadata descriptions of content being exchanged are mandatory. 
Therefore, the IDS infomodel introduces a concise set of message types specifying metadata fields that must/should/can be set in order to 
facilitate the business interactions. 

## Example INTER1: Catalog publication in Broker



## Example INTER2: Broker search and content identification

## Example INTER3: Contract negotiation of the Resource(s) selected  

## Example INTER4: Content retrieval

