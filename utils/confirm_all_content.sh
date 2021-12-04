#!/bin/sh

# Make sure we're in the right place in the repo
if ! [ -d Articles -a -d CuratedContent -a -d utils ]; then
    echo "WARNING: You are not running from top of repo"
fi

dir=$(dirname $0)
find . -name utils -prune -o -name '*.md' -exec grep -q -i 'Publish: Yes' {} \; -exec grep -m 1 '^# ' {} \; | cut -d' ' -f2- | sed -e 's/ *$//' | tr "'" "-" | xargs -L 1 $dir/confirm_content.sh
