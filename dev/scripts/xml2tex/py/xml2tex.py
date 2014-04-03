#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# python xml2tex/py/xml2tex.py

# Import system Python module
import sys
# Import utilities
sys.path.append(".")
from common import *

# Default values of command line arguments
DEFAULT_INPUT = None
DEFAULT_OUTPUT = None
DEFAULT_TEST = None

order = dict({'':0,
    'A':1.1, 'a':1.2, 'æ':1.3, 'ɑ':1.4, 'ɐ':1.5,
    'ɤ':2,
    'B':3.1, 'b':3.2, 'β':3.3, 'ɓ':3.4, 'ʙ':3.5,
    'C':4.1, 'c':4.2,
    'ɕ':5.1, 'ç':5.2,
    'D':6.1, 'd':6.2, 'ɖ':6.3, 'ð':6.4, 'ɗ':6.5,
    'E':7.1, 'e':7.2, 'ɛ':7.3, 'ə':7.4, 'ɜ':7.5, 'œ':7.6, 'ɶ':7.7, 'ɘ':7.8, 'ɞ':7.9,
    'F':8.1, 'f':8.2, 'ɸ':8.3,
    'G':9.1, 'g':9.2, 'ɡ':9.3,
    'ɣ':10.1, 'ɠ':10.2,
    'ɢ':11.1, 'ʛ':11.1,
    'H':12.1, 'h':12.2, 'ɦ':12.3, 'ɥ':12.4, 'ħ':12.5, 'ʜ':12.6, 'ɧ':12.7,
    'I':13.1, 'i':13.2, 'ɪ':13.3, 'ɨ':13.4,
    'J':14.1, 'j':14.2, 'ʝ':14.3,
    'ɟ':15.1, 'ʄ':15.2,
    'K':16.1, 'k':16.2,
    'L':17.1, 'l':17.2, 'ɭ':17.3,
    'ɬ':18.1, 'ɮ':18.2, 'ʎ':18.3, 'ʟ':18.4, 'ɺ':18.5,
    'M':19.1, 'm':19.2, 'ɱ':19.3,
    'N':20.1, 'n':20.2,
    'ɳ':21.1, 'ɲ':21.2,
    'ŋ':22,
    'ɴ':23,
    'O':24.1, 'o':24.2, 'ɔ':24.3, 'ɒ':24.4, 'ø':24.5, 'ɵ':24.6,
    'P':25.1, 'p':25.2, 'ʘ':25.3,
    'Q':26.1, 'q':26.2,
    'R':27.1, 'r':27.2, 'ɽ':27.3, 'ɹ':27.4, 'ɾ':27.5, 'ɻ':27.6,
    'ʀ':28.1, 'ʁ':28.2,
    'S':29.1, 's':29.2,
    'ʂ':30.1, 'ʃ':30.2,
    'T':31.1, 't':31.2, 'ʈ':31.3, 'θ':31.4,
    'U':32.1, 'u':32.2, 'ʊ':32.3,
    'ɯ':33.1, 'ʌ':33.2, 'ʉ':33.3,
    'V':34.1, 'v':34.2, 'ʋ':34.3,
    'W':35.1, 'w':35.2, 'ʍ':35.3, 'ɰ':35.4,
    'X':36.1, 'x':36.2,
    'χ':37,
    'Y':38.1, 'y':38.2, 'ʏ':38.3,
    'Z':39.1, 'z':39.2,
    'ʐ':40.1, 'ʒ':40.2,
    'ʑ':41,
    'ʕ':42.1, 'ʢ':42.2, 'ʔ':42.3, 'ʡ':42.4,
    'ǃ':43.1, 'ǀ':43.2, 'ǂ':43.3, 'ǁ':43.4,
    '_':44,
    # Special characters
    '*':45.1, '˭':45.2, 'ʰ':45.3, ' ̩':45.4, '‑':45.5})
