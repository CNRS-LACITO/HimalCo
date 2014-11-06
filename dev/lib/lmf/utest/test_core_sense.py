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

    def test_set_usage_note(self):
        note = "note"
        # There is no Definition instance
        self.assertIs(self.sense.set_usage_note(note), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].usageNote, note)
        # Test set a second usage note
        language = "C++"
        self.assertIs(self.sense.set_usage_note(note, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].usageNote, note)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_usage_notes(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different usage notes and languages
        state1 = Statement().set_usageNote("note1", "eng")
        state2 = Statement().set_usageNote("note2", "fra")
        state3 = Statement().set_usageNote("note3", "eng")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find usage notes
        self.assertListEqual(self.sense.find_usage_notes("fra"), [state2.usageNote])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_usage_notes("eng")), set([state1.usageNote, state3.usageNote]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_encyclopedic_information(self):
        info = "encyclopedic"
        # There is no Definition instance
        self.assertIs(self.sense.set_encyclopedic_information(info), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].encyclopedicInformation, info)
        # Test set a second encyclopedic information
        language = "C++"
        self.assertIs(self.sense.set_encyclopedic_information(info, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].encyclopedicInformation, info)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_encyclopedic_informations(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different encyclopedic informations and languages
        state1 = Statement().set_encyclopedicInformation("info1", "eng")
        state2 = Statement().set_encyclopedicInformation("info2", "fra")
        state3 = Statement().set_encyclopedicInformation("info3", "eng")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find encyclopedic informations
        self.assertListEqual(self.sense.find_encyclopedic_informations("fra"), [state2.encyclopedicInformation])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_encyclopedic_informations("eng")), set([state1.encyclopedicInformation, state3.encyclopedicInformation]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_restriction(self):
        only = "restriction"
        # There is no Definition instance
        self.assertIs(self.sense.set_restriction(only), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].restriction, only)
        # Test set a second restriction
        language = "C++"
        self.assertIs(self.sense.set_restriction(only, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].restriction, only)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_restrictions(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different restrictions and languages
        state1 = Statement().set_restriction("only1", "eng")
        state2 = Statement().set_restriction("only2", "fra")
        state3 = Statement().set_restriction("only3", "eng")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find restrictions
        self.assertListEqual(self.sense.find_restrictions("fra"), [state2.restriction])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_restrictions("eng")), set([state1.restriction, state3.restriction]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_borrowed_word(self):
        word = "borrowed"
        # There is no Definition instance
        self.assertIs(self.sense.set_borrowed_word(word), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].borrowedWord, word)

    def test_get_borrowed_word(self):
        word = "borrowed"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set borrowed word
        self.sense.definition[0].statement[0].borrowedWord = word
        # Test get borrowed word
        self.assertEqual(self.sense.get_borrowed_word(), word)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_writtenForm(self):
        form = "written"
        # There is no Definition instance
        self.assertIs(self.sense.set_written_form(form), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].writtenForm, form)

    def test_get_writtenForm(self):
        form = "written"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set written form
        self.sense.definition[0].statement[0].writtenForm = form
        # Test get written form
        self.assertEqual(self.sense.get_written_form(), form)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology(self):
        etymology = "etymology"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology(etymology), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymology, etymology)

    def test_get_etymology(self):
        etymology = "etymology"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymology = etymology
        # Test get etymology
        self.assertEqual(self.sense.get_etymology(), etymology)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology_comment(self):
        # Test etymology comment only
        comment = "etymology"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology_comment(comment), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymologyComment, comment)
        # Test etymology comment and language
        commentaire = "etymologie"
        langage = "fra"
        self.assertIs(self.sense.set_etymology_comment(commentaire, term_source_language=langage), self.sense)
        self.assertEqual(self.sense.definition[0].statement[0].etymologyComment, commentaire)
        self.assertEqual(self.sense.definition[0].statement[0].termSourceLanguage, langage)

    def test_get_etymology_comment(self):
        comment = "etymology"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymologyComment = comment
        # Test get etymology
        self.assertEqual(self.sense.get_etymology_comment(), comment)
        # Test with a language filter
        language = "eng"
        self.sense.definition[0].statement[0].termSourceLanguage = language
        self.assertIsNone(self.sense.get_etymology_comment(term_source_language="fra"))
        self.assertEqual(self.sense.get_etymology_comment(term_source_language=language), comment)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology_gloss(self):
        gloss = "GLOSS"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology_gloss(gloss), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymologyGloss, gloss)

    def test_get_etymology_gloss(self):
        gloss = "GLOSS"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymologyGloss = gloss
        # Test get etymology
        self.assertEqual(self.sense.get_etymology_gloss(), gloss)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology_source(self):
        source = "etymology"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology_source(source), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymologySource, source)

    def test_get_etymology_source(self):
        source = "etymology"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymologySource = source
        # Test get etymology
        self.assertEqual(self.sense.get_etymology_source(), source)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
