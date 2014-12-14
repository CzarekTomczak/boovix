''' This is test module. Docstring required by pylint.
    Pylint detects all three asd errors.
    Pyflakes detects only asd() in test().
'''

import os
import test2

# pep8 requires two blank lines above.
def test():
    ''' This is test function. Docstring required by pylint. '''
    asd() # Wrong indentation
    fgh = xyz

if __name__ == "__main__":
    os.asd()
    test2.asd()
