import json

file = "manifest.json"
try:
    with open(file, 'r') as fp:
        j = fp.read()
        manifest = json.loads(j)
    print(manifest['description'])
except:
    print("")

