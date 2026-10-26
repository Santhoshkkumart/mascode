"""
Tests for Merge Intervals (LeetCode 56)
Intervals / Medium
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




def test_merge_overlapping():
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_touching_intervals():
    s = Solution()
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]

def test_no_overlap():
    s = Solution()
    assert s.merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]

def test_single_interval():
    s = Solution()
    assert s.merge([[1, 4]]) == [[1, 4]]

