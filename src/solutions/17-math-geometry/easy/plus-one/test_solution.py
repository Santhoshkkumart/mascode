"""
Tests for Plus One (LeetCode 66)
Math & Geometry / Easy
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




def test_simple_increment():
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]

def test_no_carry():
    s = Solution()
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

def test_all_nines():
    s = Solution()
    assert s.plusOne([9]) == [1, 0]

def test_multiple_nines():
    s = Solution()
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]

