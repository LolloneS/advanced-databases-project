#!/usr/bin/env python3
import importlib, json
from pymongo import MongoClient
from time import time
from os.path import dirname, abspath, join

run_module = importlib.import_module('004-run-queries-without-indexes')

def create_trades_indexes():
    client = MongoClient('localhost', 27017)
    parent_folder = join(dirname(dirname(abspath(__file__))))
    global_names = json.load(open(join(parent_folder, "globals.json")))
    results = open(join(parent_folder, "results.txt"), 'a')
    results.write("Running queries using embedded and indexes \n")
    db = client[global_names["DB_NAME"]]
    trades = db.trades
    fields_to_index = ('year', 'country_or_area', 'commodity.name', 'commodity.code')
    for i in fields_to_index:
        start_time = time()
        results.write("Creating index on {}\n".format(i))
        trades.create_index(i)
        results.write("Index on {} created. Took {} seconds\n".format(i, (time() - start_time)))
    results.close()


if __name__ == '__main__':
    create_trades_indexes()
    run_module.run_queries()