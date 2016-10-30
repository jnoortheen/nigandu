#!/usr/bin/python

import os
import sys
import warnings

# the site module must be imported for normal behavior to take place; it is
# done dynamically so that cx_Freeze will not add all modules referenced by
# the site module to the frozen executable
__import__("site")

# now locate the pth file to modify the path appropriately
baseName, ext = os.path.splitext(FILE_NAME)
pathFileName = baseName + ".pth"
sys.path = [s.strip() for s in file(pathFileName).read().splitlines()] + \
        sys.path
