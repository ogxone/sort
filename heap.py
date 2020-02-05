import sys
from math import floor
from typing import List

from utils import read_input


def _heapify(arr: List):
    _len = len(arr) - 1
    start = _heap_parent(_len)

    while True:
        if start < 0:
            break
        _sift_down(arr, start, _len)

        start -= 1


def _sift_down(arr: List, start, end):
    i_root = start

    while _heap_left_child(i_root) <= end:
        i_child = _heap_left_child(i_root)
        i_swap = i_root

        if arr[i_child] > arr[i_swap]:
            i_swap = i_child

        if i_child + 1 <= end and arr[i_child + 1] > arr[i_swap]:
            i_swap = i_child + 1

        if i_swap == i_root:
            return
        else:
            arr[i_swap], arr[i_root] = arr[i_root], arr[i_swap]
            i_root = i_swap


def _heap_left_child(i):
    return 2 * i + 1


def _heap_parent(i):
    return floor((i - 1) / 2)


def sort(arr: List):
    _heapify(arr)

    end = len(arr) - 1

    while True:

        if end <= 0:
            break

        arr[end], arr[0] = arr[0], arr[end]

        end -= 1

        _sift_down(arr, 0, end)

    return arr


if __name__ == '__main__':
    input = read_input(sys.argv)
    if len(input) == 0:
        raise Exception("Not valid input provided")
    print('Input obtained:')
    print(input)
    print('Sorted result')
    print(sort(input))
