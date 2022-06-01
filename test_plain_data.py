import pytest
from plain_data import plain_data


# We are using pytest parametrize to do all test in 1 go and keep the code DRY
@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5]),
        ([6, [1, [2, 3], 4], 5], [6, 1, 2, 3, 4, 5]),
        ([[[1, 2,], 3], 4, 5], [1, 2, 3, 4, 5])
    ]
)
def test_unit(input, expected):
    assert plain_data(input) == expected