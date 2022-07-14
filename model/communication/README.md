# Communication Module

Elements of the *Communication* module allow for describing (non)interactive exchange of digital content and interactions with processing logic (Data Apps). The `Endpoint` represents an individual point of content exchange. It is defined in terms of underlying communication protocol by its `Host` and a unique `path` within the address space of the `Host`. In the most simple case there is a static `Endpoint` exposed by a `Resource` that points to a content `Artifact` making it available for download. <div align="center"><img alt="Concerns hexagon" src="../../images/Endpoint_Artifact.jpg" width="60%" /></div>

Interactive communication depend on client input in order to generate the content. `Operations`(s) are the basic interaction primitives (atomic services). `Parameter`(s) are named slots defined by an `Operation` in order to communicate the client *input*, server *output* or a *fault*. The `Message Exchange Pattern`(MEP) of the `Operation` governs the order and cardinality of `Parameter` supply (e.g. `ROBUST_IN_ONLY`). Related `Operation`s are grouped into `Interface`s. `Resource`s define `Interface`s in order to make the interactions involved in content exchange explicit and perceivable by the client in an abstract, protocol-agnostic way. <div align="center"><img alt="Concerns hexagon" src="../../images/Interface_Model.jpg" height="500px" /></div>

`Message`s are a means to invoke `Operation`s (`InvokeOperationMessage`) or mediate content (`ArtifactRequest`) in an abstract, protocol-agnostic way comparable to SOAP-based communication. They are delivered to and handled by default, conventional handlers of the Connector runtime.

`Operation Bindings`, on the other side, express how the `Operation` signature, i.e. the name and its parameters, map to structures of a communication protocol. This task is currently delegated to well-established API description documents (e.g. OpenAPI). A `Resource` may expose interactive `Endpoint`s that link to such bindings (optional, greyed out part).

<div align="center"><img alt="Concerns hexagon" src="../../images/InteractiveEndpoint.jpg" width="60%" /></div>
