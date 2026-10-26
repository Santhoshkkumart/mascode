"""
Tests for Missing Number (LeetCode 268)
Bit Manipulation / Easy
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




def test_missing_middle():
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2

def test_missing_last():
    s = Solution()
    assert s.missingNumber([0, 1]) == 2

def test_missing_eight():
    s = Solution()
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

def test_missing_zero():
    s = Solution()
    assert s.missingNumber([1]) == 0

