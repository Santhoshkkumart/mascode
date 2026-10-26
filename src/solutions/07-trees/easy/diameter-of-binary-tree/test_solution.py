"""
Tests for Diameter of Binary Tree (LeetCode 543)
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


def test_diameter_basic():
    s = Solution()
    root = build_tree([1, 2, 3, 4, 5])
    assert s.diameterOfBinaryTree(root) == 3

def test_diameter_two_nodes():
    s = Solution()
    root = build_tree([1, 2])
    assert s.diameterOfBinaryTree(root) == 1

def test_diameter_single():
    s = Solution()
    root = build_tree([1])
    assert s.diameterOfBinaryTree(root) == 0

def test_diameter_skewed():
    s = Solution()
    root = build_tree([1, 2, None, 3, None, 4, None])
    assert s.diameterOfBinaryTree(root) == 3

