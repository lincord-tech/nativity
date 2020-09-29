from flask import Flask
from flask_restful import Api, Resource, abort
from app.tst import TST
from app.dict_json_reader_class import Dict_json_reader

app = Flask(__name__)


#ternary trie form json
tst = TST()
sourse = 'app/dict_full_no_sub_Str.json'

#read a dict from json as {}
dict_reader = Dict_json_reader(sourse)
dictionary = dict_reader.get()

for word in dictionary:
    tst.put(word, dictionary[word])

@app.route('/<word>')
def show_values(word):
  return tst.get(word)



# def abort_if_dict_id_doesnt_exist(dict_id):
#     if tst.get(dict_id) == -1:
#         abort(404, message="not found".format(dict_id))


# class Dict(Resource):
#     def get(self, dict_id):
#         abort_if_dict_id_doesnt_exist(dict_id)
#         return tst.get(dict_id)


# api.add_resource(Dict, '/<dict_id>')
