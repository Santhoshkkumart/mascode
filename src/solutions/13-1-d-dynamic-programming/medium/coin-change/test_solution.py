"""
Tests for Coin Change (LeetCode 322)
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




def test_example_one():
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3

def test_impossible():
    s = Solution()
    assert s.coinChange([2], 3) == -1

def test_zero_amount():
    s = Solution()
    assert s.coinChange([1], 0) == 0

def test_single_coin_type():
    s = Solution()
    assert s.coinChange([1], 5) == 5

