#! /usr/bin/env python

def open_file(filename, mode, encoding='utf8'):
    """! @brief Open file in specified mode (automatically decode file in unicode).
    @param filename Full path to file to open.
    @param mode Read or write mode.
    @param encoding Encoding mode. Default value is 'utf8'.
    @return File handler.
    """
    try:
        return open(filename, mode, encoding=encoding)
    except TypeError:
        import codecs
        return codecs.open(filename, mode, encoding=encoding)

def open_read(filename, encoding=None):
    """! @brief Open file in read mode (automatically decode file in unicode).
    @param filename Full path to file to open.
    @param encoding Encoding mode. Default value is None.
    @return File handler.
    """
    if encoding is None:
        return open_file(filename, 'rb')
    else:
        return open_file(filename, 'rb', encoding=encoding)

def open_write(filename, encoding=None):
    """! @brief Open file in write mode (automatically decode file in unicode).
    @param filename Full path to file to open.
    @param encoding Encoding mode. Default value is None.
    @return File handler.
    """
    if encoding is None:
        return open_file(filename, 'wb')
    else:
        return open_file(filename, 'wb', encoding=encoding)
