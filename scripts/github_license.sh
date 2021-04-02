#!/bin/bash
#
# Creates a README and LICENSE file for each widget
#

for i in `cat esri-wabde-list`
do
  cd $i

  if [ -e 'README.md' ]; then
    echo
  else
    echo "# wabde-widget-$i" > README.md
    cat ../README.md >> README.md
  fi

#  DESCRIPTION=`python ../get_description.py`
#  if [ "$DESCRIPTION" == "" ]; then
#     echo $i has no description
#  elif [ "$DESCRIPTION" == $i ]; then
#     echo has a boring description
#  else
#     echo $i >> ../d
#     echo $DESCRIPTION > description
#  fi

   # Apache 2.0 license file
#  cp ../LICENSE .
#  git add README.md LICENSE
#
  git commit -m 'Added README and LICENSE files.' README.md LICENSE
  git push

  cd ..
done
