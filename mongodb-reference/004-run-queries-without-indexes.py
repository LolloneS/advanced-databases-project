#!/usr/bin/env python3

from subprocess import call
from time import time
import json
from os import listdir
from os.path import dirname, abspath, join, realpath, split



def run_queries():
    folder, _ = split(__file__)
    parent_folder = join(os.path.dirname(dirname(os.path.abspath(__file__))))
    queries_folder = realpath(join(parent_folder, 'queries'))
    global_names = json.load(open(join(parent_folder, "globals.json")))
    results = open(join(parent_folder, "results.txt"), 'a')
    results.write("Running queries using references and no indexes \n")
    queries = listdir(queries_folder)
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
    results.close()


if __name__ == '__main__':
    run_queries()