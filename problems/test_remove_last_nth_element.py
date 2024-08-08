import pytest
import remove_last_nth_element as problem


def _list_to_linked_list(numbers: list[int]) -> problem.Node | None:
    if not numbers:
        return None

    head = problem.Node(val=numbers[0])
    tail = head

    for i in range(1, len(numbers)):
        tail.next_item = problem.Node(val=numbers[i])
        tail = tail.next_item

    return head


@pytest.mark.parametrize(
    ("numbers", "expected_head"),
    [
        ([], None),
        ([1], problem.Node(val=1, next_item=None)),
        ([1, 2], problem.Node(val=1, next_item=problem.Node(val=2, next_item=None))),
    ],
)
def test_list_to_linked_list(
    numbers: list[int], expected_head: problem.Node | None
) -> None:
    assert _list_to_linked_list(numbers) == expected_head


@pytest.mark.parametrize(
    ("first_head", "second_head"),
    [
        (_list_to_linked_list([1]), _list_to_linked_list([1])),
        (_list_to_linked_list([1, 2]), _list_to_linked_list([1, 2])),
    ],
)
def test_linked_lists_equal(
    first_head: problem.Node, second_head: problem.Node
) -> None:
    assert first_head == second_head


@pytest.mark.parametrize(
    ("first_head", "second_head"),
    [
        (_list_to_linked_list([1]), _list_to_linked_list([1, 2])),
        (_list_to_linked_list([1, 2]), _list_to_linked_list([2, 1])),
        (_list_to_linked_list([1, 2]), _list_to_linked_list([1, 2, 3])),
        (_list_to_linked_list([3, 2, 1]), _list_to_linked_list([2, 1])),
        (_list_to_linked_list([3, 2, 1]), _list_to_linked_list([])),
    ],
)
def test_linked_lists_not_equal(
    first_head: problem.Node, second_head: problem.Node
) -> None:
    assert first_head != second_head


@pytest.mark.parametrize(
    ("head", "n", "expected_head"),
    [
        (
            _list_to_linked_list([1, 2, 3, 4, 5]),
            2,
            _list_to_linked_list([1, 2, 3, 5]),
        ),
        (
            _list_to_linked_list([1]),
            1,
            None,
        ),
        (
            _list_to_linked_list([1, 2]),
            1,
            _list_to_linked_list([1]),
        ),
        (
            _list_to_linked_list([1, 2]),
            2,
            _list_to_linked_list([2]),
        ),
        (
            _list_to_linked_list([1, 2]),
            5,
            _list_to_linked_list([2]),
        ),
    ],
)
def test_remove_last_nth_element(
    head: problem.Node,
    n: int,
    expected_head: problem.Node,
) -> None:
    assert problem.get_reduced_linked_list(head, n) == expected_head
