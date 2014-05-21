#/usr/bin/python

# Go under dev/scripts/toolbox/py/ and launch this script using the following command:
# python clean_ref.py

# Import system Python modules
import os

# Import regular expression Python module
import re

# Path where the text is located
TEXT_PATH = "../../../../corpus/khaling/toolbox/"

# Name of the text to clean
TEXT_NAME = "KHASolmeLamalit.txt"

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

# Split each line where 3 digits are found
tx = ''
mb = ''
ge = ''
ps = ''
for line in in_text.readlines():
    #if re.match(r"^\\tx (.*) (\d{3}) (.*$)", line):
    #out_text.write(re.sub(r"^\\wav8? ([-\w]+)", "\sf " + abs_path + r"\1.wav", line))
    if re.match(r"^\\tx .* \d{3} .*$", line):
        out_text.write(re.sub(r"^(\\tx) (.*) (\d{3}) (.*)$", r"\1 " + r"\2", line))
        if tx != '':
            print line
            raise AssertionError
        tx = re.sub(r"^(\\tx) (.*) (\d{3}) (.*)$", r"""\\ref solme2.""" + r"\3\n" + r"\1 " + r"\4", line)
    elif re.match(r"^\\mb .* \d{3} .*$", line):
        out_text.write(re.sub(r"^(\\mb) (.*) (\d{3}) (.*)$", r"\1 " + r"\2", line))
        if mb != '':
            print line
            raise AssertionError
        mb = re.sub(r"^(\\mb) (.*) (\d{3}) (.*)$", r"\1 " + r"\4", line)
    elif re.match(r"^\\ge .* \d{3} .*$", line):
        out_text.write(re.sub(r"^(\\ge) (.*) (\d{3}) (.*)$", r"\1 " + r"\2", line))
        if ge != '':
            print line
            raise AssertionError
        ge = re.sub(r"^(\\ge) (.*) (\d{3}) (.*)$", r"\1 " + r"\4", line)
    elif re.match(r"^\\ps .* \d{3} .*$", line):
        out_text.write(re.sub(r"^(\\ps) (.*) (\d{3}) (.*)$", r"\1 " + r"\2\n", line))
        if ps != '':
            print line
            raise AssertionError
        ps = re.sub(r"^(\\ps) (.*) (\d{3}) (.*)$", r"\1 " + r"\4", line)
        out_text.write(tx)
        out_text.write(mb)
        out_text.write(ge)
        out_text.write(ps)
        tx = ''
        mb = ''
        ge = ''
        ps = ''
    else:
        out_text.write(line)

# Do not forget to close files
in_text.close()
out_text.close()
