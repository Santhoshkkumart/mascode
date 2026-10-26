"""
Tests for Valid Anagram (LeetCode 242)
Arrays & Hashing / Easy
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




def test_valid_anagram_true():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True

def test_not_anagram():
    s = Solution()
    assert s.isAnagram("rat", "car") == False

def test_same_string():
    s = Solution()
    assert s.isAnagram("abc", "abc") == True

def test_different_lengths():
    s = Solution()
    assert s.isAnagram("ab", "abc") == False

