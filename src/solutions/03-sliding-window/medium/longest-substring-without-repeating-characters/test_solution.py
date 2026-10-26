"""
Tests for Longest Substring Without Repeating Characters (LeetCode 3)
Sliding Window / Medium
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




def test_length_of_longest_substring_basic():
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3

def test_length_of_longest_substring_repeated():
    s = Solution()
    assert s.lengthOfLongestSubstring("bbbbb") == 1

def test_length_of_longest_substring_mixed():
    s = Solution()
    assert s.lengthOfLongestSubstring("pwwkew") == 3

def test_length_of_longest_substring_empty():
    s = Solution()
    assert s.lengthOfLongestSubstring("") == 0

