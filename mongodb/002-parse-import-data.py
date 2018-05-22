#!/usr/bin/env python3

# Probabilmente inutile dal momento che con mongoimport ci metto un attimo e fa molto prima

'''
import csv, os, bson

# for debug purposes only 
import time
start_time = time.time()

from pymongo import MongoClient



if __name__ == "__main__":
    folder, _ = os.path.split(__file__)
    client = MongoClient('localhost', 27017)
    with open(folder + "/../dataset/commodity_trade_statistics_data.csv") as dataset:
        reader = csv.DictReader(dataset, delimiter=',', quotechar='"')
        db = client.global_trades
        collection = db["countries"]
        for row, x in zip(reader, range(700000)):
            row["commodity_name_code"] = {
                "commodity_name" : row["commodity"],
                "commodity_code" : row["comm_code"]
            }
            del row["commodity"]
            del row["comm_code"]
            
            # forse da fare nel db una volta inserito tutto?
            row["trade_usd"] = int(row["trade_usd"]) if row["trade_usd"] != '' else None
            row["weight_kg"] = int(row["weight_kg"]) if row["weight_kg"] != '' else None
            row["year"] = int(row["year"]) if row["year"] != '' else None
            if row["country_or_area"][-1] == ".":
                row["country_or_area"] = row["country_or_area"][:-1] 
            collection.insert_one(row)
            del row

    print("--- %s seconds ---" % (time.time() - start_time))
'''