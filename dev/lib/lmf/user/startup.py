#! /usr/bin/env python

import sys

# Find lib/lmf/user/ path location
user_path = sys.path[0] + '/'

# Add user configuration folder to path
sys.path.append(user_path + 'config')

# Add user demonstration folder to path
sys.path.append(user_path + 'demo')

# Add lib/ folder to path
sys.path.append(user_path + '../..')

# Import LMF library
import lmf
