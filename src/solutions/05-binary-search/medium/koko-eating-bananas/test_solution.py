"""
Tests for Koko Eating Bananas (LeetCode 875)
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
    assert s.minEatingSpeed([3,6,7,11], 8) == 4

def test_example_2():
    s = Solution()
    assert s.minEatingSpeed([30,11,23,4,20], 5) == 30

def test_example_3():
    s = Solution()
    assert s.minEatingSpeed([30,11,23,4,20], 6) == 23

def test_single_pile():
    s = Solution()
    assert s.minEatingSpeed([5], 5) == 1

