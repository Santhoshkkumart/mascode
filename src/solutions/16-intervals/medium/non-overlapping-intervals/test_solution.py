"""
Tests for Non-overlapping Intervals (LeetCode 435)
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




def test_remove_one():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

def test_remove_two():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2

def test_remove_none():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0

def test_single_interval():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2]]) == 0

