#!/bin/bash
# Add all the standard Esri widgets as submodules
#
#  Run this in the widgets/ directory
#

for i in `cat ./scripts/esri-wabde-list`
do
    git submodule add https://github.com/Wildsong/wabde-widget-$i $i
done
