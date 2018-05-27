#!/usr/bin/env python3

from pymongo import MongoClient
from subprocess import call
import json, csv, itertools, os, importlib, datetime
from os.path import dirname, abspath, join
from os import listdir
from time import time
from misc.write_result import write_result

def run_everything():
    client = MongoClient('localhost', 27017)
    global_names = json.load(open("globals.json"))
    write_result(datetime.datetime.now().strftime("%Y-%m-%d, %H-%M-%S"), "w")
    structure_dirs = {
        "EMBEDDED STRUCTURE" : "mongodb-embedded",
        "REFERENCE STRUCTURE" : "mongodb-reference"
    }

    for k, v in structure_dirs.items():
        write_result(k)
        scripts_folder = join(dirname(abspath(__file__)), v)
        scripts = listdir(scripts_folder)
        scripts.sort()
        for filename in scripts:
            if ".py" in filename:
                params = ['python', join(scripts_folder, filename)]
                write_result("Calling " + ' '.join(params))
                call(params)
        write_result("\n\n")
        

if __name__ == "__main__":
    run_everything()