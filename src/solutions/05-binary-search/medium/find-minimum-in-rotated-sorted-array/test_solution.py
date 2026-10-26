"""
Tests for Find Minimum in Rotated Sorted Array (LeetCode 153)
Binary Search / Medium
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




def test_example_1():
    s = Solution()
    assert s.findMin([3,4,5,1,2]) == 1

def test_example_2():
    s = Solution()
    assert s.findMin([4,5,6,7,0,1,2]) == 0

def test_not_rotated():
    s = Solution()
    assert s.findMin([11,13,15,17]) == 11

def test_two_elements():
    s = Solution()
    assert s.findMin([2,1]) == 1

