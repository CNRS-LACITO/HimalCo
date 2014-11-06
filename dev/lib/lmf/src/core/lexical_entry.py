#! /usr/bin/env python

"""! @package core
"""

from morphology.lemma import Lemma
from morphology.related_form import RelatedForm
from common.range import partOfSpeech_range
from utils.error_handling import Error
from config.mdf import ps_partOfSpeech
from utils.attr import check_attr_type, check_attr_range
from core.sense import Sense

class LexicalEntry():
    """! "Lexical Entry is a class representing a lexeme in a given language and is a container for managing the Form and Sense classes. A Lexical Entry instance can contain one to many different forms and can have from zero to many different senses." (LMF)
    """
    def __init__(self, id=0):
        """! @brief Constructor.
        LexicalEntry instances are owned by Lexicon.
        @param id Unique IDentifier. If not provided, default value is 0.
        @return A LexicalEntry instance.
        """
        self.homonymNumber = None
        self.status = None
        self.date = None
        self.partOfSpeech = None
        self.independentWord = None
        self.bibliography = None
        ## UID is managed at the Lexicon level
        self.id = id
        ## Sense instances are owned by LexicalEntry
        # There is zero to many Sense instances per LexicalEntry
        self.sense = []
        ## Lemma instance is owned by LexicalEntry
        # There is one Lemma instance by LexicalEntry instance
        self.lemma = None # lemmatized form
        ## RelatedForm instances are owned by LexicalEntry
        # There is zero to many RelatedForm instances per LexicalEntry
        self.related_form = []
        ## WordForm instances are owned by LexicalEntry
        # There is zero to many WordForm instances per LexicalEntry
        self.word_form = []
        ## Stem instances are owned by LexicalEntry
        # There is zero to many Stem instances per LexicalEntry
        self.stem = [] # ordered list
        ## ListOfComponents instance is owned by LexicalEntry
        # There is zero or one ListOfComponents instance per LexicalEntry
        self.list_of_components = None
        # Speaker id
        self.targets = None
        ## Pointer to an existing Speaker
        # There is one Speaker pointer per LexicalEntry instance
        self.__speaker = None

    def __del__(self):
        """! @brief Destructor.
        Release Sense, Lemma, RelatedForm, WordForm, Stem, ListOfComponents instances.
        """
        for sense in self.sense:
            del sense
        del self.sense[:]
        for related_form in self.related_form:
            del related_form
        del self.related_form[:]
        for word_form in self.word_form:
            del word_form
        del self.word_form[:]
        for stem in self.stem:
            del stem
        del self.stem[:]
        if self.lemma is not None:
            del self.lemma
        if self.list_of_components is not None:
            del self.list_of_components
        # Decrement the reference count on pointed objects
        self.__speaker = None

    def set_partOfSpeech(self, part_of_speech):
        """! @brief Set grammatical category.
        @param part_of_speech The grammatical category to set.
        @return LexicalEntry instance.
        """
        error_msg = "Part of speech value '%s' encountered for lexeme '%s' is not allowed" % (str(part_of_speech), self.get_lexeme())
        # Check part of speech type
        check_attr_type(part_of_speech, [str, unicode], error_msg)
        # Check range of part of speech value (also try with converted value from MDF to LMF)
        value = check_attr_range(part_of_speech, partOfSpeech_range, error_msg, mapping=ps_partOfSpeech)
        self.partOfSpeech = value
        return self

    def get_partOfSpeech(self):
        """! @brief Get grammatical category.
        @return LexicalEntry attribute 'partOfSpeech'.
        """
        return self.partOfSpeech

    def set_status(self, status):
        """! @brief Set lexical entry status.
        @param status The status to set.
        @return LexicalEntry instance.
        """
        self.status = status
        return self

    def get_status(self):
        """! @brief Get lexical entry status.
        @return LexicalEntry attribute 'status'.
        """
        return self.status

    def set_date(self, date):
        """! @brief Set lexical entry date.
        @param status The date to set.
        @return LexicalEntry instance.
        """
        self.date = date
        return self

    def get_date(self):
        """! @brief Get lexical entry date.
        @return LexicalEntry attribute 'date'.
        """
        return self.date

    def set_homonymNumber(self, homonym_number):
        """! @brief Set lexical entry homonym number.
        @param homonym_number The homonym number to set.
        @return LexicalEntry instance.
        """
        self.homonymNumber = homonym_number
        return self

    def get_homonymNumber(self):
        """! @brief Get lexical entry homonym number.
        @return LexicalEntry attribute 'homonymNumber'.
        """
        return self.homonymNumber

    def set_bibliography(self, bibliography):
        """! @brief Set lexical entry bibliography.
        @param bibliography The bibliography to set.
        @return LexicalEntry instance.
        """
        self.bibliography = bibliography
        return self

    def get_bibliography(self):
        """! @brief Get lexical entry bibliography.
        @return LexicalEntry attribute 'bibliography'.
        """
        return self.bibliography

    def set_independentWord(self, independent_word):
        """! @brief Set lexical entry independent word indication.
        @param independent_word The independent word indication to set.
        @return LexicalEntry instance.
        """
        error_msg = "Independent word '%s' encountered for lexeme '%s' is not allowed" % (str(independent_word), self.get_lexeme())
        check_attr_type(independent_word, bool, error_msg)
        self.independentWord = independent_word
        return self

    def get_independentWord(self):
        """! @brief Get lexical entry independent word indication.
        @return LexicalEntry attribute 'independentWord'.
        """
        return self.independentWord

    def get_id(self):
        """! @brief Get Unique IDentifier.
        @return LexicalEntry attribute 'id'.
        """
        return self.id

    def set_lexeme(self, lexeme):
        """! @brief Set lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @param lexeme The lexeme to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_lexeme(lexeme)
        return self

    def get_lexeme(self):
        """! @brief Get lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @return Lemma attribute 'lexeme' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_lexeme()

    def create_related_form(self, lexeme, semantic_relation):
        """! @brief Create a related form.
        @param lexeme Related lexeme.
        @param semantic_relation The semantic relation existing between this lexical entry and the related lexeme to create.
        @return RelatedForm instance.
        """
        return RelatedForm(lexeme).set_semanticRelation(semantic_relation)

    def add_related_form(self, related_form):
        """! @brief Add a related form to the lexical entry.
        @param related_form The RelatedForm instance to add to the lexical entry.
        @return LexicalEntry instance.
        """
        self.related_form.append(related_form)
        return self

    def create_and_add_related_form(self, lexeme, semantic_relation):
        """! @brief Create and add a related form to the lexical entry.
        @param lexeme Related lexeme.
        @param semantic_relation The semantic relation existing between this lexical entry and the related lexeme to create.
        @return LexicalEntry instance.
        """
        self.related_form.append(RelatedForm(lexeme).set_semanticRelation(semantic_relation))
        return self

    def find_related_forms(self, semantic_relation):
        """! @brief Find related lexemes.
        This attribute is owned by RelatedForm.
        @param semantic_relation The semantic relation to consider to retrieve the related form.
        @return A Python list of found RelatedForm attributes 'targets'.
        """
        found_forms = []
        for related_form in self.get_related_forms():
            if related_form.get_semanticRelation() == semantic_relation:
                found_forms.append(related_form.get_lexeme())
        return found_forms

    def get_related_forms(self):
        """! @brief Get all related forms maintained by the lexical entry.
        @return A Python set of related forms.
        """
        # Create a set without duplicates
        return set(self.related_form)

    def get_form_representations(self):
        """! @brief Get all form representations maintained by the lemma.
        Attribute 'form_representation' is owned by Lemma.
        @return Lemma attribute 'form_representation' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_form_representations()

    def set_variant_form(self, variant_form, type="unspecified"):
        """! @brief Set variant form and type.
        Attributes 'variantForm' and 'type' are owned by FormRepresentation, which is owned by Lemma.
        @param variant_form Variant form.
        @param type Type of variant, in range 'type_variant_range' defined in 'common/range.py'.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_variant_form(variant_form, type)
        return self

    def set_variant_comment(self, comment, language=None):
        """! @brief Set variant comment and language.
        Attributes 'comment' and 'language' are owned by FormRepresentation, which is owned by Lemma.
        @param comment Variant comment.
        @param language Language of comment.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_variant_comment(comment, language)
        return self

    def set_tone(self, tone):
        """! @brief Set tone.
        Attribute 'tone' is owned by FormRepresentation, which is owned by Lemma.
        @param tone The tone to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_tone(tone)
        return self

    def get_tones(self):
        """! @brief Get all tones.
        Attribute 'tone' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'tone' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_tones()

    def set_geographical_variant(self, geographical_variant):
        """! @brief Set geographical variant.
        Attribute 'geographicalVariant' is owned by FormRepresentation, which is owned by Lemma.
        @param geographical_variant The geographical variant to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_geographical_variant(geographical_variant)
        return self

    def set_phonetic_form(self, phonetic_form):
        """! @brief Set phonetic form.
        Attribute 'phoneticForm' is owned by FormRepresentation, which is owned by Lemma.
        @param phonetic_form The phonetic form to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_phonetic_form(phonetic_form)
        return self

    def get_phonetic_forms(self):
        """! @brief Get all phonetic forms.
        Attribute 'phoneticForm' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'phoneticForm' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_phonetic_forms()

    def set_contextual_variation(self, contextual_variation):
        """! @brief Set contextual variation.
        Attribute 'contextualVariation' is owned by FormRepresentation, which is owned by Lemma.
        @param contextual_variation The contextual variation to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_contextual_variation(contextual_variation)
        return self

    def get_contextual_variations(self):
        """! @brief Get all contextual variations.
        Attribute 'contextualVariation' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'contextualVariation' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_contextual_variations()

    def set_spelling_variant(self, spelling_variant):
        """! @brief Set spelling variant.
        Attribute 'spellingVariant' is owned by FormRepresentation, which is owned by Lemma.
        @param spelling_variant The spelling variant to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_spelling_variant(spelling_variant)
        return self

    def set_citation_form(self, citation_form):
        """! @brief Set citation form.
        Attribute 'citationForm' is owned by FormRepresentation, which is owned by Lemma.
        @param citation_form The citation form to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_citation_form(citation_form)
        return self

    def get_citation_forms(self):
        """! @brief Get all citation forms.
        Attribute 'citationForm' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'citationForm' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_citation_forms()

    def set_dialect(self, dialect):
        """! @brief Set dialect.
        Attribute 'dialect' is owned by FormRepresentation, which is owned by Lemma.
        @param dialect The dialect to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_dialect(dialect)
        return self

    def set_transliteration(self, transliteration):
        """! @brief Set transliteration.
        Attribute 'transliteration' is owned by FormRepresentation, which is owned by Lemma.
        @param transliteration The transliteration to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_transliteration(transliteration)
        return self

    def get_transliterations(self):
        """! @brief Get all transliterations.
        Attribute 'transliteration' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'transliteration' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_transliterations()

    def set_script_name(self, script_name):
        """! @brief Set script name.
        Attribute 'scriptName' is owned by FormRepresentation, which is owned by Lemma.
        @param script_name The script name to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_script_name(script_name)
        return self

    def create_sense(self, id=0):
        """! @brief Create a sense.
        @param id Identifier.
        @return Sense instance.
        """
        return Sense(id)

    def add_sense(self, sense):
        """! @brief Add a sense to the lexical entry.
        @param sense The Sense instance to add to the lexical entry.
        @return LexicalEntry instance.
        """
        self.sense.append(sense)
        return self

    def create_and_add_sense(self, sense_number):
        """! @brief Create and add a sense to the lexical entry.
        @param sense_number Number of the sense to add.
        @return LexicalEntry instance.
        """
        id = str(self.get_id()) + "_" + str(sense_number)
        self.add_sense(self.create_sense(id).set_senseNumber(sense_number))
        return self

    def get_senses(self):
        """! @brief Get all senses maintained by the lexical entry.
        @return LexicalEntry attribute 'sense'.
        """
        return self.sense

    def get_last_sense(self):
        """! @brief Get the previously registered sense.
        @return The last element of LexicalEntry attribute 'sense'.
        """
        if len(self.get_senses()) >= 1:
            return self.get_senses()[-1]

    def set_definition(self, definition, language=None):
        """! @brief Set definition and language.
        Attributes 'definition' and 'language' are owned by Definition, which is owned by Sense.
        @param definition Definition.
        @param language Language of definition.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_definition(definition, language)
        return self

    def set_gloss(self, gloss, language=None):
        """! @brief Set gloss and language.
        Attributes 'gloss' and 'language' are owned by Definition, which is owned by Sense.
        @param gloss Gloss.
        @param language Language of gloss.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_gloss(gloss, language)
        return self

    def set_note(self, note, type=None, language=None):
        """! @brief Set note, type and language.
        Attributes 'note', 'noteType' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param note Note to set.
        @param type Type of the note.
        @param language Language of the note.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_note(note, type, language)
        return self

    def find_notes(self, type):
        """! @brief Find notes.
        This attribute is owned by Statement, which owned by Definition, itself owned by Sense.
        @param type Type of the note to consider to retrieve the note.
        @return A Python list of found Statement attributes 'notes'.
        """
        found_notes = []
        for sense in self.get_senses():
            found_notes += sense.find_notes(type)
        return found_notes

    def set_usage_note(self, usage_note, language=None):
        """! @brief Set usage note and language.
        Attributes 'usageNote' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param usage_note Usage note to set.
        @param language Language of the usage note.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_usage_note(usage_note, language)
        return self

    def set_encyclopedic_information(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information and language.
        Attributes 'encyclopedicInformation' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language of the encyclopedic information.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_encyclopedic_information(encyclopedic_information, language)
        return self

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction and language.
        Attributes 'restriction' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param restriction Restriction to set.
        @param language Language of the restriction.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_restriction(restriction, language)
        return self

    def set_borrowed_word(self, borrowed_word):
        """! @brief Set source language (in English).
        Attribute 'borrowedWord' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param borrowed_word Source language.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_borrowed_word(borrowed_word)
        return self

    def get_borrowed_word(self):
        """! @brief Get source language (in English).
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'borrowedWord'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get source language
        if sense is not None:
            return sense.get_borrowed_word()

    def set_written_form(self, written_form):
        """! @brief Set loan word.
        Attribute 'writtenForm' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param written_form Loan word.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_written_form(written_form)
        return self

    def get_written_form(self):
        """! @brief Get loan word.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'writtenForm'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get loan word
        if sense is not None:
            return sense.get_written_form()

    def set_etymology(self, etymology):
        """! @brief Set etymology.
        Attribute 'etymology' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology Etymology.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology(etymology)
        return self

    def get_etymology(self):
        """! @brief Get etymology.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'etymology'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology
        if sense is not None:
            return sense.get_etymology()

    def set_etymology_comment(self, etymology_comment, term_source_language=None):
        """! @brief Set etymology comment and language.
        Attributes 'etymologyComment' and 'termSourceLanguage' are owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology_comment Etymology comment.
        @param term_source_language Language of the comment.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology_comment(etymology_comment, term_source_language)
        return self

    def get_etymology_comment(self, term_source_language=None):
        """! @brief Get etymology comment.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param term_source_language The language of the etymology comment to retrieve.
        @return Statement attribute 'etymologyComment'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology comment
        if sense is not None:
            return sense.get_etymology_comment(term_source_language)

    def get_term_source_language(self):
        """! @brief Get language used for the etymology comment.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'termSourceLanguage'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology comment language
        if sense is not None:
            return sense.get_term_source_language()

    def set_etymology_gloss(self, etymology_gloss):
        """! @brief Set etymology gloss.
        Attribute 'etymologyGloss' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology_gloss Etymology gloss.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology_gloss(etymology_gloss)
        return self

    def get_etymology_gloss(self):
        """! @brief Get etymology gloss.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'etymologyGloss'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology gloss
        if sense is not None:
            return sense.get_etymology_gloss()

    def set_etymology_source(self, etymology_source):
        """! @brief Set etymology source.
        Attribute 'etymologySource' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology_source Etymology source.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology_source(etymology_source)
        return self

    def get_etymology_source(self):
        """! @brief Get etymology source.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'etymologySource'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology source
        if sense is not None:
            return sense.get_etymology_source()

    def get_speaker(self):
        """! @brief Get speaker.
        @return LexicalEntry private attribute '__speaker'.
        """
        return self.__speaker
