#/usr/bin/python

# Go under dev/scripts/html2csv/py/ and launch this script using the following command:
# python html2csv.py

def lexical_data(html_file):
    SEP = '_ENTRY'
    html = open(html_file).read()
    html = re.sub(r'<p', SEP + '<p', html)
    text = nltk.clean_html(html)
    text = ' '.join(text.split())
    for entry in text.split(SEP):
        if entry.count(' ') > 2:
            yield entry.split(' ', 3)

import csv
writer = csv.writer(open("dict1.csv", "wb"))
writer.writerows(lexical_data("dict.htm"))
