from merge import sort


def test_merge_sort():
    assert [3, 8, 23, 54, 65, 65, 454, 689, 756] == sort([54, 3, 65, 756, 8, 23, 689, 65, 454])
    assert [2, 3, 4, 4, 7, 7, 43, 61, 75] == sort([7, 3, 2, 7, 43, 61, 4, 4, 75])
