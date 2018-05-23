#!/usr/bin/env python3
import importlib
from pymongo import MongoClient
from time import time

run_module = importlib.import_module('004-run-queries-without-indexes')

def create_trades_indexes():
    client = MongoClient('localhost', 27017)
    db = client["global_trades"]
    trades = db.trades
    fields_to_index = ('year', 'country_or_area', 'commodity', 'comm_code')
    for i in fields_to_index:
        start_time = time()
        print("Creating index on {}".format(i))
        trades.create_index(i)
        print("Index on {} created. Took {} seconds".format(i, (time() - start_time)))
    


if __name__ == '__main__':
    create_trades_indexes()
    run_module.run_queries()