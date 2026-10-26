"""
Tests for Count Good Nodes in Binary Tree (LeetCode 1448)
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


def test_good_nodes_basic():
    s = Solution()
    root = build_tree([3, 1, 4, 3, None, 1, 5])
    assert s.goodNodes(root) == 4

def test_good_nodes_second():
    s = Solution()
    root = build_tree([3, 3, None, 4, 2])
    assert s.goodNodes(root) == 3

def test_good_nodes_single():
    s = Solution()
    root = build_tree([1])
    assert s.goodNodes(root) == 1

def test_good_nodes_negative():
    s = Solution()
    root = build_tree([2, None, 4, 10, 8, None, None, 4])
    assert s.goodNodes(root) == 4

