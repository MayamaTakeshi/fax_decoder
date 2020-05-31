#!/usr/bin/python

import os
import sys
import json

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


cmd = "./gen_flow.sh " + wav_file + " flow.txt"


res = os.system(cmd)

if res != 0:
	sys.stderr("Command '" + cmd + "' failed with " + res)
	sys.exit(1)

cmd = "./flow2json.py flow.txt > temp.json"

res = os.system(cmd)

if res != 0:
	sys.stderr("Command '" + cmd + "' failed with " + res)
	sys.exit(1)


fin = open("./temp.json")

s = ''.join(fin.readlines())

lines = open('fax_comm_decoding.html.template').readlines()
template = ''.join(lines)

wf = wav_file.split("/")[-1]

html = template.replace("__WAV_FILE_NAME__", wf).replace("__ITEMS__", s)

fout = open(html_file, "w")
fout.write(html)
fout.close()
print(html_file + " successfully created")


