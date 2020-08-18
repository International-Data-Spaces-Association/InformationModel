#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

grep -v '^#' "$SCRIPTPATH/../docs/serializations/ontology.nt" | # no comment lines
    awk '{print $1; print $2; print $3}'                      | # print subject, predicate and object
    sed -n '/^<http/ { s/\([#\/]\)[^#\/]*>/\1>/; p}'          | # strip localnames, keep namespace URIs
    sort                                                      | # sort (by namespace URI)
    uniq -c                                                   | # count occurrences
    sort -k1 -r                                                 # sort by descending number of occurrences
