#!/usr/bin/env python3


from pymongo import MongoClient
from subprocess import call
import os
from time import time


def import_data():
    client = MongoClient('localhost', 27017)
    client.drop_database("global_trades")
    folder, _ = os.path.split(__file__)
    dataset = folder + "/../dataset/commodity_trade_statistics_data.csv"
    start_time = time()
    call(['mongoimport', '-d', 'global_trades', '-c', 'trades', 
          '--drop', '--type', 'csv', '--headerline', '--file', 
          dataset])
    print("Importing 8 million rows, ~1GB dataset took %s seconds" % (time() - start_time))



if __name__ == '__main__':
    import_data()