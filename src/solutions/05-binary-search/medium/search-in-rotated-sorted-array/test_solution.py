"""
Tests for Search in Rotated Sorted Array (LeetCode 33)
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
    assert s.search([4,5,6,7,0,1,2], 0) == 4

def test_not_found():
    s = Solution()
    assert s.search([4,5,6,7,0,1,2], 3) == -1

def test_single_not_found():
    s = Solution()
    assert s.search([1], 0) == -1

def test_single_found():
    s = Solution()
    assert s.search([1], 1) == 0

