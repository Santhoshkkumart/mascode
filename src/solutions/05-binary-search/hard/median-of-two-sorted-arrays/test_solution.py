"""
Tests for Median of Two Sorted Arrays (LeetCode 4)
Binary Search / Hard
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




def test_odd_total():
    s = Solution()
    assert s.findMedianSortedArrays([1,3], [2]) == 2.0

def test_even_total():
    s = Solution()
    assert s.findMedianSortedArrays([1,2], [3,4]) == 2.5

def test_one_empty():
    s = Solution()
    assert s.findMedianSortedArrays([], [1]) == 1.0

def test_both_single():
    s = Solution()
    assert s.findMedianSortedArrays([2], [1]) == 1.5

