# After I upgrade to a new release,
# every widget that's under git control
# and provided by Esri has to have its .git folder 
# copied from the old version.
import os
from shutil import copyfile, copytree

ROOT="/home/gis/source/repos/WABDE/"
OLD_FOLDER="widgets-2.21"
NEW_FOLDER="widgets"

widgets = os.listdir(os.path.join(ROOT, NEW_FOLDER))
for item in sorted(widgets):
    stripped = item.strip()
    if stripped[0] == '.': continue
    new_folder = os.path.join(ROOT, NEW_FOLDER, stripped)
    old_folder = os.path.join(ROOT, OLD_FOLDER, stripped)
    if not os.path.exists(new_folder) or not os.path.isdir(new_folder):
        continue
    if os.path.exists(old_folder):
        # Note that these are submodules so they have .git files, not folders.
        for item in ['.git', 'LICENSE', 'README.md']:
            source = os.path.join(old_folder, item)
            target = os.path.join(new_folder, item)
            if os.path.exists(target):
                print("Already have %s in '%s'." % (item, new_folder))
            elif (os.path.exists(source)):
                print("Copying '%s'" % source)
                copyfile(source, target)
            else:
                print("Nothing to copy in '%s'" % old_folder)
    else:
        print("I don't see", old_folder, ' or maybe ', new_folder)

source = os.path.join(ROOT, OLD_FOLDER, '.git')
target = os.path.join(ROOT, NEW_FOLDER, '.git')
if os.path.exists(source) and os.path.isdir(source):
    if not os.path.exists(target):
        copytree(source, target)

print("All done!")