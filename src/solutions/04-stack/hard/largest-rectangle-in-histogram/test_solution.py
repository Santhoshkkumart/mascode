"""
Tests for Largest Rectangle in Histogram (LeetCode 84)
Stack / Hard
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
    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10

def test_example_2():
    s = Solution()
    assert s.largestRectangleArea([2,4]) == 4

def test_single_bar():
    s = Solution()
    assert s.largestRectangleArea([5]) == 5

def test_all_same():
    s = Solution()
    assert s.largestRectangleArea([3,3,3,3]) == 12

