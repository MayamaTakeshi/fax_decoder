#!/usr/bin/python

import json
import sys
from t30 import t30


def usage(err):
    out = sys.stderr
    if(err):
        out = sys.stderr
    out.write("""
Usage: flow_file
Ex:    flow.txt
""")


def convert(filename):
    data = []
    f = open(filename)
    for line in f.readlines():
        tokens = line.split(";") 
        time = tokens[0]
        item_type = tokens[1]
        col = tokens[2]
        subject = tokens[3]

        item = {
            'time': time,
            'col': col,
            'head': item_type + " " + subject,
            'bColor': '#4cd3c2' if col == '0' else '#d1eaa3',
            'expanded': False,
            'body': 'NO DETAILS',
        }

        if item_type == 'MESSAGE':
            raw_bytes = tokens[4]
            details = tokens[5]
            info = t30[subject] if t30.has_key(subject) else {'meaning': '', 'details': ''}

            item['head'] = item['head'] + " (" + info['meaning'] + ")"
            item['body'] = "MESSAGE " + subject + " (" + info['meaning'] + "): " + info['details'] + "\n\nParse:\n" + details.replace("%0a", "\n") + "\n\nRaw Bytes:" + raw_bytes
        data.append(item)

    print json.dumps(data)




if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage("Invalid number of arguments")
        sys.exit(1)
    convert(sys.argv[1]) 
