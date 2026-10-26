"""Binary tree node type and helpers (mirrors LeetCode's TreeNode)."""


class TreeNode:
    """LeetCode-style binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values: list) -> TreeNode | None:
    """Build a binary tree from a LeetCode-style level-order list.

    Uses None for absent nodes (same as LeetCode's serialization).
    build_tree([1, 2, 3]) ->   1
                                / \\
                               2   3
    build_tree([1, None, 2]) -> 1
                                  \\
                                   2
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_array(root: TreeNode | None) -> list:
    """Convert a binary tree to a LeetCode-style level-order list."""
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Strip trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    """Find a node with the given value in a BST (or binary tree via BFS)."""
    if root is None:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None
