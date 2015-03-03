#! /usr/bin/env python

import sys

# Find lib/lmf/user/ path location
user_path = sys.path[0] + '/'

# Add default configuration folder to path
sys.path.append(user_path + 'default')

# Add lib/ folder to path
sys.path.append(user_path + '../..')

# Import LMF library
import lmf
