"""
Tests for Minimum Interval to Include Each Query (LeetCode 1851)
Intervals / Hard
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




def test_example1():
    s = Solution()
    assert s.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]

def test_example2():
    s = Solution()
    assert s.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]

def test_no_valid_interval():
    s = Solution()
    assert s.minInterval([[1, 2], [3, 4]], [5]) == [-1]

def test_single_interval():
    s = Solution()
    assert s.minInterval([[1, 10]], [5]) == [10]

