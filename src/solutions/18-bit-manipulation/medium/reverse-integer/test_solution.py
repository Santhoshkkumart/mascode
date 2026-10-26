"""
Tests for Reverse Integer (LeetCode 7)
Bit Manipulation / Medium
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




def test_positive():
    s = Solution()
    assert s.reverse(123) == 321

def test_negative():
    s = Solution()
    assert s.reverse(-123) == -321

def test_trailing_zero():
    s = Solution()
    assert s.reverse(120) == 21

def test_overflow():
    s = Solution()
    assert s.reverse(1534236469) == 0

