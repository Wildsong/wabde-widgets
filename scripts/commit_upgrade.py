import os
import subprocess

# I need to do a dos2unix thing somewhere before commiting

os.chdir('widgets')
with open("scripts/esri-wabde-list", "r") as fp:
    for item in fp.readlines():
        widget = item.strip()
        if widget:
            print(widget)
            os.chdir(widget)
            subprocess.call(["git", "commit", "-m", "'Upgrade for release 2.22 oct 2021'", "-a"])
            subprocess.call(["git", "push"])
            os.chdir('..')

