#! /usr/bin/env python

"""! @package core
"""

class Lexicon():
    """! This class represents a lexicon containing lexical entries.
    """
    def __init__(self):
        """! @brief Constructor.
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
        """! @brief This method checks all cross-references in the lexicon.
        """
        pass

    def convert_to_latex(self):
        """This method converts the lexicon into LaTeX format.
        """
        pass
