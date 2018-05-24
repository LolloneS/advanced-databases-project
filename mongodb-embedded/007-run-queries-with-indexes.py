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
    db = client[global_names["DB_NAME"]]
    trades = db.trades
    fields_to_index = ('year', 'country_or_area', 'commodity.name', 'commodity.code')
    for i in fields_to_index:
        start_time = time()
        print("Creating index on {}".format(i))
        trades.create_index(i)
        print("Index on {} created. Took {} seconds".format(i, (time() - start_time)))
    


if __name__ == '__main__':
    create_trades_indexes()
    run_module.run_queries()