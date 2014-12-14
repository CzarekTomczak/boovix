1. Install Python 3.4 from http://www.python.org/
2. Install wxPython Phoenix:
    pip install -U --pre -f http://wxpython.org/Phoenix/snapshot-builds/ wxPython_Phoenix
3. (Optional) Install Visual Studio 2013 Community IDE + Python Tools
   for Visual Studio.
4. pip install pylint
   4.1 Apply patch to pylint to add "dynamic-modules" option. Tested with
       pylint 1.4.0. Patch is here:
       /boovix/static_analysis/pylint_1.4.0_dynamic_modules.patch
       See also Issue #413 in pylint:
       https://bitbucket.org/logilab/pylint/issue/413/
5. pip install pep8
6. pip install mypy-lang
