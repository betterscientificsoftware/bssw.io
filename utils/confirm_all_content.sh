#!/bin/sh

# Make sure we're in the right place in the repo
if ! [ -d Articles -a -d CuratedContent -a -d utils ]; then
    echo "WARNING: You are not running from top of repo"
fi

# Get path to command that invoked this script and use that
# to specify path to confirm_content.sh script
dir=$(dirname $0)

# The sed and tr commands preceding xargs is to ensure we don't attempt
# to pass poorly formmatted strings through xargs. The sed removes extra
# spaces at end of line and the tr removes single quote chars.
find . -name utils -prune -o -name '*.md' -exec grep -q -i 'Publish: Yes' {} \; -exec grep -m 1 '^# ' {} \; | cut -d' ' -f2- | sed -e 's/ *$//' | tr "'" "-" | xargs -L 1 $dir/confirm_content.sh
