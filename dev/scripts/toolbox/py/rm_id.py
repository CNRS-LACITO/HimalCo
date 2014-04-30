#/usr/bin/python

# Go under dev/scripts/toolbox/py/ and launch this script using the following command:
# python rm_id.py

# Import system Python modules
import os

# Import regular expression Python module
import re

# Path where the dictionary is located
DICT_PATH = "../../../../dict/na/toolbox/"

# Create 'obj' folder if it does not exist
if not os.path.exists("obj"):
    os.mkdir("obj")

# Open input and output files
try:
    in_dict = open(DICT_PATH + "Dictionary.txt", "r", encoding="utf8")
    out_dict = open("./obj/output.txt", "w", encoding="utf8")
except TypeError:
    in_dict = open(DICT_PATH + "Dictionary.txt", "r")
    out_dict = open("./obj/Dictionary.txt", "w")

# Remove id attribute from each line starting with the \lx or \se markers
for line in in_dict.readlines():
    if re.match(r"^\\lx", line):
        out_dict.write(re.sub(r"""^\\lx <id="[-\d]+">[ \t]+(.*)""", "\lx " + r"\1", line))
    elif re.match(r"^\\se", line):
        out_dict.write(re.sub(r"""^\\se <id="[-\d]+">[ \t]+(.*)""", "\se " + r"\1", line))
    else:
        out_dict.write(line)

# Do not forget to close files
in_dict.close()
out_dict.close()
