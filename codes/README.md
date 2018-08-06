# Codes

Collection of *code lists* and taxonomies of values, instances of classes defined within "model" directory.

## Resources
- [Codelist based on ISO 19115-1:2014](https://github.com/ISO-TC211/GOM/tree/master/isotc211_GOM_harmonizedOntology/19115-1/2014/codes)
- [Guidelines for the creation and Management of SDMX Code Lists](https://sdmx.org/wp-content/uploads/SDMX_Guidelines_for_CDCL.docx)

# Issues/Questions/Ideas

## General (process)
- Define the process to suggest, agree upon and circulate new values (of existing schemes) / creation of new schemes
- Make the text normalization rules explicit and apply them consistently
    - any non-alphanumeric character is replaced by underscore, e.g. "/" -> "_"
    - lowercase characters are translated to upper case in identifier
    - local URI name is all lowercase (?)

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
- Inconsistent license URIs (idsc_lic:license_cc_by_nc_nd_2_0 <-> idsc_lic:Creative_Commons_Attribution_No_Derivs_International_CC_BYND_4_0)
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
- Compare/align with annotations present here:
    - https://www.europeandataportal.eu/en/content/show-license
    - https://www.europeandataportal.eu/data/api/action/license_list
- Listing of licenses used in Eu Data Portal (by query):

```
    CC01.0
    CC-BY4.0
    CC-BY-ND4.0
    CC-PDM1.0
    DL-DE-BY1.0
    DL-DE-BY2.0
    DL-DE-BY-NC1.0
    DL-DE-ZERO2.0
    FR-LO
    GFDL-1.3
    ODC-BY
    ODC-ODbL
    OGL2.0
    PSEUL
``` 

## Media type
- Currently only IANA types - evaluate alternative registries/sources
- Add/change predicate for the established mime type identifier, currently comment: "text/plain"
- Add reference to definitions (IANA), e.g. https://www.iana.org/assignments/media-types/text/csv
- Consider adding *filename extensions* along with a MIME type, e.g. (mime.types)[https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types]
- Consider adding [*magic numbers*](https://en.wikipedia.org/wiki/File_format#Magic_number)
- File is missing redable annotations: label, description (comment), reference
- Focus on "popular", [recommended](https://www.europeandataportal.eu/elearning/en/module9/#/id/co-01) formats
- Proposal:

```
    idsc_media:text_csv a ids:IANAMediaType ;
	rdfs:label "text/csv" ; # use the well-known, registered Media Type as label
    dct:identifier "TEXT_CSV" ; # literal identifier -> Enum value
    rdfs:comment "Comma separated values format for exchanging and converting data between various spreadsheet programs."@en ;
    rdfs:isDefinedBy <https://www.iana.org/assignments/media-types/text/csv> ;# IANA registration page, missing for some mime types
    rdfs:seeAlso <https://tools.ietf.org/html/rfc4180> .# "informative" RFC, optional because often unknown or non existent
```
- Make the translation rules into Java explicit:
    - NS bound to prefix is turned into a java Enum package according to Java convention, e.g. org.w3id.ids.code.media
    - Class name of the instance becomes the Enum type: IANAMediaType
    - Local instance name ist the capitalized local name (i.e. same as identifer) : TEXT_CSV
    - complete example:
    
```
    package org.w3id.ids.code.media
    public enum IANAMediaType {
        /** text/csv */
        TEXT_CSV("https://w3id.org/ids/code/media/text_csv")
    }

```
    
