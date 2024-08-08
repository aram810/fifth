from typing import Any, Self


class Node:
    def __init__(self, val: int, next_item: Self | None = None):
        self.val = val
        self.next_item = next_item

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            return False

        return self.val == other.val and self.next_item == other.next_item

    def __repr__(self):
        return "Node(val={0}, next_item={1})".format(self.val, self.next_item)


def get_reduced_linked_list(head: Node, n: int) -> Node | None:
    dummy = Node(val=0, next_item=head)
    left: Node | None = dummy
    right: Node | None = head

    while n > 0 and right:
        right = right.next_item
        n -= 1

    while right:
        left = left.next_item  # type: ignore[union-attr]
        right = right.next_item

    left.next_item = left.next_item.next_item  # type: ignore[union-attr]

    return dummy.next_item
