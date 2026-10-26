"""
Tests for Maximum Subarray (LeetCode 53)
Greedy / Medium
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




def test_mixed_array():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_single_element():
    s = Solution()
    assert s.maxSubArray([1]) == 1

def test_all_negative():
    s = Solution()
    assert s.maxSubArray([-1, -2, -3]) == -1

def test_all_positive():
    s = Solution()
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23

