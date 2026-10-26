"""
Tests for Lowest Common Ancestor of a Binary Search Tree (LeetCode 235)
Trees / Medium
"""
import sys
from pathlib import Path

# Add repo root to path for lib imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

# Load solution from this directory (avoids module name collision with other test_solution.py files)
import importlib.util
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("_solution", _solution_path)
_solution_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution_mod)
Solution = _solution_mod.Solution

from lib import build_tree, find_node


def test_lca_basic():
    s = Solution()
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    assert s.lowestCommonAncestor(root, p, q).val == 6

def test_lca_descendant():
    s = Solution()
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 4)
    assert s.lowestCommonAncestor(root, p, q).val == 2

def test_lca_small():
    s = Solution()
    root = build_tree([2, 1])
    p = find_node(root, 2)
    q = find_node(root, 1)
    assert s.lowestCommonAncestor(root, p, q).val == 2

