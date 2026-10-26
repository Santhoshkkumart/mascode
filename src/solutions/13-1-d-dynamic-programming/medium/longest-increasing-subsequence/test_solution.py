"""
Tests for Longest Increasing Subsequence (LeetCode 300)
1-D Dynamic Programming / Medium
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




def test_example_one():
    s = Solution()
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_example_two():
    s = Solution()
    assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4

def test_all_same():
    s = Solution()
    assert s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1

def test_single_element():
    s = Solution()
    assert s.lengthOfLIS([5]) == 1

