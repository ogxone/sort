import pytest

from merge import sort as merge_sort
from quick import sort as quick_sort


def test_merge_sort(fixtures):
    for fixture in fixtures:
        assert merge_sort(fixture[0]) == fixture[1]
        assert quick_sort(fixture[0]) == fixture[1]


@pytest.fixture
def fixtures():
    return [
        [
            [54, 3, 65, 756, 8, 23, 689, 65, 454],
            [3, 8, 23, 54, 65, 65, 454, 689, 756]
        ],
        [
            [7, 3, 2, 7, 43, 61, 4, 4, 75],
            [2, 3, 4, 4, 7, 7, 43, 61, 75]
        ]
    ]
