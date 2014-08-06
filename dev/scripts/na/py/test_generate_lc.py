#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from generate_lc import *

## Test GenerateLc class

class TestGenerateLcFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a GenerateLc object
        self.gen = GenerateLc()

    def tearDown(self):
        # Release instantiated objects
        del self.gen.options, self.gen

    def test_parse_options(self):
        self.gen.parse_options()
        self.assertFalse(self.gen.options.verbose)
        self.assertEqual(self.gen.options.input, "./obj/Dictionary_na.xml")
        self.assertEqual(self.gen.options.output, "na/py/Dictionary_na.txt")

    def test_trans_tones(self):
        # Monosyllabic nouns
        self.assertEqual(self.gen.trans_tones("LM", "n", 1), ["LH"])
        self.assertEqual(self.gen.trans_tones("LH", "n", 1), ["LH"])
        self.assertEqual(self.gen.trans_tones("M", "n", 1), ["M"])
        self.assertEqual(self.gen.trans_tones("L", "n", 1), ["M"])
        self.assertEqual(self.gen.trans_tones("#H", "n", 1), ["M"])
        self.assertEqual(self.gen.trans_tones("MH#", "n", 1), ["MH"])
        # Disyllabic nouns
        self.assertEqual(self.gen.trans_tones("M", "n", 2), ["M", "M"])
        self.assertEqual(self.gen.trans_tones("#H", "n", 2), ["M", "M"])
        self.assertEqual(self.gen.trans_tones("MH#", "n", 2), ["M", "MH"])
        self.assertEqual(self.gen.trans_tones("H$", "n", 2), ["M", "H"])
        self.assertEqual(self.gen.trans_tones("H#", "n", 2), ["M", "H"])
        self.assertEqual(self.gen.trans_tones("L", "n", 2), ["L", "LH"])
        self.assertEqual(self.gen.trans_tones("L#", "n", 2), ["M", "L"])
        self.assertEqual(self.gen.trans_tones("LM+MH#", "n", 2), ["L", "MH"])
        self.assertEqual(self.gen.trans_tones("LM+#H", "n", 2), ["L", "M"])
        self.assertEqual(self.gen.trans_tones("LM", "n", 2), ["L", "M"])
        self.assertEqual(self.gen.trans_tones("LH", "n", 2), ["L", "M"])

    def test_tones_to_analysis(self):
        # Monosyllabic nouns
        self.assertEqual(self.gen.tones_to_analysis(["LM"], "n"), "LM")
        self.assertEqual(self.gen.tones_to_analysis(["LH"], "n"), "LH")
        self.assertEqual(self.gen.tones_to_analysis(["M"], "n"), "M")
        self.assertEqual(self.gen.tones_to_analysis(["L"], "n"), "L")
        self.assertEqual(self.gen.tones_to_analysis(["H"], "n"), "#H")
        self.assertEqual(self.gen.tones_to_analysis(["MH"], "n"), "MH#")
        self.assertEqual(self.gen.tones_to_analysis(["LM"], "n"), "LM")
        # Disyllabic nouns
        self.assertEqual(self.gen.tones_to_analysis(["M", "M"], "n"), "M")
        self.assertEqual(self.gen.tones_to_analysis(["M", "#H"], "n"), "#H")
        self.assertEqual(self.gen.tones_to_analysis(["M", "MH"], "n"), "MH#")
        self.assertEqual(self.gen.tones_to_analysis(["M", "H$"], "n"), "H$")
        self.assertEqual(self.gen.tones_to_analysis(["M", "H"], "n"), "H#")
        self.assertEqual(self.gen.tones_to_analysis(["L", "L"], "n"), "L")
        self.assertEqual(self.gen.tones_to_analysis(["M", "L"], "n"), "L#")
        self.assertEqual(self.gen.tones_to_analysis(["L", "MH"], "n"), "LM+MH#")
        self.assertEqual(self.gen.tones_to_analysis(["L", "M"], "n"), "LM")
        self.assertEqual(self.gen.tones_to_analysis(["L", "H"], "n"), "LH")

    def test_lx_to_lc(self):
        # Monosyllabic nouns
        self.assertEqual(self.gen.lx_to_lc("bo˩˧", "n"), "bo˩˥")
        self.assertEqual(self.gen.lx_to_lc("ʐæ˩˥", "n"), "ʐæ˩˥")
        self.assertEqual(self.gen.lx_to_lc("lɑ˧", "n"), "lɑ˧")
        self.assertEqual(self.gen.lx_to_lc("jo˩", "n"), "jo˧")
        self.assertEqual(self.gen.lx_to_lc("ʐwæ˥", "n"), "ʐwæ˧")
        self.assertEqual(self.gen.lx_to_lc("ʈʂʰæ˧˥", "n"), "ʈʂʰæ˧˥")
        # Disyllabic nouns
        self.assertEqual(self.gen.lx_to_lc("σ˧ σ˧", "n"), "σ˧ σ˧")
        self.assertEqual(self.gen.lx_to_lc("po˧lo˧", "n"), "po˧lo˧")
        self.assertEqual(self.gen.lx_to_lc("σ˧ σ#˥", "n"), "σ˧ σ˧")
        self.assertEqual(self.gen.lx_to_lc("ʐwæ˧zo#˥", "n"), "ʐwæ˧zo˧")
        self.assertEqual(self.gen.lx_to_lc("σ˧ σ˧˥", "n"), "σ˧ σ˧˥")
        self.assertEqual(self.gen.lx_to_lc("hwɤ˧li˧˥", "n"), "hwɤ˧li˧˥")
        self.assertEqual(self.gen.lx_to_lc("σ˧ σ˥$", "n"), "σ˧ σ˥")
        self.assertEqual(self.gen.lx_to_lc("kv̩˧ʂe˥$", "n"), "kv̩˧ʂe˥")
        self.assertEqual(self.gen.lx_to_lc("σ˧ σ˥", "n"), "σ˧ σ˥")
        self.assertEqual(self.gen.lx_to_lc("hwæ˧ʈʂæ˥", "n"), "hwæ˧ʈʂæ˥")
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ˩", "n"), "σ˩ σ˩˥")
        self.assertEqual(self.gen.lx_to_lc("kʰv˩mi˩", "n"), "kʰv˩mi˩˥")
        self.assertEqual(self.gen.lx_to_lc("σ˧ σ˩", "n"), "σ˧ σ˩")
        self.assertEqual(self.gen.lx_to_lc("dɑ˧ʝi˩", "n"), "dɑ˧ʝi˩")
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ˧˥", "n"), "σ˩ σ˧˥")
        self.assertEqual(self.gen.lx_to_lc("õ˩dv˧˥", "n"), "õ˩dv˧˥")
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ#˥", "n"), "σ˩ σ˧")
        self.assertEqual(self.gen.lx_to_lc("nɑ˩hĩ#˥", "n"), "nɑ˩hĩ˧")
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ˧", "n"), "σ˩ σ˧")
        self.assertEqual(self.gen.lx_to_lc("bo˩mi˧", "n"), "bo˩mi˧")
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ˥", "n"), "σ˩ σ˧")
        self.assertEqual(self.gen.lx_to_lc("bo˩ɬɑ˥", "n"), "bo˩ɬɑ˧")
        # Checked with Alexis
        # Dictionary_na.txt
        self.assertEqual(self.gen.lx_to_lc("dze˩mi˧-kʰv˩", "n"), "dze˩mi˧-kʰv˩") # not "dze˩mi˧-kʰv˧"
        self.assertEqual(self.gen.lx_to_lc("dʑɯ˩-æ˩tsɯ˧", "n"), "dʑɯ˩-æ˩tsɯ˧") # not "dʑɯ˧-æ˩tsɯ˧"
        self.assertEqual(self.gen.lx_to_lc("dʑɯ˩pɤ˩-kv˧hĩ˩", "n"), "dʑɯ˩pɤ˩-kv˧hĩ˩") # not "dʑɯ˩pɤ˩˥-kv˧hĩ˩"
        self.assertEqual(self.gen.lx_to_lc("dʑɯ˩ʁo˩-hwɤ˩li˧", "n"), "dʑɯ˩ʁo˩-hwɤ˩li˧") # not "dʑɯ˩ʁo˩˥-hwɤ˩li˧"
        self.assertEqual(self.gen.lx_to_lc("ə˧ɲi˥-tsæ˩qæ˩", "n"), "ə˧ɲi˥-tsæ˩qæ˩") # not "ə˧ɲi˥-tsæ˩qæ˩˥"
        self.assertEqual(self.gen.lx_to_lc("ɣɯ˩-nɑ˧mi˩", "n"), "ɣɯ˩-nɑ˧mi˩") # not "ɣɯ˧-nɑ˧mi˩"
        self.assertEqual(self.gen.lx_to_lc("jɤ˩jo˧-bv#˥", "n"), "jɤ˩jo˧-bv˧") # OK
        # tone_errors.txt
        self.assertEqual(self.gen.lx_to_lc("lo˩qʰwɤ˧-kʰɯ˧ʑi˧˥", "n"), "lo˩qʰwɤ˧-kʰɯ˧ʑi˧˥") # LM+MH# => LM°MH#
        self.assertEqual(self.gen.lx_to_lc("lo˧ʂv˩-hi˩-nɑ˧mi˧", "n"), "lo˧ʂv˩-hi˩-nɑ˧mi˧")
        self.assertEqual(self.gen.lx_to_lc("ɬo˩tsʰe˩mæ˥", "n"), "ɬo˩tsʰe˩mæ˧")

    def test_dissect(self):
        pass

    def test_tone_str_to_ipa(self):
        pass

    def test_tone_ipa_to_str(self):
        pass

    def test_add_lc(self):
        pass

    def test_main(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerateLcFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
