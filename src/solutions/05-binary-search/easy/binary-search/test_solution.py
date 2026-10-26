"""
Tests for Binary Search (LeetCode 704)
Binary Search / Easy
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
    assert s.search([-1,0,3,5,9,12], 9) == 4

def test_not_found():
    s = Solution()
    assert s.search([-1,0,3,5,9,12], 2) == -1

def test_first_element():
    s = Solution()
    assert s.search([1,2,3,4,5], 1) == 0

def test_single_element():
    s = Solution()
    assert s.search([5], 5) == 0

