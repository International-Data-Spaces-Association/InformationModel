

# Questions/issues to discuss

- There is no equivalent of `dcat:Catalog` as a single point of metadata exploration.
  "Connector" as a generic runtime does not seem appropriate match. Such a Catalog
  node might link to advertisements, participants, connectors etc.

- There is no equivalent to `dcat:CatalogRecord` for IDS Resources to indicate e.g.
  when (issued, modified), by whom (contact) the advertisement (offer or request)
  was published. Resources listed in a catalog are implicitly offerings, there is
  no way to supply a request/specify demand for a resource. How do updates of data
  description relate to corresponding catalog record?

## Model / general properties

- Consider versioning properties, e.g. `dcterms:date` 
- Consider versioning predicates,  e.g. `adms:prev, adms:next, adms:last, dcterms:isReplacedBy`
- Consider annotation properties, e.g. `dcterms:abstract, dcterms:description`

## Identification
- What are the entities to be permanently and uniformally identified, e.g. their PID
  must be immutable and constant across catalogs? Examples: Participant, Connector.

    
