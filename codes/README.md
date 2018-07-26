# Codes

Collection of *code lists* and taxonomies of values, instances of classes defined within "model" directory.

## Resources
- [Codelist based on ISO 19115-1:2014](https://github.com/ISO-TC211/GOM/tree/master/isotc211_GOM_harmonizedOntology/19115-1/2014/codes)
- [Guidelines for the creation and Management of SDMX Code Lists](https://sdmx.org/wp-content/uploads/SDMX_Guidelines_for_CDCL.docx)

# Issues/Questions/Ideas

## General (process)
- Define the process to suggest, agree upon and circulate new values (of existing schemes) / creation of new schemes

## General (model)
- Agree on URI style rules, e.g. intial or no upper-case etc. - currently inconsistent usage
- How is the `dct:identifier` used, what is its purpose ("APPLICATION_GEO_JSON")?
- Decide the right predicate for well known, established IDs (e.g. "application/geo+json"), currently `rdfs:comment`, e.g. [`rdf:value`](https://www.w3.org/TR/rdf-schema/#ch_value)?
- Define and follow a minimal annotation set (e.g. rdfs:lael sometimes missing)
- Consider adding `owl:differentFrom` annotation, at least to top-level, incompatible instances

## Category
- Defines an own skos:ConceptScheme, move to model/resource/Category
- There are custom examples from a weather/traffic domain, how are themes / categories handeld in general -> review and purge
- Consider standards like eCl@ss, ETIM, UNSPSC, proficl@ss 

## Content type
- How do the instances relate to model/resource/ContentType subclasses?
    - Subclasses or intermeidaries ("Media") are intended as domains for type-specific properties (audio/samplingRate)
    - E.g. CT (Sub)classes defined in terms of OWL axiom (owl:onProperty ids:contentType owl:hasValue idsc_content:data)?
    - Is there a 1:1 mapping instance <-> subclass?

## Hash function
- Discuss usage of capitalized local names (e.g. MD2)
- Comments/documentation (related to isage in IDS is missing) 

## Industrial classification
- Currently based on ISIC (IndustrialClassificationISIC) - how competitive/alternative classfications are used/integrated?
- Label is missing (currently as comment)
- Comment should be an explanatory text

## Language
- Augment existing standard identifiers/language codes, e.g. IETF language tag, ISO 639-1, ISO 639-2 and ISO 639-3
    
## License
- Inconsistent license URIs
- Add existing identifiers, e.g. GPLv3, LGPLv2 
- Add sources/references for the listing
- Add reference to https://tldrlegal.com/
- Evaluate and align with: https://en.wikipedia.org/wiki/Software_Package_Data_Exchange#License_syntax
- Align identifiers with: https://spdx.org/licenses/
    - see: https://spdx.org/sites/cpstandard/files/pages/files/using_spdx_license_list_short_identifiers.pdf
- Link definitions in https://github.com/spdx/license-list-data
    - linked data versions available:             https://github.com/spdx/license-list-data/tree/master/rdfturtle
    - refer to via rawgit, e.g. -  https://raw.githubusercontent.com/spdx/license-list-data/master/rdfturtle/AAL.turtle
                                            https://cdn.rawgit.com/spdx/license-list-data/8651cf2a/rdfturtle/AAL.turtle

## Mime type
- Currently only IANA types - evaluate alternative registries/sources
- Add/change predicate for the established mime type identifier, currently comment: "text/plain"
- Add reference to definitions (IANA)
- Consider adding *filename extensions* along with a MIME type, e.g. (mime.types)[https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types]
- Consider adding [*magic numbers*](https://en.wikipedia.org/wiki/File_format#Magic_number)
