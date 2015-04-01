#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Add koyi configuration folder to path
sys.path.append(user_path + 'koyi')

# Create result folder
if not os.path.exists(user_path + "koyi/result"):
    os.mkdir(user_path + "koyi/result")
