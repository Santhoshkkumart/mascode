"""
Tests for Contains Duplicate (LeetCode 217)
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




def test_contains_duplicate_true():
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) == True

def test_no_duplicate():
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 4]) == False

def test_many_duplicates():
    s = Solution()
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

def test_single_element():
    s = Solution()
    assert s.containsDuplicate([1]) == False

