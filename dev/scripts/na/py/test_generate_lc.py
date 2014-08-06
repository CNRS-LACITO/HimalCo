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

    def test_apply_rules(self):
        self.assertEqual(self.gen.apply_rules((0,), 1, ["L"]), ["M"])

    def test_apply_rule_0(self):
        self.assertEqual(self.gen.apply_rule_0(1, ["L"]), ["M"])

    def test_apply_rule_1(self):
        self.assertEqual(self.gen.apply_rule_1(4, ["L", "H"]), ["L", "L", "L", "H"])

    def test_apply_rule_2(self):
        pass

    def test_apply_rule_3(self):
        self.assertEqual(self.gen.apply_rule_3(2, ["H", "M"]), ["M", "M"])

    def test_apply_rule_4(self):
        self.assertEqual(self.gen.apply_rule_4(3, ["M", "H", "H"]), ["M", "H", "L"])

    def test_apply_rule_5(self):
        self.assertEqual(self.gen.apply_rule_5(3, ["M", "HL", "H"]), ["M", "HL", "L"])
        self.assertEqual(self.gen.apply_rule_5(3, ["ML", "M", "H"]), ["ML", "L", "L"])

    def test_apply_rule_6(self):
        self.assertEqual(self.gen.apply_rule_6(3, ["L", "L", "M"]), ["L", "L", "H"])

    def test_apply_rule_7(self):
        self.assertEqual(self.gen.apply_rule_7(3, ["L", "L", "L"]), ["L", "L", "LH"])

    def test_trans_tones(self):
        # Monosyllabic nouns
        self.assertEqual(self.gen.trans_tones("n", 1, ["LM"]), ["LH"])
        self.assertEqual(self.gen.trans_tones("n", 1, ["LH"]), ["LH"])
        self.assertEqual(self.gen.trans_tones("n", 1, ["M"]), ["M"])
        self.assertEqual(self.gen.trans_tones("n", 1, ["L"]), ["M"])
        self.assertEqual(self.gen.trans_tones("n", 1, ["H"]), ["M"])
        self.assertEqual(self.gen.trans_tones("n", 1, ["MH"]), ["MH"])
        # Disyllabic nouns
        self.assertEqual(self.gen.trans_tones("n", 2, ["M", "M"]), ["M", "M"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["M", "#H"]), ["M", "M"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["M", "MH"]), ["M", "MH"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["M", "H$"]), ["M", "H"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["M", "H"]), ["M", "H"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["L", "L"]), ["L", "LH"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["M", "L"]), ["M", "L"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["L", "MH"]), ["L", "MH"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["L", "#H"]), ["L", "M"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["L", "M"]), ["L", "H"])
        self.assertEqual(self.gen.trans_tones("n", 2, ["L", "H"]), ["L", "H"])

    def test_tones_to_analysis(self):
        # Monosyllabic nouns
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["LM"]), "LM")
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["LH"]), "LH")
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["M"]), "M")
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["L"]), "L")
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["H"]), "#H")
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["MH"]), "MH#")
        self.assertEqual(self.gen.tones_to_analysis("n", 1, ["LM"]), "LM")
        # Disyllabic nouns
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["M", "M"]), "M")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["M", "#H"]), "#H")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["M", "MH"]), "MH#")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["M", "H$"]), "H$")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["M", "H"]), "H#")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["L", "L"]), "L")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["M", "L"]), "L#")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["L", "MH"]), "LM+MH#")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["L", "M"]), "LM")
        self.assertEqual(self.gen.tones_to_analysis("n", 2, ["L", "H"]), "LH")

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
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ˧", "n"), "σ˩ σ˥")
        self.assertEqual(self.gen.lx_to_lc("bo˩mi˧", "n"), "bo˩mi˥")
        self.assertEqual(self.gen.lx_to_lc("σ˩ σ˥", "n"), "σ˩ σ˥")
        self.assertEqual(self.gen.lx_to_lc("bo˩ɬɑ˥", "n"), "bo˩ɬɑ˥")
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
