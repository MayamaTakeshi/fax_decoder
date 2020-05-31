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

wav_file=$1
out_file=$2

mkdir -p temp

sox $wav_file temp/side1.wav remix 1
sox $wav_file temp/side2.wav remix 2

fax_decoder temp/side1.wav 0 > temp/temp.txt 2>&1
fax_decoder temp/side2.wav 1 >> temp/temp.txt 2>&1

cat temp/temp.txt | grep -E "MESSAGE|STATS" | sort > $out_file

echo "$out_file successfully generated"