unicode_order = ({})
for key in order.keys():
    unicode_order.update({key.decode(encoding=CODEC):order[key]})

class Lexeme(object):
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        for i in range(min(len(self.obj), len(other.obj))):
            try:
                if unicode_order[self.obj[i]] == unicode_order[other.obj[i]]:
                    continue
                return unicode_order[self.obj[i]] < unicode_order[other.obj[i]]
            # Handle other characters
            except KeyError:
                if self.obj[i] == other.obj[i]:
                    continue
                return self.obj[i] < other.obj[i]
        # If all characters match, the smallest string is the shortest one
        return len(self.obj) < len(other.obj)
    def __gt__(self, other):
        for i in range(min(len(self.obj), len(other.obj))):
            try:
                if unicode_order[self.obj[i]] == unicode_order[other.obj[i]]:
                    continue
                return unicode_order[self.obj[i]] > unicode_order[other.obj[i]]
            # Handle other charcaters
            except KeyError:
                if self.obj[i] == other.obj[i]:
                    continue
                return self.obj[i] < other.obj[i]
        # If all characters match, the biggest string is the longest one
        return len(self.obj) > len(other.obj)
    def __eq__(self, other):
        # If both strings do not have the same length, they do not equal
        if len(self.obj) != len(other.obj):
            return False
        for i in range(len(self.obj)):
            try:
                # If at least one character differs, both strings do not equal
                if unicode_order[self.obj[i]] != unicode_order[other.obj[i]]:
                    return False
            # Handle other characters
            except KeyError:
                if self.obj[i] != other.obj[i]:
                    return False
        # If all characters match, both strings equal
        return True
    def __le__(self, other):
        for i in range(min(len(self.obj), len(other.obj))):
            try:
                if unicode_order[self.obj[i]] == unicode_order[other.obj[i]]:
                    continue
                return unicode_order[self.obj[i]] <= unicode_order[other.obj[i]]
            # Handle other characters
            except KeyError:
                if self.obj[i] == other.obj[i]:
                    continue
                return self.obj[i] <= other.obj[i]
        # If all characters match, the smallest string is the shortest one
        return len(self.obj) <= len(other.obj)
    def __ge__(self, other):
        for i in range(min(len(self.obj), len(other.obj))):
            try:
                if unicode_order[self.obj[i]] == unicode_order[other.obj[i]]:
                    continue
                return unicode_order[self.obj[i]] >= unicode_order[other.obj[i]]
            # Handle other characters
            except KeyError:
                if self.obj[i] == other.obj[i]:
                    continue
                return self.obj[i] >= other.obj[i]
        # If all characters match, the biggest string is the longest one
        return len(self.obj) >= len(other.obj)
    def __ne__(self, other):
        # If both strings do not have the same length, they do not equal
        if len(self.obj) != len(other.obj):
            return True
        for i in range(len(self.obj)):
            try:
                # If at least one character differs, both strings do not equal
                if unicode_order[self.obj[i]] != unicode_order[other.obj[i]]:
                    return True
            # Handle other characters
            except KeyError:
                if self.obj[i] != other.obj[i]:
                    return True
        # If all characters match, both strings equal
        return False

