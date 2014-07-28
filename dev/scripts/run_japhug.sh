#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# ./run_japhug.sh

# Results are available under dev/scripts/obj/ folder.

python mdf2xml/py/mdf2xml_tb.py -t japhug
python xml2tex/py/xml2tex.py -t japhug
