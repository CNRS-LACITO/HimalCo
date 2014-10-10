#! /usr/bin/env python

from startup import *
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from morphology.related_form import RelatedForm
from utils.error_handling import Error

## Test LexicalEntry class

class TestLexicalEntryFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a LexicalEntry object
        self.lexical_entry = LexicalEntry()

    def tearDown(self):
        # Release instantiated objects
        del self.lexical_entry

    def test_init(self):
        self.assertIsNone(self.lexical_entry.homonymNumber)
        self.assertIsNone(self.lexical_entry.status)
        self.assertIsNone(self.lexical_entry.date)
        self.assertIsNone(self.lexical_entry.partOfSpeech)
        self.assertIsNone(self.lexical_entry.independentWord)
        self.assertIsNone(self.lexical_entry.bibliography)
        self.assertEqual(self.lexical_entry.id, 0)
        self.assertListEqual(self.lexical_entry.sense, [])
        self.assertIsNone(self.lexical_entry.lemma)
        self.assertListEqual(self.lexical_entry.related_form, [])
        self.assertListEqual(self.lexical_entry.word_form, [])
        self.assertListEqual(self.lexical_entry.stem, [])
        self.assertIsNone(self.lexical_entry.list_of_components)
        self.assertIsNone(self.lexical_entry.targets)
        self.assertIsNone(self.lexical_entry.get_speaker())

    def test_set_partOfSpeech(self):
        part_of_speech = "verb"
        self.assertEqual(self.lexical_entry.set_partOfSpeech(part_of_speech), self.lexical_entry)
        self.assertEqual(self.lexical_entry.partOfSpeech, part_of_speech)
        # Test error case
        test = False
        try:
            self.lexical_entry.set_partOfSpeech("whatever")
        except Error:
            test = True
        self.assertTrue(test)

    def test_get_partOfSpeech(self):
        self.assertIs(self.lexical_entry.get_partOfSpeech(), self.lexical_entry.partOfSpeech)

    def test_set_status(self):
        status = "draft"
        self.assertEqual(self.lexical_entry.set_status(status), self.lexical_entry)
        self.assertEqual(self.lexical_entry.status, status)

    def test_get_status(self):
        self.assertIs(self.lexical_entry.get_status(), self.lexical_entry.status)

    def test_set_date(self):
        date = "2014-06-15"
        self.assertEqual(self.lexical_entry.set_date(date), self.lexical_entry)
        self.assertEqual(self.lexical_entry.date, date)

    def test_get_date(self):
        self.assertIs(self.lexical_entry.get_date(), self.lexical_entry.date)

    def test_get_id(self):
        self.assertIs(self.lexical_entry.get_id(), self.lexical_entry.id)

    def test_set_lexeme(self):
        lexeme = "hello"
        self.assertEqual(self.lexical_entry.set_lexeme(lexeme), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.lexeme, lexeme)

    def test_get_lexeme(self):
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_lexeme())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        self.assertEqual(self.lexical_entry.get_lexeme(), self.lexical_entry.lemma.lexeme)
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_create_related_form(self):
        lexeme = "form"
        relation = "homonym"
        # Test create related form
        form = self.lexical_entry.create_related_form(lexeme, relation)
        self.assertEqual(form.targets, lexeme)
        self.assertEqual(form.semanticRelation, relation)
        # Release RelatedForm instance
        del form

    def test_add_related_form(self):
        # Create related forms
        form1 = RelatedForm("form1")
        form2 = RelatedForm("form2")
        # Test add related forms to the lexical entry
        self.assertEqual(self.lexical_entry.add_related_form(form1), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.related_form, [form1])
        self.assertEqual(self.lexical_entry.related_form[0].targets, "form1")
        self.assertEqual(self.lexical_entry.add_related_form(form2), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.related_form, [form1, form2])
        self.assertEqual(self.lexical_entry.related_form[1].targets, "form2")
        # Release RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2

    def test_create_and_add_related_form(self):
        # Test create and add related forms to the lexical entry
        lexeme = "form1"
        relation = "homonym"
        self.assertEqual(self.lexical_entry.create_and_add_related_form(lexeme, relation), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.related_form), 1)
        self.assertEqual(self.lexical_entry.related_form[0].targets, lexeme)
        lexeme = "form2"
        relation = "derived form"
        self.assertEqual(self.lexical_entry.create_and_add_related_form(lexeme, relation), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.related_form), 2)
        self.assertEqual(self.lexical_entry.related_form[1].targets, lexeme)
        # Release RelatedForm instances
        del self.lexical_entry.related_form[1], self.lexical_entry.related_form[0]

    def test_find_related_forms(self):
        # Create several related forms with different semantic relations
        form1 = RelatedForm().set_semanticRelation("synonym")
        form2 = RelatedForm().set_semanticRelation("antonym")
        form3 = RelatedForm().set_semanticRelation("synonym")
        form4 = RelatedForm().set_semanticRelation("simple link")
        # Add related forms to the lexical entry
        self.lexical_entry.related_form = [form1, form2, form3, form4]
        # Test find related forms
        self.assertListEqual(self.lexical_entry.find_related_forms("antonym"), [form2.targets])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.lexical_entry.find_related_forms("synonym")), set([form1.targets, form3.targets]))
        # Release RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2, form3, form4

    def test_get_related_forms(self):
        # List of RelatedForm instances is empty
        self.assertEqual(self.lexical_entry.get_related_forms(), set([]))
        # Create RelatedForm instances and add them to the list
        form1 = RelatedForm()
        form2 = RelatedForm()
        self.lexical_entry.related_form = [form1, form2]
        # Test get related forms
        self.assertEqual(self.lexical_entry.get_related_forms(), set([form1, form2]))
        self.lexical_entry.related_form.append(form1)
        self.assertEqual(self.lexical_entry.get_related_forms(), set([form1, form2]))
        # Delete RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2

    def test_get_definitions(self):
        pass

    def test_get_senses(self):
        pass

    def test_get_gloss(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalEntryFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
