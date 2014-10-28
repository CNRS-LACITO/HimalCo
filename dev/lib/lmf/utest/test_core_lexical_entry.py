#! /usr/bin/env python

from startup import *
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from morphology.related_form import RelatedForm
from utils.error_handling import Error
from core.form_representation import FormRepresentation
from core.sense import Sense

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

    def test_set_homonymNumber(self):
        nb = "3"
        self.assertEqual(self.lexical_entry.set_homonymNumber(nb), self.lexical_entry)
        self.assertEqual(self.lexical_entry.homonymNumber, nb)

    def test_get_homonymNumber(self):
        self.assertIs(self.lexical_entry.get_homonymNumber(), self.lexical_entry.homonymNumber)

    def test_set_bibliography(self):
        biblio = "212"
        self.assertEqual(self.lexical_entry.set_bibliography(biblio), self.lexical_entry)
        self.assertEqual(self.lexical_entry.bibliography, biblio)

    def test_get_bibliography(self):
        self.assertIs(self.lexical_entry.get_bibliography(), self.lexical_entry.bibliography)

    def test_set_independentWord(self):
        self.assertEqual(self.lexical_entry.set_independentWord(False), self.lexical_entry)
        self.assertFalse(self.lexical_entry.independentWord)
        # Test error case
        test = False
        try:
            self.lexical_entry.set_independentWord("whatever")
        except Error:
            test = True
        self.assertTrue(test)

    def test_get_independentWord(self):
        self.assertIs(self.lexical_entry.get_independentWord(), self.lexical_entry.independentWord)

    def test_get_id(self):
        self.assertIs(self.lexical_entry.get_id(), self.lexical_entry.id)

    def test_set_lexeme(self):
        lexeme = "hello"
        self.assertIs(self.lexical_entry.set_lexeme(lexeme), self.lexical_entry)
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
        self.assertIs(self.lexical_entry.add_related_form(form1), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.related_form, [form1])
        self.assertEqual(self.lexical_entry.related_form[0].targets, "form1")
        self.assertIs(self.lexical_entry.add_related_form(form2), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.related_form, [form1, form2])
        self.assertEqual(self.lexical_entry.related_form[1].targets, "form2")
        # Release RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2

    def test_create_and_add_related_form(self):
        # Test create and add related forms to the lexical entry
        lexeme = "form1"
        relation = "homonym"
        self.assertIs(self.lexical_entry.create_and_add_related_form(lexeme, relation), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.related_form), 1)
        self.assertEqual(self.lexical_entry.related_form[0].targets, lexeme)
        lexeme = "form2"
        relation = "derived form"
        self.assertIs(self.lexical_entry.create_and_add_related_form(lexeme, relation), self.lexical_entry)
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

    def test_get_form_representations(self):
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_form_representations())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get form representations
        self.assertListEqual(self.lexical_entry.get_form_representations(), [repr1, repr2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_variant_form(self):
        form = "form"
        type = "archaic"
        self.assertIs(self.lexical_entry.set_variant_form(form, type), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].variantForm, form)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].type, type)

    def test_set_variant_comment(self):
        comment = "comment"
        lang = "lang"
        self.assertIs(self.lexical_entry.set_variant_comment(comment, lang), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].comment, comment)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].language, lang)

    def test_set_tone(self):
        tone = "tone"
        self.assertIs(self.lexical_entry.set_tone(tone), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].tone, tone)

    def test_get_tones(self):
        tone1 = "My tone."
        tone2 = "Another tone."
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_tones())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.tone = tone1
        repr2 = FormRepresentation()
        repr2.tone = tone2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get tones
        self.assertListEqual(self.lexical_entry.get_tones(), [tone1, tone2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_geographical_variant(self):
        geo = "geo"
        self.assertIs(self.lexical_entry.set_geographical_variant(geo), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].geographicalVariant, geo)

    def test_set_phonetic_form (self):
        form = "form"
        self.assertIs(self.lexical_entry.set_phonetic_form(form), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].phoneticForm, form)

    def test_get_phonetic_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_phonetic_forms())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.phoneticForm = form1
        repr2 = FormRepresentation()
        repr2.phoneticForm = form2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get phonetic forms
        self.assertListEqual(self.lexical_entry.get_phonetic_forms(), [form1, form2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_contextual_variation(self):
        ctx = "ctx"
        self.assertIs(self.lexical_entry.set_contextual_variation(ctx), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].contextualVariation, ctx)

    def test_get_contextual_variations(self):
        ctx1 = "ctx1"
        ctx2 = "ctx2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_contextual_variations())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.contextualVariation = ctx1
        repr2 = FormRepresentation()
        repr2.contextualVariation = ctx2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get contextual variations
        self.assertListEqual(self.lexical_entry.get_contextual_variations(), [ctx1, ctx2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_spelling_variant(self):
        var = "var"
        self.assertIs(self.lexical_entry.set_spelling_variant(var), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].spellingVariant, var)

    def test_set_citation_form(self):
        form = "form"
        self.assertIs(self.lexical_entry.set_citation_form(form), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].citationForm, form)

    def test_get_citation_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_citation_forms())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.citationForm = form1
        repr2 = FormRepresentation()
        repr2.citationForm = form2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get citations forms
        self.assertListEqual(self.lexical_entry.get_citation_forms(), [form1, form2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_dialect(self):
        dial = "dial"
        self.assertIs(self.lexical_entry.set_dialect(dial), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].dialect, dial)

    def test_set_transliteration(self):
        trans = "trans"
        self.assertIs(self.lexical_entry.set_transliteration(trans), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].transliteration, trans)

    def test_get_transliterations(self):
        trans1 = "trans1"
        trans2 = "trans2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_transliterations())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.transliteration = trans1
        repr2 = FormRepresentation()
        repr2.transliteration = trans2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get transliterations
        self.assertListEqual(self.lexical_entry.get_transliterations(), [trans1, trans2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_script_name(self):
        script = "script"
        self.assertIs(self.lexical_entry.set_script_name(script), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].scriptName, script)

    def test_create_and_add_sense(self):
        # Test create and add senses to the lexical entry
        nb1 = "1"
        self.assertIs(self.lexical_entry.create_and_add_sense(nb1), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(self.lexical_entry.sense[0].id, "0_1")
        # Test with an identifier
        self.lexical_entry.id = "form"
        nb2 = 22
        self.assertIs(self.lexical_entry.create_and_add_sense(nb2), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 2)
        self.assertEqual(self.lexical_entry.sense[1].id, "form_22")
        # Release Sense instances
        del self.lexical_entry.sense[1], self.lexical_entry.sense[0]

    def test_get_senses(self):
        # List of Sense instances is empty
        self.assertListEqual(self.lexical_entry.get_senses(), [])
        # Create Sense instances and add them to the list
        sens1 = Sense()
        sens2 = Sense()
        self.lexical_entry.sense = [sens1, sens2]
        # Test get senses
        self.assertListEqual(self.lexical_entry.get_senses(), [sens1, sens2])
        # Delete Sense instances
        del self.lexical_entry.sense[:]
        del sens1, sens2

    def test_get_definitions(self):
        pass

    def test_get_gloss(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalEntryFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
