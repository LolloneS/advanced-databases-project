#!/usr/bin/env python3
import importlib, os, json
from pymongo import MongoClient
from time import time
from os.path import dirname, abspath

run_module = importlib.import_module('004-run-queries-without-indexes')

def create_trades_indexes():
    client = MongoClient('localhost', 27017)
    parent_folder = os.path.join(dirname(dirname(abspath(__file__))))
    global_names = json.load(open(os.path.join(parent_folder, "globals.json")))
    results = open(join(parent_folder, "results.txt"), 'a')
    results.write("Running queries using references and indexes \n")
    db = client[global_names["DB_NAME_REF"]]
    trades_ref = db[global_names["COLLECTION_NAME_REF_1"]]
    commodities_ref = db[global_names["COLLECTION_NAME_REF_2"]]
    fields_to_index = {
        trades_ref : ['year', 'country_or_area'],
        commodities_ref : ['name', 'code']
    }
    for k, v in fields_to_index:
        for j in v:
            start_time = time()
            results.write("Creating index on {}".format(j))
            k.create_index(i)
            results.write("Index on {} created. Took {} seconds".format(i, (time() - start_time)))
    

if __name__ == '__main__':
    create_trades_indexes()
    run_module.run_queries()