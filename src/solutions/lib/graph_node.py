"""Graph node type and helpers (mirrors LeetCode's Node for graph problems)."""


class Node:
    """LeetCode-style graph node (used in Clone Graph etc.)."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"


def build_graph(adj_list: list) -> Node | None:
    """Build a graph from a LeetCode-style adjacency list.

    build_graph([[2,4],[1,3],[2,4],[1,3]]) -> graph with 4 nodes
    Node 1 has neighbors [2, 4], Node 2 has neighbors [1, 3], etc.
    """
    if not adj_list:
        return None
    nodes = {}
    for i in range(1, len(adj_list) + 1):
        nodes[i] = Node(i)
    for i, neighbors in enumerate(adj_list, 1):
        for n in neighbors:
            nodes[i].neighbors.append(nodes[n])
    return nodes[1]


def graph_to_adjacency(node: Node | None) -> list:
    """Convert a graph back to a LeetCode-style adjacency list."""
    if node is None:
        return []
    visited = {}
    result = []

    def visit(n):
        if n.val in visited:
            return
        visited[n.val] = len(visited) + 1
        while len(result) < visited[n.val]:
            result.append([])
        for neighbor in n.neighbors:
            result[visited[n.val] - 1].append(neighbor.val)
        for neighbor in n.neighbors:
            visit(neighbor)

    visit(node)
    return result
