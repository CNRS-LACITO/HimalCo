#! /usr/bin/env python

"""! @package core
"""

from morphology.lemma import Lemma
from morphology.related_form import RelatedForm
from common.range import partOfSpeech_range
from utils.error_handling import Error
from config.mdf import ps_partOfSpeech

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
        self.independentWord = None # boolean
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
        # Check part of speech value
        if part_of_speech not in partOfSpeech_range:
            # Try with converted value from MDF to LMF
            try:
                ps_partOfSpeech[part_of_speech]
            except KeyError:
                raise Error("Part of speech value '%s' encountered for lexeme '%s' is not allowed" % (part_of_speech, self.get_lexeme()))
            else:
                self.partOfSpeech = ps_partOfSpeech[part_of_speech]
                return self
        self.partOfSpeech = part_of_speech
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

    def get_id(self):
        """! @brief Get Unique IDentifier.
        @return LexicalEntry attribute 'id'.
        """
        return self.id

    def set_lexeme(self, lexeme):
        """! @brief Set lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @param lexeme The lexeme to set.
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
        else:
            return None

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

    def get_speaker(self):
        """! @brief Get speaker.
        @return LexicalEntry private attribute '__speaker'.
        """
        return self.__speaker

    def get_definitions(self):
        pass

    def get_senses(self):
        pass

    def get_gloss(self, lang):
        pass
