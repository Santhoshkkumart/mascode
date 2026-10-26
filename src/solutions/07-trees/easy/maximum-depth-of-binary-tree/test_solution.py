"""
Tests for Maximum Depth of Binary Tree (LeetCode 104)
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


def test_max_depth_basic():
    s = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert s.maxDepth(root) == 3

def test_max_depth_single():
    s = Solution()
    root = build_tree([1, None, 2])
    assert s.maxDepth(root) == 2

def test_max_depth_empty():
    s = Solution()
    assert s.maxDepth(None) == 0

def test_max_depth_one_node():
    s = Solution()
    root = build_tree([1])
    assert s.maxDepth(root) == 1

