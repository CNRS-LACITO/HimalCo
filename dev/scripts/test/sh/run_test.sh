#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# test/sh/run_test.sh

# Unit tests

python utest/test_all.py

# Results are available under dev/scripts/obj/ folder.

python mdf2xml/py/mdf2xml_tb.py -t japhug1
python mdf2xml/py/mdf2xml_tb.py -t japhug2
python mdf2xml/py/mdf2xml_tb.py -t khaling1
python mdf2xml/py/mdf2xml_tb.py -t khaling2
python xls2xml/py/xls2mdf.py -t na1
python xls2xml/py/mdf2xml_tb.py -t na1

# Na

python xls2xml/py/xls2mdf.py
python xls2xml/py/mdf2xml_tb.py -t na
python xml2tex/py/xml2tex.py -t na
cd obj/
/usr/texbin/xelatex Dictionary_na.tex >> /dev/null
/usr/texbin/xelatex Dictionary_na.tex >> /dev/null
cd ..

# Japhug

python mdf2xml/py/mdf2xml_tb.py -t japhug
python xml2tex/py/xml2tex.py -t japhug
cd obj/
/usr/texbin/xelatex Dictionary_japhug.tex >> /dev/null
/usr/texbin/xelatex Dictionary_japhug.tex >> /dev/null
cd ..
