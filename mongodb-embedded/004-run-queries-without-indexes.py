#!/usr/bin/env python3

from subprocess import call
import os

DB_NAME = 'global_trades'

def run_queries():
    folder, _ = os.path.split(__file__)
    queries_folder = os.path.realpath(folder + '/../queries')
    queries = os.listdir(queries_folder)
    queries.sort()
    i = 1
    for filename in queries:
        if 'mongo-embedded' in filename:
            print("Running script number " + str(i))
            params = ['mongo', DB_NAME, queries_folder + '/' + filename]
            call(params)
            i += 1



if __name__ == '__main__':
    run_queries()