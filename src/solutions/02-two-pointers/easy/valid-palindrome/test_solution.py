"""
Tests for Valid Palindrome (LeetCode 125)
Two Pointers / Easy
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




def test_valid_palindrome_true():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True

def test_valid_palindrome_false():
    s = Solution()
    assert s.isPalindrome("race a car") == False

def test_valid_palindrome_empty():
    s = Solution()
    assert s.isPalindrome(" ") == True

def test_valid_palindrome_with_numbers():
    s = Solution()
    assert s.isPalindrome("0P") == False