class Xml2Tex(InOut, XmlFormat):
    def __init__(self):
        XmlFormat.__init__(self)

    def parse_options(self):
        """Get command line arguments.
        """
        # Options management
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print more details to stdout [default=False]")
        parser.add_option("-i", "--input", dest="input", action="store", default=DEFAULT_INPUT, help="input XML file [default=" + str(DEFAULT_INPUT) + "]")
        parser.add_option("-o", "--output", dest="output", action="store", default=DEFAULT_OUTPUT, help="output LaTeX file [default=" + str(DEFAULT_OUTPUT) + "]")
        parser.add_option("-t", "--test", dest="test", action="store", default=DEFAULT_TEST, help="test to run [default=" + str(DEFAULT_TEST) + "]")
        self.options = parser.parse_args()[0]
        # Tests
        if self.options.test is not None:
            if self.options.test == "japhug":
                self.options.input = "obj/Dictionary_japhug.xml"
            elif self.options.test == "na":
                self.options.input = "obj/Dictionary_na.xml"
            else:
                sys.exit(-1)
        # Compute output filename
        if self.options.output is None:
            self.options.output = "./obj/" + self.options.input[self.options.input.rfind('/') + 1:self.options.input.rfind('.') + 1] + "tex"

    def sort_lx(self):
        data = []
        for lxGroup in self.tree.iter("lxGroup"):
            for child in lxGroup.getchildren():
                if child.tag == "lx":
                    key = Lexeme(child.text)
                    data.append((key, lxGroup))
        data.sort()
        td = Element("toolbox_data")
        td.text = "\n    "
        for (k, e) in data:
            td.append(e)
        self.tree = ElementTree(element=td)
        self.tree.write(self.options.input.rstrip(".xml") + "_sorted.xml", encoding=CODEC)

    def compute_header(self):
        """Create LaTeX header.
        """
        if self.options.test == "japhug":
            hdr = self.open_read("./xml2tex/tex/preamble_GJ.tex")
        elif self.options.test == "na":
            hdr = self.open_read("./xml2tex/tex/preamble_AM.tex")
        header = hdr.read()
        hdr.close()
        return header

    def add_lx_id(self):
        """Add 'lx' identifiers.
        """
        id = 0
        for element in self.tree.getroot().iter():
            if element.tag == "lx":
                id += 1
                element.attrib['id'] = str(id)
        self.tree.write(self.options.input.rstrip(".xml") + "_new.xml", encoding=CODEC)
        print id, "record(s)"

    def format_font(self, text):
        """Replace '{xxx}' or '\{xxx}' by '\ipa{xxx}'.
        """
        return text.replace('\\', '').replace('{', "\\ipa{")

    def format_pinyin(self, text):
        """Replace '@xxx' by '\\textcolor{gray}{xxx}' in 'lx', 'dv', 'xv' fields (already in API).
        """
        import re
        return re.sub(r"(\w*)@(\w*)", r"\1" + r"\\textcolor{gray}{" + r"\2" + "}", text)

    def format_tone(self, text, np=False):
        """Format tone type as subscript: '\textsubscript{xxx}'.
        """
        import re
        if np and len(text) < 10: # 2 characters maximum followed by an index, for one or several syllabs
            tones_str = "LMH"
        else:
            tones_str = "˩˧˥".decode(encoding=CODEC)
        api_str = ""
        for character in unicode_order.keys():
            if int(unicode_order[character]) < 43: # consider only API characters
                api_str += character
        # Case when tone type ends the string
        pattern = "^(\w*)([" + tones_str + "]{1,2})([abcd123])"
        if re.search(pattern + "$", text):
            result = re.sub(pattern, r"\1" + r"\2" + r"\\textsubscript{" + r"\3" + "}", text)
            return result
        # In the case when tone type is in the middle of the string, check if it is not followed by another syllab
        pattern += "([^0-9" + api_str + "]\w*)"
        if re.search(pattern, text):
            result = re.sub(pattern, r"\1" + r"\2" + r"\\textsubscript{" + r"\3" + "}" + r"\4", text)
            return result
        return text

    def write_fields(self):
        """Write LaTeX output file.
        """
        tex_file = self.open_write(self.options.output)
        tex_file.write(self.compute_header())
        tex_file.write("\n\\begin{document}\n")
        tex_file.write("\\maketitle\n")
        tex_file.write("\\newpage\n")
        tex_file.write("\\begin{multicols}{2}\n")
        # Tags added by Toolbox
        tags_tb = set(["toolbox_data", "header", "_sh"])
        # Tags that need additional references
        tags_ref = set(["sy", "an", "cf"])
        # Tags corresponding to examples (do not include comments: 'xc')
        tags_ex = set(["xv", "xe", "xn", "xr", "xf"])
        ex_started = False
        # Tones
        tones = set(["˩", "˧", "˥"])
        # japhug : 'ipa' = API ; chinois : 'zh' ; tibetain : r
        format = dict({
            "lx"    : lambda e: "\n\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{" + e.text + "}} \\hspace{0.2cm} \\hypertarget{" + e.attrib['id'] + "}{}\n",
            "sf"    : lambda e: "",
            "wav"   : lambda e: "",
            "wav8"  : lambda e: "",
            "hbf"   : lambda e: "",
            "hm"    : lambda e: "",
            "dt"    : lambda e: "",
            "ph"    : lambda e: "",
            "se"    : lambda e: "\n\\hspace{0.2cm} {\large \ipa{" + e.text + "}}\n",
            "bw"    : lambda e: "",
            "et"    : lambda e: "\\textit{Etym:} \\textbf{\ipa{" + e.text + "}}.\n",
            "ec"    : lambda e: "",
            "ps"    : lambda e: "\\textcolor{teal}{\\textit{" + e.text + "}}\n",
            "sn"    : lambda e: "",
            "sy"    : lambda e: "\\textit{Syn:} ",
            "an"    : lambda e: "\\textit{Ant:} ",
            "cf"    : lambda e: "\\textit{See:} ",
            "sd"    : lambda e: "",
            "nt"    : lambda e: "",
            "np"    : lambda e: "\\textit{Tone:} " + e.text + ".\n",
            "ng"    : lambda e: "",
            "nd"    : lambda e: "",
            "nq"    : lambda e: "\\textit{[Ques:} \nq{" + e.text + "} \\textit{]}.\n",
            "so"    : lambda e: "",
            "a"     : lambda e: "\\textit{Variant:} \\textbf{\ipa{" + e.text + "}}.\n",
            "va"    : lambda e: "",
            "vf"    : lambda e: "",
            "pdl"   : lambda e: "\\textit{" + e.text + ":} ",
            "pdv"   : lambda e: "\\textbf{\ipa{" + e.text + "}}.\n",
            "pdf"   : lambda e: "",
            "a2s"   : lambda e: "\\textit{[Th\`{e}me du pass\\'{e}:} \ipa{" + e.text + "} \\textit{]}.\n",
            "comit" : lambda e: "\\textit{[Comitatif:} \ipa{" + e.text + "} \\textit{]}.\n",
            "constr": lambda e: "\\textit{[Construction:} \ipa{" + e.text + "} \\textit{]}.\n",
            "dv"    : lambda e: "\\textbf{\ipa{" + e.text + "}}.\n",
            "gv"    : lambda e: "",
            "de"    : lambda e: e.text + ".\n",
            "ge"    : lambda e: e.text + "\n",
            "dn"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "gn"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "dr"    : lambda e: "",
            "gr"    : lambda e: "",
            "df"    : lambda e: "",
            "gf"    : lambda e: "",
            "uv"    : lambda e: "\\textit{Usage:} \\textbf{\ipa{" + e.text + "}}.\n",
            "un"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "ev"    : lambda e: "\\textbf{\ipa{" + e.text + "}}.\n",
            "en"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "er"    : lambda e: "",
            "rf"    : lambda e: "",
            "xv"    : lambda e: "\\ex \ipa{" + e.text + "}\n",
            "xe"    : lambda e: "\\trans " + e.text + "\n",
            "xn"    : lambda e: "\\trans \\textit{\zh{" + e.text + "}}\n",
            "xr"    : lambda e: "",
            "xf"    : lambda e: "\\trans " + e.text + "\n",
            "xc"    : lambda e: ""
        })
        # Keep reference errors
        errors = set()
        current_character = ''
        for element in self.tree.getroot().iter():
            # Handle reserved characters: \ { } $ # & _ ^ ~ %
            if element.text.find("{") != -1:
                element.text = self.format_font(element.text)
            if element.text.find("@") != -1:
                element.text = self.format_pinyin(element.text)
            if element.text.find("#") != -1:
                element.text = element.text.replace('#', '\#')
            if element.text.find("_") != -1:
                element.text = element.text.replace('_', '\_')
            if element.text.find("&") != -1:
                element.text = element.text.replace('&', '\&')
            if element.text.find("$") != -1:
                # Do not know what to do with '$' character
                element.text = element.text.replace('$', '')
            if element.tag == "pdl" and element.text == "directional":
                # Use abbreviation
                element.text = "dir"
            if element.tag == "np":
                # Format tone if any
                element.text = self.format_tone(element.text, np=True)
            if element.text == '_':
                # LaTeX returns error in case of "\ipa{_}"
                pass
            elif element.tag in tags_tb:
                # Remove
                pass
            elif element.tag.find("Group") != -1 :
                # Remove
                pass
            else:
                # Handle examples
                if element.tag in tags_ex:
                    if not ex_started:
                        tex_file.write("\\setcounter{exx}{0}\n")
                        tex_file.write("\\begin{exe}\n")
                        ex_started = True
                else:
                    if ex_started:
                        tex_file.write("\\end{exe}\n")
                        ex_started = False
                # Check if current element is a lexeme starting with a different character than previous lexeme
                if element.tag == "lx" and int(unicode_order[element.text[0]]) != int(unicode_order[current_character])\
                    and int(unicode_order[element.text[0]]) < 45: # do not consider special characters (hugly!)
                    current_character = element.text[0]
                    tex_file.write("\\newpage\n")
                    title = ''
                    for key,value in sorted(unicode_order.items(), key=lambda x: x[1]):
                        if int(value) == int(unicode_order[current_character]):
                            title += ' ' + key
                    tex_file.write("\\part*{-\ipa{" + title + "} -}\n")
                # Format tone if any, then keep text as it was to handle cross-references
                text = element.text
                element.text = self.format_tone(element.text)
                tex_file.write(format[element.tag](element))
                element.text = text
                if element.tag in tags_ref:
                    from string import digits
                    found = False
                    # Check if there is an homonym number at the end of the string
                    if element.text[-1] in digits:
                        for lxGroup in self.tree.iterfind("lxGroup"):
                            lx = None
                            for subelement in lxGroup:
                                if subelement.tag == "lx" and subelement.text == element.text[:-1]:
                                    lx = subelement
                                if lx is not None and subelement.tag == "hm" and subelement.text == element.text[-1]:
                                    tex_file.write("\\hyperlink{" + lx.get('id') + "}{" + lx.text + "\\textsuperscript{" + element.text[:-1] + "}}.\n")
                                    found = True
                                    break
                    # If there is no homonym number, just search for the whole string
                    else:
                        for lx in self.tree.iterfind("lxGroup/lx"):
                            if lx.text == element.text:
                                tex_file.write("\\hyperlink{" + lx.get('id') + "}{" + lx.text + "}.\n")
                                found = True
                                break
                    if not found:
                        # Just write the reference without hyperlink and log error
                        tex_file.write(element.text + ".\n")
                        errors.add(element.text)
        tex_file.write("\end{multicols}\n")
        tex_file.write("\n\end{document}\n")
        tex_file.close()
        for error in errors:
            print error

    def main(self):
        self.parse_options()
        # Parse input XML file
        self.tree = parse(self.options.input)
        if self.options.test == "japhug":
            # Add 'lx' identifiers
            self.add_lx_id()
        # Sort in alphabetical order
        self.sort_lx()
        # Convert to LaTeX
        self.write_fields()

if __name__ == '__main__':
    converter = Xml2Tex()
    converter.main()
    # Exit program properly
    sys.exit(0)
