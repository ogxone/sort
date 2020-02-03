import sys
from typing import List

from utils import read_input


def sort(arr: List, low: int = None, high: int = None):
    low = low if low is not None else 0
    high = high if high is not None else len(arr) - 1

    if high < low:
        return arr

    middle = _partition(arr, low, high)

    sort(arr, low, middle - 1)
    sort(arr, middle + 1, high)

    return arr


def _partition(arr: List, low: int, high: int) -> int:
    j = low
    pivot = arr[high]

    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    arr[j], arr[high] = arr[high], arr[j]

    return j


if __name__ == '__main__':
    input = read_input(sys.argv)
    if len(input) == 0:
        raise Exception("Not valid input provided")
    print('Input obtained:')
    print(input)
    print('Sorted result')
    print(sort(input))
