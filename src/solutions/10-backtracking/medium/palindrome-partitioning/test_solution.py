"""
Tests for Palindrome Partitioning (LeetCode 131)
Backtracking / Medium
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




def test_aab():
    s = Solution()
    result = s.partition("aab")
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert sorted(tuple(x) for x in result) == sorted(tuple(x) for x in expected)

def test_single_char():
    s = Solution()
    assert s.partition("a") == [["a"]]

def test_all_palindrome():
    s = Solution()
    result = s.partition("aaa")
    expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    assert sorted(tuple(x) for x in result) == sorted(tuple(x) for x in expected)

