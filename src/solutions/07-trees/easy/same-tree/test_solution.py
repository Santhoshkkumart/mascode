"""
Tests for Same Tree (LeetCode 100)
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


def test_same_tree_true():
    s = Solution()
    p = build_tree([1, 2, 3])
    q = build_tree([1, 2, 3])
    assert s.isSameTree(p, q) is True

def test_same_tree_structure_diff():
    s = Solution()
    p = build_tree([1, 2])
    q = build_tree([1, None, 2])
    assert s.isSameTree(p, q) is False

def test_same_tree_value_diff():
    s = Solution()
    p = build_tree([1, 2, 1])
    q = build_tree([1, 1, 2])
    assert s.isSameTree(p, q) is False

def test_same_tree_both_empty():
    s = Solution()
    assert s.isSameTree(None, None) is True

