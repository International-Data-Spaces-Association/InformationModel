# Collection of command-line utilities and scripts

## Snippets
- List declared namespace-prefixes (including empty ones)
    - `grep -rh --include "*.ttl" "@prefix"  | sed -E 's/@prefix\s+(\w*):.*/\1/' | sort | uniq`
- List declared namespaces
    - `grep -rh --include "*.ttl" "@prefix"  | sed -E 's/[^<]+<([^>]+)>.*/\1/' | sort | uniq`
- List resource QNames form the IDS namespace (i.e. ids, idsm, idsv, idsc_media etc.)
    - `grep -rEho --include "*.ttl" "ids(\w*):\w+" | sort | uniq`
- Generate list of included ttl files (wenn run in $INFO_MODEL_ROOT)
    - `find . -name "*.ttl" ! -name "Ontology.ttl" ! -path "*/references/*" | sort | sed -r 's/^\.\/(.*)/<\1>,/'`




