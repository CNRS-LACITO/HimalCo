#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# python na/py/generate_lc.py

# Import system Python module
import sys
# Import utilities
sys.path.append(".")
from common import *

# Default values of command line arguments
DEFAULT_INPUT = "./obj/Dictionary_na.xml"
DEFAULT_OUTPUT = None

class GenerateLc(InOut, XmlFormat):
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
        parser.add_option("-o", "--output", dest="output", action="store", default=DEFAULT_OUTPUT, help="output MDF file [default=" + str(DEFAULT_OUTPUT) + "]")
        self.options = parser.parse_args()[0]
        # Compute output filename
        if self.options.output is None:
            self.options.output = "na/py/" + self.options.input[self.options.input.rfind('/') + 1:self.options.input.rfind('.')] + ".txt"

    def mono_noun(self, tones):
        """Get rules to apply.
        """
        rules = None,
        if tones == ["LM"]:
            rules = 6,
        elif tones == ["L"]:
            rules = 0,
        elif tones == ["H"]:
            rules = 3,
        return rules

    def di_noun(self, tones):
        """Get rules to apply.
        """
        rules = None,
        if tones == ["M", "M"]:
            rules = 2,
        elif tones == ["M", "#H"]:
            rules = 10, 2
        elif tones == ["M", "MH"]:
            rules = 2,
        elif tones == ["M", "H$"]:
            rules = 10, 2
        elif tones == ["M", "H"]:
            rules = 2,
        elif tones == ["L", "L"]:
            rules = 1, 7
        elif tones == ["M", "L"]:
            rules = 2,
        elif tones == ["L", "#H"]:
            rules = 10,
        elif tones == ["L", "M"]:
            rules = 6,
        return rules

    def mono_verb(self, tones):
        """Get rules to apply.
        """
        rules = None,
        if tones == ["H"]:
            rules = 3,
        elif tones == ["L"]:
            rules = 7,
        return rules

    def adj(self, tones):
        """Get rules to apply.
        """
        return self.mono_verb(tones)

    def apply_rules(self, rules, syllables_nb, tones):
        """Call each rule in order.
        """
        for rule in rules:
            if rule is not None:
                tones = getattr(self, "apply_rule_" + str(rule))(syllables_nb, tones)
        return tones

    def apply_rule_0(self, syllables_nb, tones):
        """Exception.
        """
        if tones == ["L"]:
            tones[0] = "M"
        return tones

    def apply_rule_1(self, syllables_nb, tones):
        """Rule 1: L tone spreads progressively (‘left-to-right’) onto syllables that are unspecified for tone.
        """
        if syllables_nb > len(tones) and tones[0] == "L":
            new_tones = []
            for i in range (0, syllables_nb - len(tones) + 1):
                new_tones.append("L")
            for i in range (syllables_nb - len(tones) + 1, syllables_nb):
                new_tones.append(tones[i - syllables_nb + len(tones)])
            return new_tones
        return tones

    def apply_rule_2(self, syllables_nb, tones):
        """Rule 2: Syllables that remain unspecified for tone after the application of Rule 1 receive M tone.
        """
        return tones

    def apply_rule_3(self, syllables_nb, tones):
        """Rule 3: In tone-group-initial position, H and M are neutralized to M.
        """
        if tones[0] == "H":
            tones[0] = "M"
        return tones

    def apply_rule_4(self, syllables_nb, tones):
        """Rule 4: A syllable following a H-tone syllable receives L tone.
        """
        for i in range (0, len(tones) - 1):
            if tones[i] == "H":
                tones[i+1] = "L"
        return tones

    def apply_rule_5(self, syllables_nb, tones):
        """Rule 5: All syllables following a HL or ML sequence receive L tone.
        """
        for i in range (0, len(tones) - 1):
            if tones[i] == "HL" or tones[i] == "ML":
                for j in range (i + 1, len(tones)):
                    tones[j] = "L"
                break
        return tones

    def apply_rule_6(self, syllables_nb, tones):
        """Rule 6: In tone-group-final position, H and M are neutralized to H if they follow a L tone.
        """
        if tones[-1] == "LM":
            tones[-1] = "LH"
        if len(tones) > 1:
            if tones[-2] == "L" and tones[-1] == "M":
                tones[-1] = "H"
        return tones

    def apply_rule_7(self, syllables_nb, tones):
        """Rule 7: If a tone group only contains L tones, a post-lexical H tone is added to its last syllable.
        """
        L = True
        for i in range (0, len(tones)):
            if tones[i] != "L":
                L = False
        if L:
            tones[-1] += "H"
        return tones
    
    def apply_rule_10(self, syllables_nb, tones):
        """Final #H => M, H$ => H.
        """
        if tones[-1] == "#H":
            tones[-1] = "M"
        elif tones[-1] == "H$":
            tones[-1] = "H"
        return tones

    def trans_tones(self, ps, syllables_nb, tones):
        """Depending on 'ps' and number of syllables, get 'lc' tones.
        """
        if ps == "n":
            if syllables_nb == 1:
                tones = self.apply_rules(self.mono_noun(tones), syllables_nb, tones)
            elif syllables_nb == 2:
                tones = self.apply_rules(self.di_noun(tones), syllables_nb, tones)
        elif ps == "v" and syllables_nb == 1:
            tones = self.apply_rules(self.mono_verb(tones), syllables_nb, tones)
        elif ps == "adj":
            tones = self.apply_rules(self.adj(tones), syllables_nb, tones)
        return tones

    def tones_to_analysis(self, ps, syllables_nb, tones):
        """Depending on 'ps' and number of syllables, map tones in list (one per syllable) into an analysis string.
        """
        analysis = None
        if ps == "n":
            # Monosyllabic nouns
            if syllables_nb == 1:
                if tones == ["H"]:
                    analysis = "#H"
                elif tones == ["MH"]:
                    analysis = "MH#"
                else:
                    analysis = tones[0]
            # Disyllabic nouns
            elif syllables_nb == 2:
                if tones == ["M", "M"]:
                    analysis = "M"
                elif tones == ["M", "#H"]:
                    analysis = "#H"
                elif tones == ["M", "MH"]:
                    analysis = "MH#"
                elif tones == ["M", "H$"]:
                    analysis = "H$"
                elif tones == ["M", "H"]:
                    analysis = "H#"
                elif tones == ["L", "L"]:
                    analysis = "L"
                elif tones == ["M", "L"]:
                    analysis = "L#"
                elif tones == ["L", "MH"]:
                    analysis = "LM+MH#"
                elif tones == ["L", "#H"]:
                    analysis = "LM+#H"
                elif tones == ["L", "M"]:
                    analysis = "LM"
                elif tones == ["L", "H"]:
                    analysis = "LH"
        elif ps == "v" and syllables_nb == 1:
            # TOLERATE M?
            if tones == ["M"]:
                analysis = "Ma"
            # TOLERATE L?
            elif tones == ["L"]:
                analysis = "La"
            else:
                analysis = tones[0]
        elif ps == "adj" and syllables_nb == 1:
            # TOLERATE M?
            if tones == ["M"]:
                analysis = "Ma"
            # TOLERATE L?
            elif tones == ["L"]:
                analysis = "La"
            # TOLERATE #H?
            elif tones == ["#H"]:
                analysis = "H"
            else:
                analysis = tones[0]
        return analysis

    def lx_to_lc(self, lx, ps, np=None, codec=True):
        """Depending on 'ps' and number of syllables, compute 'lc' form 'lx'.
        """
        lc = ''
        if lx is None or ps is None:
            return None
        if codec:
            lx = lx.decode(encoding=CODEC)
        # Handle '-' separator
        full_analysis = ''
        for lx_segment in lx.split('-'):
            lc_segment = ''
            syllables, tones = self.dissect(lx_segment)
            syllables_nb = len(syllables)
            analysis = self.tones_to_analysis(ps, syllables_nb, tones)
            if analysis is None:
                return None
            # Reconstitute analysis from segments
            if full_analysis != '':
                full_analysis += u"°"
            full_analysis += analysis
            lc_tones = self.trans_tones(ps, syllables_nb, tones)
            if lc_tones is None:
                return None
            for i in range (0, syllables_nb):
                lc_segment += syllables[i]
                lc_segment += self.tone_str_to_ipa(lc_tones[i])
            # Reconstitute 'lc' from segments
            if lc != '':
                lc += '-'
            lc += lc_segment
        # Check that 'np' corresponds to tones composing 'lx'
        if np is not None:
            # In case of different variants separated with '/' character, compare with each of them
            equal = False
            # TOLERATE '+' instead of '°' character?
            full_analysis_bis = full_analysis.replace(u"°", '+')
            for variant in np.split('/'):
                if variant.strip() == full_analysis or variant.strip() == full_analysis_bis:
                    equal = True
            # Consider all assumptions separated by '?' character
            for hypothesis in np.split('?'):
                if hypothesis.strip() == full_analysis or hypothesis.strip() == full_analysis_bis:
                    equal = True
            if not equal:
                return None
        if codec:
            lc = lc.encode(encoding=CODEC)
        return lc

    def dissect(self, lx):
        """Return syllables and tones composing 'lx'.
        """
        import re
        syllables = []
        tones = []
        if lx is None:
            return syllables, tones
        tones_ipa = "˩˧˥".decode(encoding=CODEC)
        mono_pattern = "([^" + tones_ipa + "#$]+)(#?[" + tones_ipa + "]{1,2}[$#]?)([abcd123]?)"
        # Monosyllabic
        pattern = "^" + mono_pattern + "$"
        if re.search(pattern, lx):
            result = re.match(pattern, lx)
            syllables.append(result.group(1))
            tones.append(self.tone_ipa_to_str(result.group(2) + result.group(3)))
        # Disyllabic: add a constraint on the second syllab which must have at least 2 characters
        pattern = "^" + mono_pattern + "([^" + tones_ipa + "#$]{2,})(#?[" + tones_ipa + "]{1,2}[$#]?)([abcd123]?)" + "$"
        if re.search(pattern, lx):
            result = re.match(pattern, lx)
            syllables.append(result.group(1))
            syllables.append(result.group(4))
            tones.append(self.tone_ipa_to_str(result.group(2) + result.group(3)))
            tones.append(self.tone_ipa_to_str(result.group(5) + result.group(6)))
        return syllables, tones

    def tone_str_to_ipa(self, tone):
        """Convert a tone string composed of 'LMH' characters into a tone string composed of '˩˧˥' IPA characters.
        """
        new_tone = tone
        tones_str = "LMH"
        tones_ipa = "˩˧˥".decode(encoding=CODEC)
        for i in range (0,3):
            new_tone = new_tone.replace(tones_str[i], tones_ipa[i])
        return new_tone

    def tone_ipa_to_str(self, tone):
        """Convert a tone string composed of '˩˧˥' characters into a tone string composed of 'LMH' IPA characters.
        """
        new_tone = tone
        tones_ipa = "˩˧˥".decode(encoding=CODEC)
        tones_str = "LMH"
        for i in range (0,3):
            new_tone = new_tone.replace(tones_ipa[i], tones_str[i])
        return new_tone

    def add_lc(self):
        """Compute 'lc' field.
        """
        out_file = self.open_write(self.options.output)
        err_file = self.open_write("na/py/tone_errors.txt")
        for lxGroup in self.tree.iterfind("lxGroup"):
            lc = None
            lx = None
            ps = None
            np = None
            for subelement in lxGroup:
                if subelement.tag == "lx":
                    lx = subelement.text
                elif subelement.tag == "ps":
                    ps = subelement.text
                elif subelement.tag == "np":
                    try:
                        if subelement.attrib["type"] == "tone":
                            np = subelement.text
                    except KeyError:
                        pass
            # Generate 'lc' from 'lx' and 'ps'
            lc = self.lx_to_lc(lx, ps, np=np, codec=False)
            # Write result in output or error file
            if lc is not None:
                file = out_file
            else:
                file = err_file
            if lc is None:
                lc = str(lc)
            if np is None:
                np = str(np)
            if lx is not None:
                file.write("\lx " + lx + "\n")
                file.write("\lc " + lc + "\n")
                file.write("\ps " + str(ps) + "\n")
                file.write("\\np " + np + "\n\n")
        err_file.close()
        out_file.close()

    def main(self):
        self.parse_options()
        # Parse input XML file
        self.tree = parse(self.options.input)
        # Add 'lc' marker
        self.add_lc()

if __name__ == '__main__':
    converter = GenerateLc()
    converter.main()
    # Exit program properly
    sys.exit(0)
