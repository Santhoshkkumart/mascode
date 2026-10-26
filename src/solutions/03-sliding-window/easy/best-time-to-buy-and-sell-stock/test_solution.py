"""
Tests for Best Time to Buy and Sell Stock (LeetCode 121)
Sliding Window / Easy
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




def test_max_profit_basic():
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5

def test_max_profit_no_profit():
    s = Solution()
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0

def test_max_profit_single_day():
    s = Solution()
    assert s.maxProfit([5]) == 0

def test_max_profit_increasing():
    s = Solution()
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4

