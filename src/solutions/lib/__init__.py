"""
Shared type definitions and helper utilities for NeetCode 150 problems.

These mirror the types LeetCode provides automatically in their online judge.
Import from here in solution and test files when you need ListNode, TreeNode,
or graph Node types.
"""

from .list_node import ListNode, build_linked_list, linked_list_to_array
from .tree_node import TreeNode, build_tree, tree_to_array, find_node
from .graph_node import Node, build_graph, graph_to_adjacency

__all__ = [
    "ListNode",
    "build_linked_list",
    "linked_list_to_array",
    "TreeNode",
    "build_tree",
    "tree_to_array",
    "find_node",
    "Node",
    "build_graph",
    "graph_to_adjacency",
]
