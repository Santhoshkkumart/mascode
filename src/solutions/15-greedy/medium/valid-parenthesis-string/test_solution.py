"""
Tests for Valid Parenthesis String (LeetCode 678)
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




def test_simple_valid():
    s = Solution()
    assert s.checkValidString("()") == True

def test_star_as_open():
    s = Solution()
    assert s.checkValidString("(*)") == True

def test_star_as_close():
    s = Solution()
    assert s.checkValidString("(*))") == True

def test_invalid():
    s = Solution()
    assert s.checkValidString(")(") == False

def test_all_stars():
    s = Solution()
    assert s.checkValidString("***") == True

