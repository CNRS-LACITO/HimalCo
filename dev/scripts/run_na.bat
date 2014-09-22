REM -*- coding: utf-8 -*-

REM Go under dev/scripts/ and launch this script using the following command:
REM run_na.bat

REM Results are available under dev/scripts/obj/ folder.

python xls2xml/py/mdf2xml_tb.py -t na
python xml2tex/py/xml2tex.py -t na
python xml2tex/py/xml2tex.py -t na -l fr
python xml2tex/py/xml2tex.py -t na -l en
