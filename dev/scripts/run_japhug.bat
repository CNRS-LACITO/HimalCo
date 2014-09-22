REM # -*- coding: utf-8 -*-

REM Go under dev/scripts/ and launch this script using the following command:
REM run_japhug.bat

REM Results are available under dev/scripts/obj/ folder.

python mdf2xml/py/mdf2xml_tb.py -t japhug
python xml2tex/py/xml2tex.py -t japhug
