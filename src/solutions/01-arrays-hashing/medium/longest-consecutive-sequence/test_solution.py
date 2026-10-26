"""
Tests for Longest Consecutive Sequence (LeetCode 128)
Arrays & Hashing / Medium
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




def test_longest_consecutive_basic():
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

def test_longest_consecutive_full_range():
    s = Solution()
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

def test_longest_consecutive_empty():
    s = Solution()
    assert s.longestConsecutive([]) == 0

def test_longest_consecutive_single():
    s = Solution()
    assert s.longestConsecutive([1]) == 1

