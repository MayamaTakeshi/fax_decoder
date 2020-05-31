#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

function usage() {
	cat <<EOF
Usage: $0 stereo_wav_file out_file
Ex:    $0 b9c76087-3887-45ef-97fd-14cc556128ed.wav flow.txt
EOF
}

if [[ $# -ne 2 ]]
then
	usage;
	exit 1;
fi

file=$1

sox $file side1.wav remix 1
sox $file side2.wav remix 2

fax_decoder side1.wav 0 > temp.txt
fax_decoder side2.wav 1 >> temp.txt

cat temp.txt | grep -E "MESSAGE|STATS" | sort > flow.txt 

echo success
