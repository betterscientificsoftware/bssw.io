#!/bin/bash
# Run in CuratedContent/ directory to extract the unique list of tags used

grep -h -i tags: *.md | \
    sed 's/^\ *Tags: //' | \
    grep -v "^\[" | \
    grep -v -i "^specify" | \
    sed 's/, /\n/g' | \
    sort | \
    uniq
