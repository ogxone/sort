import sys
from typing import List

from utils import read_input


def sort(arr: List):
    arr_size = len(arr) - 1

    if arr_size == 0:
        return arr

    for j in range(arr_size):
        for i in range(arr_size):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]

    return arr


if __name__ == '__main__':
    input = read_input(sys.argv)
    if len(input) == 0:
        raise Exception("Not valid input provided")
    print('Input obtained:')
    print(input)
    print('Sorted result')
    print(sort(input))
