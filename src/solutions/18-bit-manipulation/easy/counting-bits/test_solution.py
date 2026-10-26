"""
Tests for Counting Bits (LeetCode 338)
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




def test_n_equals_two():
    s = Solution()
    assert s.countBits(2) == [0, 1, 1]

def test_n_equals_five():
    s = Solution()
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]

def test_n_equals_zero():
    s = Solution()
    assert s.countBits(0) == [0]

def test_n_equals_ten():
    s = Solution()
    assert s.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

