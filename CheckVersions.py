"""
EECS 658 Assignment 1
Program: CheckVersions.py

Description:
Checks versions of Python and required ML libraries.
Prints "Hello World!" to verify execution.

Inputs:
None

Outputs:
- Python version
- scipy version
- numpy version
- pandas version
- sklearn version
- Hello World!

Author: Your Full Name
Creation Date: YYYY-MM-DD
Sources: Lecture slides, Assignment 1 instructions
"""

import sys          # Access Python version
import scipy        # Scientific computing
import numpy        # Numerical arrays
import pandas       # Data handling
import sklearn      # Machine learning library

# Print Python version
print("Python:", sys.version)

# Print library versions
print("scipy:", scipy.__version__)
print("numpy:", numpy.__version__)
print("pandas:", pandas.__version__)
print("sklearn:", sklearn.__version__)

# Hello World confirmation
print("Hello World!")
