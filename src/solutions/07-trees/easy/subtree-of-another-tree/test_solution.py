"""
Tests for Subtree of Another Tree (LeetCode 572)
Trees / Easy
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

from lib import build_tree


def test_subtree_true():
    s = Solution()
    root = build_tree([3, 4, 5, 1, 2])
    subRoot = build_tree([4, 1, 2])
    assert s.isSubtree(root, subRoot) is True

def test_subtree_false():
    s = Solution()
    root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = build_tree([4, 1, 2])
    assert s.isSubtree(root, subRoot) is False

def test_subtree_equal():
    s = Solution()
    root = build_tree([1, 1])
    subRoot = build_tree([1])
    assert s.isSubtree(root, subRoot) is True

def test_subtree_not_present():
    s = Solution()
    root = build_tree([1, 2, 3])
    subRoot = build_tree([4])
    assert s.isSubtree(root, subRoot) is False

