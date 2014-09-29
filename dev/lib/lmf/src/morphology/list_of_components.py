#! /usr/bin/env python

"""! @package morphology
"""

class ListOfComponents():
    """ "List of Components is a class representing the aggregative aspect of a multiword expression (MWE). The mechanism can also be applied recursively, so that an MWE way be comprised of components that are themselves MWEs. This class is used in the morphological pattern and MWE pattern packages." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        ListOfComponents instance is owned by LexicalEntry.
        @return A ListOfComponents instance.
        """
        ## Component instances are owned by ListOfComponents
        # There are two or more Component instances per ListOfComponents
        self.component = [] # ordered list

    def __del__(self):
        """! @brief Destructor.
        Release Component instances.
        """
        for component in self.component:
            del component
        del self.component[:]
