#!/usr/bin/env python3

from subprocess import call
import os, json


def run_queries():
    folder, _ = os.path.split(__file__)
    parent_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    queries_folder = os.path.realpath(os.path.join(parent_folder, 'queries'))
    global_names = json.load(open(os.path.join(parent_folder, "globals.json")))
    queries = os.listdir(queries_folder)
    queries.sort()
    DB_NAME = global_names["DB_NAME"]
    i = 1
    for filename in queries:
        if 'mongo-embedded' in filename:
            print("Running script number " + str(i))
            params = ['mongo', DB_NAME, queries_folder + '/' + filename]
            call(params)
            i += 1



if __name__ == '__main__':
    run_queries()