#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# Import modules
import json
from logging import warning
from os import makedirs, remove
from os.path import expanduser, isdir

j_folder = expanduser('~/.config/face')
j_file = j_folder + '/settings.json'

default_js = {
  "AutoStart": "False",
  "TrayIcon": "True",
  "StartUp": "Default",
  "StatusBar": "False",
  "Opacity": 100,
  "SizeFont": "Default",
  "AutoReload": "False"
}

# Check if exist settings.json, else file as create
try:
    with open(j_file):
        pass
except Exception as msg:
    warning("\033[33m %s. \033[32mCreate a settings.json ...\033[m", msg)
    if not isdir(j_folder):
        makedirs(j_folder)
    with open(j_file, 'w') as jfile:
        json.dump(default_js, jfile, indent=2)


# Set value of the json file
def set_json(op):
    with open(j_file) as jf:
        objJson = json.load(jf)
    return objJson[op]


# Write value of the json file
def write_json(op, val):
    with open(j_file, 'r') as jf:
        objJson = json.load(jf)
        objJson[op] = val

    # Replace original file
    remove(j_file)
    with open(j_file, 'w') as jf:
        json.dump(objJson, jf, indent=2)
