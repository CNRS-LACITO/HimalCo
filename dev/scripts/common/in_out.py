#! /usr/bin/env python
# -*- coding: utf-8 -*-

from defs import CODEC

class InOut():

    def create_obj(self):
        """Create 'obj' folder if it does not exist.
        """
        import os
        if not os.path.exists("obj"):
            os.mkdir("obj")

    def open_file(self, filename, mode, encoding=CODEC):
        try:
            return open(filename, mode, encoding=encoding)
        except TypeError:
            import codecs
            return codecs.open(filename, mode, encoding=encoding)

    def open_read(self, filename, encoding=CODEC):
        """Open file in read mode (automatically decode file in unicode).
        """
        return self.open_file(filename, 'rb', encoding=encoding)

    def open_write(self, filename, encoding=CODEC):
        """Open file in write mode (automatically code file in unicode).
        """
        return self.open_file(filename, 'wb', encoding=encoding)
