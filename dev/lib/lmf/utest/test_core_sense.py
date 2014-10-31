#! /usr/bin/env python

from startup import *
from core.sense import Sense
from core.definition import Definition
from core.statement import Statement

## Test Sense class

class TestSenseFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Sense object
        self.sense = Sense()

    def tearDown(self):
        # Release instantiated objects
        del self.sense

    def test_init(self):
        self.assertIsNone(self.sense.senseNumber)
        self.assertEqual(self.sense.id, 0)
        self.assertListEqual(self.sense.definition, [])
        self.assertListEqual(self.sense.sense, [])
        self.assertListEqual(self.sense.equivalent, [])
        self.assertListEqual(self.sense.context, [])
        self.assertListEqual(self.sense.subject_field, [])
        self.assertListEqual(self.sense.paradigm, [])

    def test_get_id(self):
        self.assertIs(self.sense.get_id(), self.sense.id)

    def test_set_senseNumber(self):
        nb = 123
        self.assertIs(self.sense.set_senseNumber(nb), self.sense)
        self.assertEqual(self.sense.senseNumber, nb)

    def test_get_senseNumner(self):
        nb = 456
        self.sense.senseNumber = nb
        self.assertEqual(self.sense.get_senseNumber(), nb)

    def test_create_definition(self):
        # Test create definition
        definition = self.sense.create_definition()
        self.assertIsInstance(definition, Definition)
        # Release Definition instance
        del definition

    def test_add_definition(self):
        # Create definitions
        def1 = Definition()
        def2 = Definition()
        # Test add definitions to the sense
        self.assertIs(self.sense.add_definition(def1), self.sense)
        self.assertListEqual(self.sense.definition, [def1])
        self.assertIs(self.sense.add_definition(def2), self.sense)
        self.assertListEqual(self.sense.definition, [def1, def2])
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2

    def test_get_definitions(self):
        # List of Definition instances is empty
        self.assertListEqual(self.sense.get_definitions(), [])
        # Create Definition instances and add them to the list
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Test get definitions
        self.assertListEqual(self.sense.get_definitions(), [def1, def2])
        # Delete Definition instances
        del self.sense.definition[:]
        del def1, def2

    def test_get_last_definition(self):
        # List of Definition instances is empty
        self.assertIsNone(self.sense.get_last_definition())
        # Create Definition instances and add them to the list
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Test get last definition
        self.assertIs(self.sense.get_last_definition(), def2)
        self.sense.definition.pop()
        self.assertIs(self.sense.get_last_definition(), def1)
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2

    def test_find_definitions(self):
        # Create several definitions with different languages
        def1 = Definition().set_definition("def1").set_language("fra")
        def2 = Definition().set_definition("def2").set_language("eng")
        def3 = Definition().set_definition("def3").set_language("fra")
        def4 = Definition().set_definition("def4").set_language("srp")
        # Add definitions to the sense
        self.sense.definition = [def1, def2, def3, def4]
        # Test find definitions
        self.assertListEqual(self.sense.find_definitions("eng"), [def2.definition])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_definitions("fra")), set([def1.definition, def3.definition]))
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2, def3, def4

    def test_set_definition(self):
        definition = "#define"
        # There is no Definition instance
        self.assertIs(self.sense.set_definition(definition), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(self.sense.definition[0].definition, definition)
        # Test set a second definition
        language = "C++"
        self.assertIs(self.sense.set_definition(definition, language), self.sense)
        self.assertEqual(len(self.sense.definition), 2)
        self.assertEqual(self.sense.definition[1].definition, definition)
        self.assertEqual(self.sense.definition[1].language, language)

    def test_find_glosses(self):
        # Create several definitions with different glosses and languages
        def1 = Definition().set_gloss("DEF1").set_language("fra")
        def2 = Definition().set_gloss("DEF2").set_language("eng")
        def3 = Definition().set_gloss("DEF3").set_language("fra")
        def4 = Definition().set_gloss("DEF4").set_language("srp")
        # Add definitions to the sense
        self.sense.definition = [def1, def2, def3, def4]
        # Test find glosses
        self.assertListEqual(self.sense.find_glosses("eng"), [def2.gloss])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_glosses("fra")), set([def1.gloss, def3.gloss]))
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2, def3, def4

    def test_set_gloss(self):
        gloss = "GLOSS"
        # There is no Definition instance
        self.assertIs(self.sense.set_gloss(gloss), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(self.sense.definition[0].gloss, gloss)
        # Test set a second gloss
        language = "C++"
        self.assertIs(self.sense.set_gloss(gloss, language), self.sense)
        self.assertEqual(len(self.sense.definition), 2)
        self.assertEqual(self.sense.definition[1].gloss, gloss)
        self.assertEqual(self.sense.definition[1].language, language)

    def test_set_note(self):
        note = "note"
        # There is no Definition instance
        self.assertIs(self.sense.set_note(note), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].note, note)
        # Test set a second note
        language = "C++"
        self.assertIs(self.sense.set_note(note, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].note, note)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_notes(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different notes and types
        state1 = Statement().set_note("note1", "comparison")
        state2 = Statement().set_note("note2", "general")
        state3 = Statement().set_note("note3", "comparison")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find notes
        self.assertListEqual(self.sense.find_notes("general"), [state2.note])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_notes("comparison")), set([state1.note, state3.note]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
