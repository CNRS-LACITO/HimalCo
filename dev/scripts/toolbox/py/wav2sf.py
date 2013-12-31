#/usr/bin/python

# Go under dev/scripts/toolbox/py/ and launch this script using the following command:
# python wav2sf.py

# Import system Python modules
import os

# Import regular expression Python module
import re

# Path where the dictionary is located
DICT_PATH = "../../../../dict/japhug/toolbox/"

# Create 'obj' folder if it does not exist
if not os.path.exists("obj"):
    os.mkdir("obj")

# Compute audio files absolute path
if os.name is 'posix':
    abs_path = os.path.realpath("../../../../dict/japhug/data/audio") + '/'
else:
    abs_path = os.path.realpath("..\..\..\..\dict\japhug\data") + r'\\audio\\'

# Open input and output files
try:
    in_dict = open(DICT_PATH + "Dictionary.txt", "r", encoding="utf8")
    out_dict = open("./obj/output.txt", "w", encoding="utf8")
except TypeError:
    in_dict = open(DICT_PATH + "Dictionary.txt", "r")
    out_dict = open("./obj/output.txt", "w")

# Replace each line starting with the \wav or \wav8 markers by a line starting with the \sf standard marker
# Also add relative path and .wav extension to audio filename
for line in in_dict.readlines():
    if re.match(r"^\\wav", line):
        out_dict.write(re.sub(r"^\\wav8? ([-\w]+)", "\sf " + abs_path + r"\1.wav", line))
    else:
        out_dict.write(line)

# Do not forget to close files
in_dict.close()
out_dict.close()
