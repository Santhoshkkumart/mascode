"""
Tests for Rotting Oranges (LeetCode 994)
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




def test_all_rotten():
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert s.orangesRotting(grid) == 4

def test_impossible():
    s = Solution()
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert s.orangesRotting(grid) == -1

def test_no_fresh():
    s = Solution()
    assert s.orangesRotting([[0, 2]]) == 0

