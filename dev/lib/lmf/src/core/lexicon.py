#! /usr/bin/env python

"""! @package core
"""

class Lexicon():
    """! "Lexicon is a class containing all the lexical entries of a given language within the entire resource." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Lexicon instances are owned by LexicalResource.
        @return A Lexicon instance.
        """
        self.language = None
        self.languageScript = None
        self.id = None
        self.label = None
        self.lexiconType = None
        self.entrySource = None
        self.vowelHarmony = None
        ## All LexicalEntry instances are maintained by Lexicon
        # There is one or more LexicalEntry instances per Lexicon
        self.lexical_entry = []

    def get_lexical_entries(self):
        """! @brief Get all lexical entries maintained by the lexicon.
        @return A Python set of lexical entries.
        """
        # Create a set without duplicates
        return set(self.lexical_entry)

    def add_lexical_entry(self, lexical_entry):
        """! @brief Add a lexical entry to the lexicon.
        @param lexical_entry A LexicalEntry instance to add to the Lexicon.
        @return Lexicon instance.
        """
        self.lexical_entry.append(lexical_entry)
        return self

    def remove_lexical_entry(self, lexical_entry):
        """! @brief Remove a lexical entry from the lexicon.
        @param lexical_entry The LexicalEntry instance to remove from the Lexicon.
        @return Lexicon instance.
        """
        self.lexical_entry.remove(lexical_entry)
        return self

    def count_lexical_entries(self):
        """! @brief Count number of lexical entries of the lexicon.
        @return The number of lexical entries without duplicates maintained by the lexicon.
        """
        return len(self.get_lexical_entries())

    def sort_lexical_entries(self, items=lambda lexical_entry: lexical_entry.get_lexeme(), order=None):
        """! @brief Sort given items of lexical entries contained in the lexicon according to a certain order.
        @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
        @param order Default value is 'None', which means that the lexicographical ordering uses the ASCII ordering.
        @return The sorted Python list of lexical entries.
        """
        # Create a list of tuples associating items and their lexical entries: [(item1, entry1), (item2, entry2), ...]
        items_and_entries = [(items(lexical_entry), lexical_entry) for lexical_entry in self.lexical_entry]
        if order is None:
            # Sort given items in alphabetical order
            items_and_entries.sort()
            # Retrieve lexical entries to create a sorted list
            sorted_entries = [item_and_entry[1] for item_and_entry in items_and_entries]
            return sorted_entries
        else:
            # TODO
            return self.lexical_entry

    def find_lexical_entries(self, filter):
        """! @brief Find all lexical entries which characteristics meet the given condition.
        @param filter Function or lambda function taking a lexical entry as argument, and returning True or False; for instance 'lambda lexical_entry: lexical_entry.get_lexeme() == "Hello"'.
        @return A Python list of LexicalEntry instances.
        """
        lexical_entries = []
        for lexical_entry in self.get_lexical_entries():
            if filter(lexical_entry):
                lexical_entries.append(lexical_entry)
        return lexical_entries

    def check_cross_references(self):
        """! @brief Check all cross-references in the lexicon.
        Fill the private attribute '__lexicalEntry' of each RelatedForm instance for all lexical entries.
        @return Lexicon instance.
        """
        for lexical_entry in self.get_lexical_entries():
            for related_form in lexical_entry.get_related_forms():
                # From RelatedForm targets attribute, retrieve the pointed LexicalEntry instance
                found_entry = self.find_lexical_entries(lambda lexical_entry: lexical_entry.get_lexeme() == related_form.get_lexeme())
                if len(found_entry) < 1:
                    # No lexical entry with this lexeme exists.
                    raise IOError(0, __file__, "Lexical entry %s does not exist. Please solve this issue by checking the related form of %s." % (related_form.get_lexeme(), lexical_entry.get_lexeme()))
                elif len(found_entry) > 1:
                    # Several lexical entries with this lexeme exist.
                    raise IOError(0, __file__, "Several lexical entries %s exist. Please solve this issue by renaming lexical entries correctly." % lexical_entry.get_lexeme())
                # Save the found lexical entry
                related_form.set_lexical_entry(found_entry[0])
        return self

    def convert_to_latex(self):
        """This method converts the lexicon into LaTeX format.
        """
        pass
