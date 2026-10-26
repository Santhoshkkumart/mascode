"""
Tests for Merge Triplets to Form Target Triplet (LeetCode 1899)
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




def test_merge_possible():
    s = Solution()
    assert s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) == True

def test_already_target():
    s = Solution()
    assert s.mergeTriplets([[1, 3, 4], [2, 5, 8]], [2, 5, 8]) == True

def test_impossible():
    s = Solution()
    assert s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 0, 2]], [5, 5, 5]) == False

def test_skip_invalid():
    s = Solution()
    assert s.mergeTriplets([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [3, 3, 3]) == True

