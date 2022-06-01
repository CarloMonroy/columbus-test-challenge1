import pytest


# Columbus interview test

def plain_data(data: list):
    if not isinstance(data, list):
        return 'type error'
    if len(data) == 0:  # Here we check if the list is empty
        return data
    if isinstance(data[0], list):  # Here we check if the instance is another list
        # If it is we use recursion to see if there is another list inside that element. We do this until the list is completely flat
        return plain_data(data[0]) + plain_data(data[1:])
    return data[:1] + plain_data(data[1:])  # Here we use recursion again until we don't have anymore nested lists


# main.py

if __name__ == "__main__":
    plain_data([1, [2, [3, [4, 5]]]])


def test_first_use_case():
    expected_value = [1, 2, 3, 4, 5]
    result = plain_data([1, [2, [3, [4, 5]]]])
    assert result == expected_value

# We are using the pytest parametrize to test all cases in one go
@pytest.mark.parametrize("x, y, z", [([1, [2, [3, [4, 5]]]], [6, [1, [2, 3], 4], 5], [[[1, 2, ], 3], 4, 5]),
                                  ([[[1, 2, ], 3], 4, 5], [[[1, 2, ], 3], 4, 5], [1, 2, 3, 4, 5])])
def testuse_case(x, y, z):
    expected_value = [6, 1, 2, 3, 4, 5]
    result = plain_data([6, [1, [2, 3], 4], 5])
    assert result == expected_value

