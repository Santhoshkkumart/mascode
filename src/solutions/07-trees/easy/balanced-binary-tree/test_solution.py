"""
Tests for Balanced Binary Tree (LeetCode 110)
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


def test_balanced_true():
    s = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert s.isBalanced(root) is True

def test_balanced_false():
    s = Solution()
    root = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert s.isBalanced(root) is False

def test_balanced_empty():
    s = Solution()
    assert s.isBalanced(None) is True

def test_balanced_single():
    s = Solution()
    root = build_tree([1])
    assert s.isBalanced(root) is True

