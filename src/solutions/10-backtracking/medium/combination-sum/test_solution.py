"""
Tests for Combination Sum (LeetCode 39)
Backtracking / Medium
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




def test_basic():
    s = Solution()
    result = s.combinationSum([2, 3, 6, 7], 7)
    expected = [[2, 2, 3], [7]]
    assert sorted(tuple(sorted(x)) for x in result) == sorted(tuple(sorted(x)) for x in expected)

def test_multiple_combinations():
    s = Solution()
    result = s.combinationSum([2, 3, 5], 8)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted(tuple(sorted(x)) for x in result) == sorted(tuple(sorted(x)) for x in expected)

def test_no_solution():
    s = Solution()
    assert s.combinationSum([2], 1) == []

