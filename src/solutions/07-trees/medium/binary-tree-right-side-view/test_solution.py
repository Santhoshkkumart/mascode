"""
Tests for Binary Tree Right Side View (LeetCode 199)
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


def test_right_side_view_basic():
    s = Solution()
    root = build_tree([1, 2, 3, None, 5, None, 4])
    assert s.rightSideView(root) == [1, 3, 4]

def test_right_side_view_right_only():
    s = Solution()
    root = build_tree([1, None, 3])
    assert s.rightSideView(root) == [1, 3]

def test_right_side_view_empty():
    s = Solution()
    assert s.rightSideView(None) == []

def test_right_side_view_left_skewed():
    s = Solution()
    root = build_tree([1, 2, None, 3])
    assert s.rightSideView(root) == [1, 2, 3]

