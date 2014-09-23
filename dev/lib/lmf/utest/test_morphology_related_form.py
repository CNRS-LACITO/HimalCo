#! /usr/bin/env python

from startup import *
from morphology.related_form import RelatedForm
from core.lexical_entry import LexicalEntry

## Test RelatedForm class

class TestRelatedFormFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a RelatedForm object
        self.related_form = RelatedForm()

    def tearDown(self):
        # Release instantiated objects
        del self.related_form

    def test_init(self):
        self.assertIsNone(self.related_form.variantForm)
        self.assertIsNone(self.related_form.type)
        self.assertIsNone(self.related_form.semanticRelation)
        self.assertIsNone(self.related_form.get_lexical_entry())
        self.assertIsNone(self.related_form.targets)

    def test_set_semanticRelation(self):
        # Test error case
        test = False
        try:
            self.related_form.set_semanticRelation("whatever")
        except AttributeError:
            test = True
        self.assertTrue(test)
        # Test nominal case
        relation = "homonym"
        self.assertEqual(self.related_form.set_semanticRelation(relation), self.related_form)
        self.assertEqual(self.related_form.semanticRelation, relation)

    def test_get_semanticRelation(self):
        # Set semantic relation
        relation = "whatever"
        self.related_form.semanticRelation = relation
        # Test get semantic relation
        self.assertEqual(self.related_form.get_semanticRelation(), relation)

    def test_get_lexeme(self):
        # Set lexeme
        lexeme = "hello"
        self.related_form.targets = lexeme
        # Test get lexeme
        self.assertEqual(self.related_form.get_lexeme(), lexeme)

    def test_set_lexical_entry(self):
        # Create a lexical entry
        entry = LexicalEntry()
        # Test set lexical entry
        self.assertEqual(self.related_form.set_lexical_entry(entry), self.related_form)
        self.assertEqual(self.related_form.get_lexical_entry(), entry)
        # Test lexical entry modifications
        entry.lexeme = "toto"
        self.assertEqual(self.related_form.get_lexical_entry().lexeme, "toto")
        # Release lexical entry
        del entry

    def test_get_lexical_entry(self):
        # Set related LexicalEntry
        entry = LexicalEntry()
        self.related_form.set_lexical_entry(entry)
        # Test get lexical entry
        self.assertEqual(self.related_form.get_lexical_entry(), entry)
        # Test lexical entry modifications
        entry.lexeme = "toto"
        self.assertEqual(self.related_form.get_lexical_entry().lexeme, "toto")
        # Release lexical entry
        del entry

suite = unittest.TestLoader().loadTestsFromTestCase(TestRelatedFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
