# Collection of command-line utilities and scripts

## Snippets
- List declared namespace-prefixes (including empty ones)
    - `grep -rh --include "*.ttl" "@prefix"  | sed -E 's/@prefix\s+(\w*):.*/\1/' | sort | uniq`
- List declared namespaces
    - `grep -rh --include "*.ttl" "@prefix"  | sed -E 's/[^<]+<([^>]+)>.*/\1/' | sort | uniq`
- List resource QNames form the IDS namespace (i.e. ids, idsm, idsv, idsc_media etc.)
    - `grep -rEho --include "*.ttl" "ids(\w*):\w+" | sort | uniq`
- Generate list of model files for import purposes within a static ontology file, considering the code lists (`codes`), concept definitions (`model, metamodel`) and concept taxonomies (`taxonomies`) except related 3rd party `references` (to be executed in $INFO_MODEL_ROOT). 
    - `find . ! -path "*/references/*" -and \( -path "*/codes/**.ttl" -or -path "*/model/**.ttl" -or -path "*/metamodel/**.ttl" -or -path "*/taxonomies/**.ttl" \) | sort | sed -r 's/^\.\/(.*)/<\1>,/'`




