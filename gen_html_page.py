#!/usr/bin/python

import os
import sys
import json
from t30 import t30

def usage(err):
	out = sys.stdout
	if err:
		out = sys.stderr
	out.write(err + "\n")
	out.write("""
Usage: %(app)s wav_file html_file
Ex:    %(app)s b9c76087-3887-45ef-97fd-14cc556128ed.wav fax_comm_decoding.html
""" % {"app": sys.argv[0]})


if len(sys.argv) != 3:
	usage("Invalid number of arguments")
	sys.exit(1)


app, wav_file, html_file = sys.argv


cmd = "./gen_flow.sh " + wav_file + " temp/flow.txt"


res = os.system(cmd)

if res != 0:
	sys.stderr.write("Command '" + cmd + "' failed with " + str(res))
	sys.exit(1)

cmd = "./flow2json.py temp/flow.txt > temp/temp.json"

res = os.system(cmd)

if res != 0:
	sys.stderr.write("Command '" + cmd + "' failed with " + str(res))
	sys.exit(1)


fin = open("temp/temp.json")

s = ''.join(fin.readlines())
data = json.loads(s)

for item in data:
    item['expanded'] = False
    if item['aggregation'] == "0":
        item['bColor'] = '#4cd3c2'
    else:
        item['bColor'] = '#d1eaa3'

    if item['type'] == 'MESSAGE':
        msg = item['event']
        info = t30[msg] if t30.has_key(msg) else {'meaning': '', 'details': ''}

        item['event'] = item['event'] + " (" + info['meaning'] + ")"
        item['body'] = "MESSAGE " + msg + " (" + info['meaning'] + "): " + info['details'] + "\n\nParse:\n" + item['details'].replace("%0a", "\n") + "\n\nRaw Bytes:" + item['bytes']
        del item['bytes']
        del item['details']
    elif item['type'] == 'TONE':
        msg = item['event']
        info = t30[msg] if t30.has_key(msg) else {'meaning': '', 'details': ''}

        item['event'] = item['event'] + " (" + info['meaning'] + ")"
        item['body'] = "TONE " + msg + " (" + info['meaning'] + "): " "\n" + info['details'].replace("%0a", "\n")
        del item['bytes']
        del item['details']
    elif item['type'] == 'STATS':
        item['body'] = "STATS: " "\n" + item['bytes'].replace("%0a", "\n") # actually the info should be in the item['details'] instead of item['bytes']
        del item['bytes']
        del item['details']

lines = open('fax_comm_decoding.html.template').readlines()
template = ''.join(lines)

wf = wav_file.split("/")[-1]

html = template.replace("__WAV_FILE_NAME__", wf).replace("__ITEMS__", json.dumps(data))

fout = open(html_file, "w")
fout.write(html)
fout.close()
print(html_file + " successfully created")


