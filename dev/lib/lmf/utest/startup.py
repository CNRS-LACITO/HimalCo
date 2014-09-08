#! /usr/bin/env python

## Import system Python module and unit tests Python module
import sys, unittest

utest_path = sys.path[0] + '/'
sys.path.append(utest_path + '..')
sys.path.append(utest_path + '../src')

# Activate unitary test mode
#sys.argv.append('-u')

# Import LMF library
from src import *
