"""
Tests for 3Sum (LeetCode 15)
Two Pointers / Medium
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




def test_three_sum_basic():
    s = Solution()
    result = s.threeSum([-1, 0, 1, 2, -1, -4])
    sorted_result = sorted([sorted(t) for t in result])
    expected = sorted([[-1, -1, 2], [-1, 0, 1]])
    assert sorted_result == expected

def test_three_sum_no_result():
    s = Solution()
    result = s.threeSum([0, 1, 1])
    assert result == []

def test_three_sum_zeros():
    s = Solution()
    result = s.threeSum([0, 0, 0])
    assert result == [[0, 0, 0]]

