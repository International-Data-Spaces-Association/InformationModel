# Information Model - Messaging module

- Infrastructure Components exchange data that is related to IDS operation (e.g., registration and querying of connector self-descriptions)
in a **message-driven** way

- The protocols used for exchanging these messages are
    - HTTPS or MQTT, details such as the HTTP method or MQTT topic name still need to be defined
    - IDSCP 

- Transfer of participant data (aka "payload data" provided on the IDS) may use any type of protocol and data exchange method. Two scenarios can be differentiated:
    - proprietary protocols, imposed by the participant, e.g., messaging, RPC, shared databases, etc. and is not within the control of the IDS architecture
    - IDS messages, as defined in this module 

- For exchanging payload data, regardless of the communication method, metadata needs to be attached to the payload data to, e.g.,
document source, destination, and terms of the data flow. This information is captured in the DataTransfer class.

- The technical implementation to attach DataTransfer information to the payload data depends on the data exchange method

- Therefore, DataTransfer is **not** a message in the way of, e.g., Broker registration or query messages, but is composed of fields
and properties of the Message class, which are necessary for **any** payload data flow.  

- In cases where proprietary protocols are used to transfer data, instances of DataTransfer need to be associated to the data as 
    - payload of a participant's proprietary message format
    - part of communication protocol (e.g., HTTP multipart)
    - embedded in the transfered payload data itself (e.g., image header fields)   

## List of message types by targeted infrastructure components 

"A _command_ is a message that expresses the intent to make a modification; if successful, it
results in an _event_, which is an immutable fact about the past. A _query_, on the other hand,
is a message that expresses the desire to obtain information and that may be answered
by a _result_ that describes an aspect of the domain object at the point in time when the
query was processed." (Reactive Design Patterns)

_rejections_ are responses to messages that are incorrect syntactically or content-wise. 

### General Message Structure

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

- RequestResource (contains resource id and, optionally, a contract)
- OfferResource (offers the transfer of a resource)

#### Events

- ResourceRequestAccepted

#### Queries

- GetSelfDescription

#### Results

- SelfDescription

#### Rejections

- ContractNotAccepted (contains alternative offers of contracts)
- TransferNotAuthorized