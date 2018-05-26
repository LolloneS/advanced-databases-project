from pymongo import MongoClient
from subprocess import call
import json, csv, itertools, os
from os.path import dirname, abspath, join
from time import time

def run_everything():
    client = MongoClient('localhost', 27017)
    global_names = json.load(open("globals.json"))
    results = open("results.txt", 'w')
    results.write("Running the whole pipeline \n")
    
    # Embedded structure
    results.write("EMBEDDED STRUCTURE\n")
    results.close()
    scripts_folder = join(dirname(abspath(__file__)), "mongodb-embedded")
    scripts = os.listdir(scripts_folder)
    scripts.sort()
    for filename in scripts:
        if filename[0] == '0':
            params = ['python', join(scripts_folder, filename)]
            print("Calling " + ' '.join(params))
            call(params, shell=True)

    # Reference structure
    results = open("results.txt", 'a')
    results.write("REFERENCE STRUCTURE\n")
    results.close()
    scripts_folder = join(dirname(abspath(__file__)), "mongodb-reference")
    scripts = os.listdir(scripts_folder)
    scripts.sort()
    for filename in scripts:
        if filename[0] == '0':
            params = ['python', join(scripts_folder, filename)]
            print("Calling " + ' '.join(params))
            call(params, shell=True)    
    

if __name__ == "__main__":
    run_everything()