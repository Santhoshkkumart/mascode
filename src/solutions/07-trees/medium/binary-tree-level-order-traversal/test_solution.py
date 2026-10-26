"""
Tests for Binary Tree Level Order Traversal (LeetCode 102)
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


def test_level_order_basic():
    s = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]

def test_level_order_single():
    s = Solution()
    root = build_tree([1])
    assert s.levelOrder(root) == [[1]]

def test_level_order_empty():
    s = Solution()
    assert s.levelOrder(None) == []

def test_level_order_complete():
    s = Solution()
    root = build_tree([1, 2, 3, 4, 5])
    assert s.levelOrder(root) == [[1], [2, 3], [4, 5]]

