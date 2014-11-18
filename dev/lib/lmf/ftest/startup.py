#! /usr/bin/env python

import sys

# Find lib/lmf/ftest/ path location
ftest_path = sys.path[0] + '/'

# Add lib/ folder to path
sys.path.append(ftest_path + '../..')

# Import LMF library
import lmf
