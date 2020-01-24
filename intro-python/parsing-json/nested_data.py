#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_cont = json.load(file)


# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
#for content in json_cont["ietf-interfaces:interfaces"]["interface"]:
#    print(content["name"])

for content in json_cont["ietf-interfaces:interfaces"]["interface"]:
    for eyy in content["ietf-ip:ipv4"]["address"]:
        print(content.get("name"), eyy.get("ip"), eyy.get("netmask"))

