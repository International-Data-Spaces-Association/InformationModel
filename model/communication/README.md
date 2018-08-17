# Information Model - Communication module
- implemenation of an Interface w.r.t. a particular communication protocol

## Establishing Data Exchange

### Enable Authenticated Communication

At first, a secure, encrypted communication channel must be established that ensures authentication of the communication partners. IDSCP
suggests the following workflow:

![Enable Authenticated Communication](../../images/establish_authenticated_connection.png)

However, authenticated channels may also be established by using TLS in combination with, e.g., HTTP. In that case the above workflow
will take place implictly when requesting the access token (without presenting the dynamic attribute token, see next section).

### Ensure Authorized Access  

Based on an authenticated connection,  consumers need to request an access token in order to authorize for resource usage. The actual
method that must called to retrieve the token (step 1a) is stated in the connector's self description.

![Enable Authenticated Communication](../../images/establish_authorized_connection.png)

## Resource Usage

In order to use (download, query,...) a resource, consumers invoke a certain operation (as retrieved from the set of possible
operations from the connector's self description). Invoking the operation is done by creating a request as stated in the connector's
self description. That request depends on the provider's connector configuration and may be a http call, mqtt publication, a certain 
message type or others.  

![Resource Usage](../../images/resource_usage.png)

Prior to invoke an operation to a resource, a contract for using the resource can be optionally negotiated. This is inititated by issuing
a ContractOffer message (defined in the IDS information model) to the resource provider's messaging endpoint. A workflow of a successful
contract agreement is depicted below.

![Contract Negotiation](../../images/contract_negotiation.png)

## Broker Interaction

Information exchange with Broker instances is defined by a set of messages (see Section "Messages" below). Basis of each interaction is 
an established authorized connection, i.e. an access token is attached to each message. The case of registering a connector at a Broker 
with the means of a RegisterConnector message is depicted below.

![Contract Negotiation](../../images/broker_interaction.png)

## Messages

Certain infrastructure-relevant communication (such as, e.g, connector registration at brokers) is implemented by exchanging messages
of defined content. This section lists the specified messages and the type infrastructure components that must be able to accept and
interpret them.  

## List of message types by targeted infrastructure components 

"A _command_ is a message that expresses the intent to make a modification; if successful, it
results in an _event_, which is an immutable fact about the past. A _query_, on the other hand,
is a message that expresses the desire to obtain information and that may be answered
by a _result_ that describes an aspect of the domain object at the point in time when the
query was processed." (Reactive Design Patterns)

_rejections_ are responses to messages that are incorrect syntactically or content-wise. 

### General Message Structure

Each message is required to contain the following information (see the Information Model sources for further specification):
* String : modelVersion
* ??? issuingConnector -> @jaro: the ttl says the domain is ConnecotrIdentifier. Why can't this be URL?
* DateTime : issued

### General Messages
* RequestAccessToken

### Broker

This section names the message types that **must** be processed by any Broker implementation in order to be IDS compliant.

#### Connector Management Command

These messages deal with announcing information about IDS Connectors to the Broker. On message reception, the Broker **must** 
reply either with an Event or a Rejection Message. The rejection message references the command message by the correlation
id property. 

##### RegisterConnector
mandatory properties:
* String : connector self description 
OR
* URL : unique identifier of the connector 

##### UpdateConnector
mandatory properties: same as for RegisterConnector

##### UnregisterConnector
mandatory properties:
* URL : unique identifier of the connector

##### EnableConnector
mandatory properties: same as for UnregisterConnector

##### DisableConnector
mandatory properties: same as for UnregisterConnector

#### Events

For each Command message a corresponding Event message exists that is sent as a reply to the command. Their correlation 
id attribute must be set in order to reference the command message that caused the event. 

##### ConnectorRegistered, ConnectorUnregistered, ConnectorUpdated,...
mandatory properties:
* URL : correlation id (command message identifier)
* URL : connector 

#### Queries 

- GetWholeCatalog
- GetConnectorData
- QueryCatalog

#### Results

- CatalogResult

#### Rejections

- InvalidMessageFormat (e.g., signature missing, mandatory properties not included)
- NotAuthorized
- AuthorizationFailed
- TemporarilyUnavailable

### Connector

#### Resource Access Commands

When resources (e.g., Data Assets) are offered by the Connector 

- RequestResource (contains resource id)
- OfferResource (offers the transfer of a resource)

#### Contract Negotiation

- ContractOfferMessage
mandatory properties:
* URL : requested resource identifier
* String : offered contract (according to the infomodel, i.e., currently based on ODRL) 

#### Events

- ResourceRequestAccepted
mandatory properties:
* URL : resource identifier
* String : offered resource description (according to the infomodel) 

- ContractAgreement
mandatory properties:
* URL : identifier for which the contract has been negotiated
* String : description of the contract according to the infomodel

#### Queries

- GetSelfDescription
mandatory properties: none

- ContractRequestMessage
mandatory properties:
* URL : resource identifier for which the contract should be requested

#### Results

- SelfDescription
mandatory properties:
* String : self description according to infomodel

#### Rejections

- ContractNotAccepted (contains alternative offers of contracts)
optional properties:
List<String> : alternative contracts according to infomodel, each identified with an own (local) URL

- MalformedContract (contract misses information or is not compliant to a certain schema)
- TransferNotAuthorized

# Resources
- [DCAT GitHub-Wiki: Cataloguing data services](https://github.com/w3c/dxwg/wiki/Cataloguing-data-services)

