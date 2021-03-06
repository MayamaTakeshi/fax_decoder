#!/bin/bash

set -o errexit
set -o nounset
#set -o pipefail # if grep in the pipe fails, it should be ignored (it will happen if the wav file doesn't have fax communication)

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

# do not redirect stderr to stdout using 2>&1 because logs from spandsp might mess with our logs.
fax_decoder temp/side1.wav 0 > temp/temp.txt
fax_decoder temp/side2.wav 1 >> temp/temp.txt

cat temp/temp.txt | grep -E "TONE|MESSAGE|STATS" | sort > $out_file

echo "$out_file successfully generated"

