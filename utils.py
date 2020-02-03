import re
from typing import List


def read_input(argv: List):
    argv.pop(0)

    result = []

    arg_re = re.compile(r"\d+")

    for arg in argv:
        try:
            arg = arg_re.match(arg).group(0)
        except AttributeError:
            pass

        try:
            result.append(int(arg))
        except ValueError:
            pass

    return result
