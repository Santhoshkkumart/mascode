"""
Tests for Decode Ways (LeetCode 91)
1-D Dynamic Programming / Medium
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




def test_twelve():
    s = Solution()
    assert s.numDecodings("12") == 2

def test_two_two_six():
    s = Solution()
    assert s.numDecodings("226") == 3

def test_leading_zero():
    s = Solution()
    assert s.numDecodings("06") == 0

def test_single_digit():
    s = Solution()
    assert s.numDecodings("1") == 1

def test_ten():
    s = Solution()
    assert s.numDecodings("10") == 1

