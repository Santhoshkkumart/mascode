"""
Tests for Palindromic Substrings (LeetCode 647)
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




def test_abc():
    s = Solution()
    assert s.countSubstrings("abc") == 3

def test_aaa():
    s = Solution()
    assert s.countSubstrings("aaa") == 6

def test_single_char():
    s = Solution()
    assert s.countSubstrings("a") == 1

def test_two_chars():
    s = Solution()
    assert s.countSubstrings("aa") == 3

