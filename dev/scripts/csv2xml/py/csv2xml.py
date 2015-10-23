#/usr/bin/python

# Go under dev/scripts/csv2xml/py/ and launch this script using the following command:
# python csv2xml.py

# Import Python modules
import os, sys, csv, codecs

# Path where the dictionary is located
DICT_PATH = "../"

# Input lexicon
dict = DICT_PATH + "na.csv"

# Define codec
codec = "utf8"

# Create 'obj' folder if it does not exist
if not os.path.exists("obj"):
    os.mkdir("obj")

# Functions from http://docs.python.org/2/library/csv.html
#
def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data), dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

class UTF8Recoder:
    """
        Iterator that reads an encoded stream and reencodes the input to UTF-8
        """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
    
    def __iter__(self):
        return self
    
    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
        A CSV reader which will iterate over lines in the CSV file "f",
        which is encoded in the given encoding.
        """
    
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
    
    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]
    
    def __iter__(self):
        return self

class UnicodeWriter:
    """
        A CSV writer which will write rows to CSV file "f",
        which is encoded in the given encoding.
        """
    
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    
    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    
    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

# Functions from the web
#
def convertXLS2CSV(aFile):
    '''converts a MS Excel file to csv w/ the same name in the same directory'''
    
    print "------ beginning to convert XLS to CSV ------"
    
    try:
        import win32com.client, os
        from win32com.client import constants as c
        excel = win32com.client.Dispatch('Excel.Application')
        
        fileDir, fileName = os.path.split(aFile)
        nameOnly = os.path.splitext(fileName)
        newName = nameOnly[0] + ".csv"
        outCSV = os.path.join(fileDir, newName)
        workbook = excel.Workbooks.Open(aFile)
        workbook.SaveAs(outCSV, c.xlCSVMSDOS) # 24 represents xlCSVMSDOS
        workbook.Close(False)
        excel.Quit()
        del excel
        
        print "...Converted " + nameOnly + " to CSV"
    except:
        print ">>>>>>> FAILED to convert " + aFile + " to CSV!"

#convertXLS2CSV(dict)

# My functions
#
def my_open(filename, access, encoding):
    try:
        my_file = open(filename, access, encoding)
    except TypeError:
        my_file = codecs.open(filename, access, encoding)
    return my_file

ureader = UnicodeReader(my_open(dict, 'rb', "utf-8"))
for row in ureader:
    print type(row)

with my_open(dict, 'rb', codec) as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE, quotechar=csv.excel.quotechar)
    for row in reader:
        print ', '.join(row)
    try:
        for row in unicode_csv_reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE, quotechar=csv.excel.quotechar):
            print ', '.join(row)
    except csv.Error as e:
        csvfile.close()
        sys.exit('file %s, line %d: %s' % (dict, reader.line_num, e))
    csvfile.close()

#pairs = [(lexeme, defn) for (lexeme, _, _, defn) in lexicon]
#lexemes, defns = zip(*pairs)
#defn_words = set(w for defn in defns for w in defn.split())
#sorted(defn_words.difference(lexemes))
