"""
Tests for Regular Expression Matching (LeetCode 10)
2-D Dynamic Programming / Hard
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




def test_single_char_no_match():
    s = Solution()
    assert s.isMatch("aa", "a") == False

def test_star_match():
    s = Solution()
    assert s.isMatch("aa", "a*") == True

def test_dot_star():
    s = Solution()
    assert s.isMatch("ab", ".*") == True

def test_complex_pattern():
    s = Solution()
    assert s.isMatch("aab", "c*a*b") == True

def test_no_match():
    s = Solution()
    assert s.isMatch("mississippi", "mis*is*p*.") == False

