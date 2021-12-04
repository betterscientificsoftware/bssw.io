#!/bin/sh

title="${@:1}"

# slugify the title (beware...unicode chars in sed -e args)
slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed -e 's@](https\{0,1\}://.*)@@g' | tr '.&' '--' | tr -d ':?();,{}+=_[]"”“@%$#<>|*!' | tr "'" "-" | tr ' /’.' '----' | sed -e 's/-–-/-/g' | sed -e 's/-—-/-/g' | sed -e 's/–/-/g' | tr -s '-' | sed -e 's/^-//' -e 's/-$//')

# attempt to find it in items, then communities, then webinars
wget --no-check-certificate -q --spider https://bssw.io/items/$slug -o /dev/null || \
wget --no-check-certificate -q --spider https://bssw.io/communities/$slug -o /dev/null || \
wget --no-check-certificate -q --spider https://bssw.io/webinars/$slug -o /dev/null || echo "$title" Not found [$slug]
