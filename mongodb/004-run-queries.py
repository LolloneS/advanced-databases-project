#!/usr/bin/env python3


from subprocess import call
import os
import time


DB_NAME = 'global_trades_csv'

if __name__ == '__main__':
    folder, _ = os.path.split(__file__)
    queries_folder = os.path.realpath(folder + '/../queries')
    queries = os.listdir(queries_folder)
    queries.sort()
    i = 1
    for filename in queries:
        if 'mongo' in filename:
            print("Running script number " + str(i))
            params = ['mongo', DB_NAME, queries_folder + '/' + filename]
            call(params)
            i += 1
