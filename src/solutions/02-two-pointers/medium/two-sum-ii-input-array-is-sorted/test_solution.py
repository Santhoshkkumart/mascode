"""
Tests for Two Sum II - Input Array Is Sorted (LeetCode 167)
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




def test_two_sum_ii_basic():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]

def test_two_sum_ii_middle():
    s = Solution()
    assert s.twoSum([2, 3, 4], 6) == [1, 3]

def test_two_sum_ii_negative():
    s = Solution()
    assert s.twoSum([-1, 0], -1) == [1, 2]

