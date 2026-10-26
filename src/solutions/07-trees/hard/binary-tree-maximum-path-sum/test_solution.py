"""
Tests for Binary Tree Maximum Path Sum (LeetCode 124)
Trees / Hard
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


def test_max_path_sum_basic():
    s = Solution()
    root = build_tree([1, 2, 3])
    assert s.maxPathSum(root) == 6

def test_max_path_sum_negative():
    s = Solution()
    root = build_tree([-10, 9, 20, None, None, 15, 7])
    assert s.maxPathSum(root) == 42

def test_max_path_sum_single_negative():
    s = Solution()
    root = build_tree([-3])
    assert s.maxPathSum(root) == -3

def test_max_path_sum_all_negative():
    s = Solution()
    root = build_tree([2, -1, -2])
    assert s.maxPathSum(root) == 2

