"""
Tests for Kth Smallest Element in a BST (LeetCode 230)
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


def test_kth_smallest_basic():
    s = Solution()
    root = build_tree([3, 1, 4, None, 2])
    assert s.kthSmallest(root, 1) == 1

def test_kth_smallest_second():
    s = Solution()
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert s.kthSmallest(root, 3) == 3

def test_kth_smallest_largest():
    s = Solution()
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert s.kthSmallest(root, 6) == 6

def test_kth_smallest_single():
    s = Solution()
    root = build_tree([1])
    assert s.kthSmallest(root, 1) == 1

