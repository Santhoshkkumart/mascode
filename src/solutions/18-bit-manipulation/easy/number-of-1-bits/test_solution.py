"""
Tests for Number of 1 Bits (LeetCode 191)
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




def test_three_bits():
    s = Solution()
    assert s.hammingWeight(0b00000000000000000000000000001011) == 3

def test_one_bit():
    s = Solution()
    assert s.hammingWeight(0b00000000000000000000000010000000) == 1

def test_zero():
    s = Solution()
    assert s.hammingWeight(0) == 0

def test_all_ones():
    s = Solution()
    assert s.hammingWeight(0b11111111111111111111111111111101) == 31

