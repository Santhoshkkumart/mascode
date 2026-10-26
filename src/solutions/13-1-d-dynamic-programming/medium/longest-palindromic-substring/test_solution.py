"""
Tests for Longest Palindromic Substring (LeetCode 5)
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




def test_babad():
    s = Solution()
    result = s.longestPalindrome("babad")
    assert result == "bab" or result == "aba"

def test_cbbd():
    s = Solution()
    assert s.longestPalindrome("cbbd") == "bb"

def test_single_char():
    s = Solution()
    assert s.longestPalindrome("a") == "a"

def test_full_palindrome():
    s = Solution()
    assert s.longestPalindrome("racecar") == "racecar"

