#!/usr/bin/env python3
from subprocess import call
import os
import time

DB_NAME = 'global_trades_csv'


if __name__ == '__main__':
    folder, _ = os.path.split(__file__)
    i = 1
    queries_folder = os.path.realpath(folder + '/../queries')
    for filename in os.listdir(queries_folder):
        if 'mongo' in filename:
            print("Running script number " + str(i))
            params = ['mongo', DB_NAME, queries_folder + '/' + filename]
            call(params)
            i += 1
