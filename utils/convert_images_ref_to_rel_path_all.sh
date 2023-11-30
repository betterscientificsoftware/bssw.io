#!/bin/bash
#
# Run as:
#
#   cd bssw.io/
#   ./utils/convert_images_ref_to_rel_path_all.sh
#
# to update the images refs to relative paths in this repo for all of *.md
# files the bssw.io repo.
#

find Articles CuratedContent Events Site -name "*.md" \
  -exec ./utils/convert_images_ref_to_rel_path.py {} \;

# NOTE: We don't want to replace any paths in the bssw.io/docs/ directory
# because those are for a github pages site and if they reference any images,
# those will point into bssw.io/docs/images/ and **not** into bssw.io/images/!
