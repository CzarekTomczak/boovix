# Copyright (c) 2014, The Boovix authors that are listed
# in the AUTHORS file. All rights reserved. Use of this
# source code is governed by the BSD 3-clause license that
# can be found in the LICENSE file.

"""
Static analysis: pylint, pep8. The autopep8 is disabled currently,
as it forces strict indentation while pep8 allows more freedom
in that matter.
"""

import os
import sys
import subprocess
from subprocess import STDOUT
import fnmatch
import re

# C:\\Python34\\Scripts - autopep8 and other tools reside there.
#                         PTVS does not add this directory to sys.path
SCRIPTS_DIRECTORY = os.path.join(os.path.dirname(sys.executable),
                                 "Scripts")

CURRENT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(
                                                 __file__)))
ROOT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)


def main():
    """ Main function """
    os.chdir(ROOT_DIRECTORY)
    static_analysis()


def static_analysis():
    """ Static analysis: autopep8, pylint, pep8 """
    # autopep8() - disabled, see docstring for module.
    pylint()
    pep8()


def check_output(command):
    """ A wrapper around subprocess.check_output(). If it fails output
    is written to STDERR along with message that static analysis failed.
    Then it exits with returncode.
    """
    try:
        print(command)
        output = subprocess.check_output(command, stderr=STDOUT, shell=True)
        if output:
            print(output.decode("ascii", errors="replace"))
        print("OK")
    except subprocess.CalledProcessError as error:
        print(error.output.decode("ascii", errors="replace"))
        print("-"*80)
        print("ERROR: static analysis failed")
        print("-"*80)
        sys.exit(error.returncode)


def autopep8():
    """ Remove trailing whitespace, as VS2013 does not have such option.
    Additionally it makes other style related fixes as well.
    """
    prog = os.path.join(SCRIPTS_DIRECTORY, "autopep8")
    # E309 - Add missing blank line (after class declaration).
    check_output("%s --in-place --recursive --ignore E309 ." % prog)


def pylint():
    """ Static analysis of code using Pylint """
    modules_and_packages = get_packages_and_modules()
    # Do not use absolute path for rcfile as output is less readable.
    rcfile = os.path.join("static_analysis", ".pylintrc")
    assert os.path.exists(rcfile)
    for modpkg in modules_and_packages:
        prog = os.path.join(SCRIPTS_DIRECTORY, "pylint")
        check_output("%s --reports=n --rcfile=\"%s\" %s" % (
                     prog, rcfile, modpkg))


def get_packages_and_modules():
    """ Finds packages and alone modules in Boovix directory recursively.
    An alone module is in a form of a full path to a file.
    """
    packages = []
    all_modules = []
    # The builtins.StopIteration exception must be unchecked in PTVS
    # "user-unhandled" column, otherwise a blank exception occurs
    # when calling os.walk().
    for (curroot, dummy_dirnames, filenames) in os.walk(ROOT_DIRECTORY):
        for pyfile in fnmatch.filter(filenames, '*.py'):
            pyfile = os.path.join(curroot, pyfile)
            pyfile = pyfile.replace(ROOT_DIRECTORY + os.path.sep, "")
            if pyfile.endswith("__init__.py"):
                package = pyfile.replace(os.path.sep + "__init__.py", "")
                package = package.replace(os.path.sep, ".")
                packages.append(package)
            else:
                module = re.sub(r"\.py$", "", pyfile)
                module = module.replace(os.path.sep, ".")
                all_modules.append(module)
    alone_files = []
    for module in all_modules:
        possible_package = re.sub(r"\.?\w+$", "", module)
        if possible_package not in packages:
            pyfile = module.replace(".", os.path.sep)
            pyfile = pyfile + ".py"
            # Do not show full path as it is less readable.
            # pyfile = os.path.join(ROOT_DIRECTORY, pyfile)
            # Do not include static_analysis/tests/
            static_analysis_tests = os.path.join("static_analysis", "tests") \
                + os.path.sep
            if not pyfile.startswith(static_analysis_tests):
                alone_files.append(pyfile)
    return packages + alone_files


def pep8():
    """ Check PEP8 style guidelines """
    prog = os.path.join(SCRIPTS_DIRECTORY, "pep8")
    check_output("%s --exclude=static_analysis/tests/ ./" % prog)


if __name__ == "__main__":
    main()
