#!/usr/bin/env python3
import os
import re
import jsonpickle
import json


#make a dictionary form a json file
class Dict_json_reader:
    def __init__(self, path_to_file):
        self.source = path_to_file

    def get(self):
        return self.read()

    def read(self):
        with open(self.source, 'r') as file:
            decoded_dict = jsonpickle.decode(file.read(), keys=True)
            my_dict = json.loads(decoded_dict)

        return my_dict
