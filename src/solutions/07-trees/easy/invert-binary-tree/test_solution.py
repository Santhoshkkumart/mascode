"""
Tests for Invert Binary Tree (LeetCode 226)
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

from lib import build_tree, tree_to_array


def test_invert_basic():
    s = Solution()
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    result = s.invertTree(root)
    assert tree_to_array(result) == [4, 7, 2, 9, 6, 3, 1]

def test_invert_small():
    s = Solution()
    root = build_tree([2, 1, 3])
    result = s.invertTree(root)
    assert tree_to_array(result) == [2, 3, 1]

def test_invert_empty():
    s = Solution()
    result = s.invertTree(None)
    assert result is None

