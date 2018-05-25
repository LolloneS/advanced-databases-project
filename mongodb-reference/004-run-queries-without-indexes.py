#!/usr/bin/env python3

from subprocess import call
from time import time
import os, json
from os.path import dirname, abspath, join



def run_queries():
    folder, _ = os.path.split(__file__)
    parent_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    queries_folder = os.path.realpath(os.path.join(parent_folder, 'queries'))
    global_names = json.load(open(os.path.join(parent_folder, "globals.json")))
    results = open(join(parent_folder, "results.txt"), 'a')
    results.write("Running queries using references and no indexes \n")
    queries = os.listdir(queries_folder)
    queries.sort()
    DB_NAME = global_names["DB_NAME_REF"]
    i = 1
    for filename in queries:
        if 'mongo-reference' in filename:
            results.write("Running script number " + str(i) + "\n")
            params = ['mongo', DB_NAME, queries_folder + '/' + filename]
            start_time = time()
            call(params)
            results.write("Took %s seconds \n" % (time() - start_time))
            i += 1


if __name__ == '__main__':
    run_queries()