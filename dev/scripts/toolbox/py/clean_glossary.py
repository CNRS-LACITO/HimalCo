#/usr/bin/python

# Go under dev/scripts/toolbox/py/ and launch this script using the following command:
# python clean_glossary.py

## This script removes identical glossary entries if consecutive

# Import system Python modules
import os

# Import regular expression Python module
import re

# Path where the glossary is located
GLOSSARY_PATH = "../../../../corpus/koyi/ITE files/"

# Name of the glossary to clean
GLOSSARY_NAME = "Koy_glossary.txt"

# Create 'obj' folder if it does not exist
if not os.path.exists("obj"):
    os.mkdir("obj")

# Open input and output files
try:
    in_glossary = open(GLOSSARY_PATH + GLOSSARY_NAME, "r", encoding="utf8")
    out_glossary = open("./obj/output_glossary.txt", "w", encoding="utf8")
except TypeError:
    in_glossary = open(GLOSSARY_PATH + GLOSSARY_NAME, "r")
    out_glossary = open("./obj/output_glossary.txt", "w")

# Glossary only contains 'lx' and 'ge'
pattern = r"^\\(\w{2}) (.*)$"
lx = ''
ge = ''
previous_lx = ''
previous_ge = ''
for line in in_glossary.readlines():
    # Do not consider empty lines
    if line == "\n":
        continue
    result = re.search(pattern, line)
    if result:
        if result.group(1) == "lx":
            lx = result.group(2)
        elif result.group(1) == "ge":
            ge = result.group(2)
            # Write 'lx' and 'ge' lines only if different from previous ones
            if lx != previous_lx or ge != previous_ge:
                out_glossary.write("\n")
                out_glossary.write("\\lx " + lx + "\n")
                out_glossary.write("\\ge " + ge + "\n")
                # Update previous values with new ones
                previous_lx = lx
                previous_ge = ge
    else:
        out_glossary.write(line)

# Do not forget to close files
in_glossary.close()
out_glossary.close()
