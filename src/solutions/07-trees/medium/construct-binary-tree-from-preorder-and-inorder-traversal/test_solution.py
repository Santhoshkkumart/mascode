"""
Tests for Construct Binary Tree from Preorder and Inorder Traversal (LeetCode 105)
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

from lib import build_tree, tree_to_array


def test_build_tree_basic():
    s = Solution()
    root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_array(root) == [3, 9, 20, None, None, 15, 7]

def test_build_tree_single():
    s = Solution()
    root = s.buildTree([-1], [-1])
    assert tree_to_array(root) == [-1]

def test_build_tree_left_skewed():
    s = Solution()
    root = s.buildTree([1, 2, 3], [3, 2, 1])
    assert tree_to_array(root) == [1, 2, None, 3]

def test_build_tree_right_skewed():
    s = Solution()
    root = s.buildTree([1, 2, 3], [1, 2, 3])
    assert tree_to_array(root) == [1, None, 2, None, 3]

