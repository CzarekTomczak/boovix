# Copyright (c) 2014, The Boovix authors that are listed
# in the AUTHORS file. All rights reserved. Use of this
# source code is governed by the BSD 3-clause license that
# can be found in the LICENSE file.

"""
Function annotations in Python 3:
http://legacy.python.org/dev/peps/pep-3107/

Type checking in Python 3:
* http://code.activestate.com/recipes/578528
* http://stackoverflow.com/questions/1275646

mypy static type checking during compilation:
https://mail.python.org/pipermail/python-ideas/2014-August/028618.html

    from typing import List, Dict
    def word_count(input: List[str]) -> Dict[str, int]:
        result = {}  #type: Dict[str, int]
        for line in input:
            for word in line.split():
                result[word] = result.get(word, 0) + 1
        return result

    Note that the #type: comment is part of the mypy syntax
"""
