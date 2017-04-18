#!/usr/bin/python3

import json
import sys
import subprocess

def usage():
    print ("\nUSAGE: python release.py <version>")
    sys.exit()

if len(sys.argv) <= 1:
    usage()
else:
    v = sys.argv[1]

if v == '--help' or v == '-h':
    usage()

with open("package.json") as jsonFile:
    data = json.load(jsonFile)

oldVersion = data["version"]
data["version"] = v

with open("package.json", "w") as jsonFile:
    jsonFile.write(json.dumps(data, sort_keys=False, indent=2))

with open("VERSION", "w") as versionFile:
    versionFile.write(v)

subprocess.call('git commit -am "Release: v{version}"'.format(version=v), shell=True)
subprocess.call('git tag -a {version} -m "New version: {version}"'.format(version=v), shell=True)
subprocess.call('git push origin master --follow-tags', shell=True)
