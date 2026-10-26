"""Singly linked list node type and helpers (mirrors LeetCode's ListNode)."""


class ListNode:
    """LeetCode-style singly linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None


def build_linked_list(values: list) -> ListNode | None:
    """Build a linked list from a Python list of values.

    build_linked_list([1, 2, 3]) -> 1 -> 2 -> 3 -> None
    """
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def linked_list_to_array(head: ListNode | None) -> list:
    """Convert a linked list back to a Python list."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result
