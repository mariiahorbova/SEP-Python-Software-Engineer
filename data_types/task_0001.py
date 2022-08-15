# 1. Write Python program to get the version(not inside iterpretator).

import sys

def python_version():
    if sys.version_info.major == 3:
        print('Python3')
    else:
        print('Python2')

python_version()
