#!/usr/bin/env python3
import os
import re
import array
import jsonpickle
import json
from app.dict_json_reader_class import Dict_json_reader
from app.tst import TST

# if __name__ == "__main__":

#     tst = TST()

#     tst.put("apple", 100)
#     tst.put("orange", 200)

#     print(tst.get("orange"))

#sourse = '/home/d/pikkaConstilation/dict_full_no_sub_Str.json'

# #read a dict from json as {}
# dict_reader = Dict_json_reader(sourse)

# dictionary = dict_reader.get()

# for word in dictionary:
# 	tst.put(word, dictionary[word])

# print(tst.get('for'))

#
# try to write a dict from json and then in order to safe RAM
# put data in two arrays
# then read both of them to build a trie

# try it with gzip as well. but just for fun if there ll be some free time
