#!/bin/bash

# gh docs  https://cli.github.com/

for i in `cat esri-wabde-list`
do
  cd $i

  git init
  git checkout -b main
  git branch -d master
  git add .
  git commit -m initial\ commit -a

  # "when the current directory is a git repo, the new repo will be added as the origin..."
  # This allows me to have the name of the repo be different than the name of the CWD.
  gh repo create Wildsong/wabde-widget-$i --confirm --public
  git remote -v

  git push --set-upstream origin main

  VERSION=`python ../get_version.py`
  if [ "$VERSION" == "" ]; then
      echo WARNING!!!!! $i has no manifest.json version set. No tag created.
  else
      git tag -a $VERSION -m "Imported from Esri version $VERSION."
      git push origin $VERSION
  fi
  
  cd ..
done
  
