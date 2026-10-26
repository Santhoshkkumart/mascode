"""
Tests for Insert Interval (LeetCode 57)
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




def test_overlap_middle():
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

def test_overlap_multiple():
    s = Solution()
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]

def test_no_overlap_before():
    s = Solution()
    assert s.insert([], [5, 7]) == [[5, 7]]

def test_no_overlap_after():
    s = Solution()
    assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]

