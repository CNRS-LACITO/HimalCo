#/usr/bin/python

# Go under dev/scripts/toolbox/py/ and launch this script using the following command:
# python add_ref.py

# Import system Python modules
import os

# Import regular expression Python module
import re

# Path where the text is located
TEXT_PATH = "../../../../corpus/koyi/ITE files/"

# Name of the text to clean
TEXT_NAME = "Koy_Syurime_ok"

# Create 'obj' folder if it does not exist
if not os.path.exists("obj"):
    os.mkdir("obj")

# Open input and output files
try:
    in_text = open(TEXT_PATH + TEXT_NAME, "r", encoding="utf8")
    out_text = open("./obj/output.txt", "w", encoding="utf8")
except TypeError:
    in_text = open(TEXT_PATH + TEXT_NAME, "r")
    out_text = open("./obj/output.txt", "w")

# Add 'ref' line before each 'sync_d' line
line_nb = 0
out_text.write("\\id Sjurime\n")
for line in in_text.readlines():
    if re.match(r"^\\sync_d .*$", line):
        line_nb += 1
        out_text.write("\\ref Sjurime." + "%03d" % line_nb + "\n")
    out_text.write(line)

# Do not forget to close files
in_text.close()
out_text.close()
