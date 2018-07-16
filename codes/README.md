# Codes

Collection of *code lists* and taxonomies of values, instances of classes defined within "model" directory.

## Resources
- [Codelist based on ISO 19115-1:2014](https://github.com/ISO-TC211/GOM/tree/master/isotc211_GOM_harmonizedOntology/19115-1/2014/codes)
- [Guidelines for the creation and Management of SDMX Code Lists](https://sdmx.org/wp-content/uploads/SDMX_Guidelines_for_CDCL.docx)

# Issues/Questions/Ideas

## Mime type
- Consider adding *filename extensions* along with a MIME type, e.g. (mime.types)[https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types]
- Consider adding [*magic numbers*](https://en.wikipedia.org/wiki/File_format#Magic_number)
- Decide the right predicate for mime type string ("application/geo+json"), currently `rdfs:comment`, e.g. [`rdf:value`](https://www.w3.org/TR/rdf-schema/#ch_value)
- How is the `dct:identifier` used, what is its purpose ("APPLICATION_GEO_JSON")?
