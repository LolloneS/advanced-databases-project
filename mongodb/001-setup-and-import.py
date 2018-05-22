#!/usr/bin/env python3


from pymongo import MongoClient
from subprocess import call
import os
import time


if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    client.drop_database("global_trades_csv")
    folder, _ = os.path.split(__file__)
    dataset = folder + "/../dataset/commodity_trade_statistics_data.csv"
    start_time = time.time()
    call(['mongoimport', '-d', 'global_trades_csv', '-c', 'countries', 
          '--drop', '--type', 'csv', '--headerline', '--file', 
          dataset])
    print("Importing 8 million rows, ~1GB dataset took %s seconds" % (time.time() - start_time))
