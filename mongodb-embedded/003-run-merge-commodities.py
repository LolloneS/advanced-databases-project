#!/usr/bin/env python3

from subprocess import call
import os, json

def run_queries():
    folder, _ = os.path.split(__file__)
    queries_folder = os.path.realpath(folder + '/../queries')
    queries = os.listdir(queries_folder)
    queries.sort()
    global_names = json.load(open(os.path.join(folder, "globals.json")))
    params = ['mongo', global_names["DB_NAME"], "002-merge-commodities.js"]
    call(params)
    

if __name__ == '__main__':
    run_queries()