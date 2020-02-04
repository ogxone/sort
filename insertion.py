import sys
from typing import List

from utils import read_input


def sort(arr: List):
    if len(arr) <= 1:
        return arr

    out = [arr.pop(0)]

    while True:
        try:
            next = arr.pop(0)
        except IndexError:
            break

        for i, v in enumerate(out):
            if next < v:
                out.insert(i, next)
                break
        else:
            out.append(next)

    return out


if __name__ == '__main__':
    input = read_input(sys.argv)
    if len(input) == 0:
        raise Exception("Not valid input provided")
    print('Input obtained:')
    print(input)
    print('Sorted result')
    print(sort(input))
