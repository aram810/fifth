import pytest
import two_sum


@pytest.mark.parametrize(
    ("numbers", "target", "expected_indexes"),
    [
        ([], 1, []),
        ([1], 1, []),
        ([1, 2, 3], 4, [0, 2]),
        ([1, 2, 100, 5], 105, [2, 3]),
        ([1, 1, 100, 5], 2, [0, 1]),
        ([100, 200, 300], 700, []),
    ],
)
def test_input(
    numbers: list[int],
    target: int,
    expected_indexes: list[int],
) -> None:
    assert sorted(two_sum.find_indexes(numbers, target)) == expected_indexes
