#!/usr/bin/python

import json
import sys
from t30 import t30


def usage(err):
    app = sys.argv[0]

    out = sys.stderr
    if(err):
        out = sys.stderr
    out.write("""
Usage: %s flow_file
Ex:    %s flow.txt
""" % (app, app))


def convert(filename):
    data = []
    f = open(filename)
    for line in f.readlines():
        tokens = line.split(";",5)
        if len(tokens) < 6:
            print(tokens)
            tokens = tokens + ['' for i in range(6 - len(tokens))]
        item = {
            'time': tokens[0],
            'type': tokens[1],
            'aggregation': tokens[2],
            'event': tokens[3],
            'bytes': tokens[4],
            'details': tokens[5],
        }

        data.append(item)

    print(json.dumps(data))




if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage("Invalid number of arguments")
        sys.exit(1)
    convert(sys.argv[1]) 
