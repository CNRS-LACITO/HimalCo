#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/scripts/tools and launch this script using the following command:
# ./degrade_wav2mp3.sh

# Results are directly available under dict/japhug/data/audio/mp3/ and dict/japhug/data/audio/wav/ folders.

for audio in ../../../dict/japhug/data/audio/*/*
do
./ffmpeg -i $audio -ab 128k -ar 44100 ${audio%.*}.mp3
done
