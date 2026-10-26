"""
Tests for Search a 2D Matrix (LeetCode 74)
Binary Search / Medium
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




def test_found():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True

def test_not_found():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False

def test_first_element():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1) == True

def test_last_element():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60) == True

