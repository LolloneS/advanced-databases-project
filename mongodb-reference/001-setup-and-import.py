#!/usr/bin/env python3

from pymongo import MongoClient, errors
from subprocess import call
import json, csv, itertools
from os.path import dirname, abspath, join
from time import time

def parse_data():
    client = MongoClient('localhost', 27017)
    parent_folder = join(dirname(dirname(abspath(__file__))))
    global_names = json.load(open(join(parent_folder, "globals.json")))
    client.drop_database(global_names["DB_NAME_REF"])
    db = client[global_names["DB_NAME_REF"]]
    trades_ref = db[global_names["COLLECTION_NAME_REF_1"]]
    commodities_ref = db[global_names["COLLECTION_NAME_REF_2"]]
    dataset = join(parent_folder, "dataset/commodity_trade_statistics_data.csv")
    
    with open(dataset) as csvfile:
        trades = csv.DictReader(csvfile, delimiter=",")
        i = 0
        trades_to_insert = []
        commodities_to_insert = set()
        start_time = time()
        for row in trades:
            # sistema le commodity
            commodity = {
                "name" : row["commodity"],
                "code" : row["comm_code"],
                "category" : row["category"]
            }

            del row["commodity"]
            del row["category"]

            commodities_to_insert.add(tuple(commodity.items()))

            # sistema i trade details    
            trade_details = {}
            if row["flow"]:
                trade_details["flow"] = row["flow"]
            if row["weight_kg"] != '':
                trade_details["weight_kg"] = int(row["weight_kg"])
            if row["trade_usd"] != '':
                trade_details["trade_usd"] = int(row["trade_usd"])
            if row["quantity"] != '':
                trade_details["quantity"] = int(eval(row["quantity"]))
            if row["quantity_name"] != '':
                trade_details["quantity_name"] = row["quantity_name"]

            row["trade_details"] = trade_details

            del row["flow"]
            del row["weight_kg"]
            del row["trade_usd"]
            del row["quantity"]
            del row["quantity_name"]

            trades_to_insert.append(row)

            if (i == 10000):
                result = trades_ref.insert_many(trades_to_insert)
                trades_to_insert = []
                i = 0
            i += 1
        
        if len(trades_to_insert) > 0:
            trades_ref.insert_many(trades_to_insert)
            trades_to_insert = []
        
        commodities_ref.insert_many(list(dict(i) for i in list(commodities_to_insert)))

    print("Importing 8+ million rows, ~1GB dataset took %s seconds" % (time() - start_time))        


if __name__ == '__main__':
    parse_data()