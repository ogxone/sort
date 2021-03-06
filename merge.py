import re
import sys
from typing import List

from utils import read_input


def sort(arr: List):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = sort(arr[:mid])
    right = sort(arr[mid:])

    res = []
    i_left = left.pop(0)
    i_right = right.pop(0)

    while True:

        if i_left and (i_right is None or i_left < i_right):
            res.append(i_left)
            try:
                i_left = left.pop(0)
            except IndexError:
                i_left = None
        elif i_right:
            res.append(i_right)
            try:
                i_right = right.pop(0)
            except IndexError:
                i_right = None

        if i_left is None and i_right is None:
            break

    return res


if __name__ == '__main__':
    input = read_input(sys.argv)
    if len(input) == 0:
        raise Exception("Not valid input provided")
    print('Input obtained:')
    print(input)
    print('Sorted result')
    print(sort(input))
