#/usr/bin/python

# Go under dev/scripts/xml2html/py/ and launch this script using the following command:
# python lexicon.py

legal_pos = set(['n', 'v.t.', 'v.i.', 'adj', 'det'])
pattern = re.compile(r"'font-size:11.0pt'>([a-z.]+)<")
document = open("dict.htm").read()
used_pos = set(re.findall(pattern, document))
illegal_pos = used_pos.difference(legal_pos)
print list(illegal_pos)
