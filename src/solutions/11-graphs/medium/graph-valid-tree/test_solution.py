"""
Tests for Graph Valid Tree (LeetCode 261)
Graphs / Medium
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




def test_valid_tree():
    s = Solution()
    assert s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True

def test_has_cycle():
    s = Solution()
    assert s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False

def test_not_connected():
    s = Solution()
    assert s.validTree(4, [[0, 1], [2, 3]]) is False

