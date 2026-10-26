"""
Tests for Validate Binary Search Tree (LeetCode 98)
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

from lib import build_tree


def test_valid_bst_true():
    s = Solution()
    root = build_tree([2, 1, 3])
    assert s.isValidBST(root) is True

def test_valid_bst_false():
    s = Solution()
    root = build_tree([5, 1, 4, None, None, 3, 6])
    assert s.isValidBST(root) is False

def test_valid_bst_single():
    s = Solution()
    root = build_tree([1])
    assert s.isValidBST(root) is True

def test_valid_bst_violation_deep():
    s = Solution()
    root = build_tree([10, 5, 15, None, None, 6, 20])
    assert s.isValidBST(root) is False

