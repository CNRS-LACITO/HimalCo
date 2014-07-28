#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# ./run_na.sh

# Results are available under dev/scripts/obj/ folder.

python xls2xml/py/mdf2xml_tb.py -t na
python xml2tex/py/xml2tex.py -t na
python xml2tex/py/xml2tex.py -t na -l fr
python xml2tex/py/xml2tex.py -t na -l en
