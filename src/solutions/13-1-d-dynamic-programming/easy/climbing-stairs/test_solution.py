"""
Tests for Climbing Stairs (LeetCode 70)
1-D Dynamic Programming / Easy
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




def test_two_steps():
    s = Solution()
    assert s.climbStairs(2) == 2

def test_three_steps():
    s = Solution()
    assert s.climbStairs(3) == 3

def test_five_steps():
    s = Solution()
    assert s.climbStairs(5) == 8

def test_one_step():
    s = Solution()
    assert s.climbStairs(1) == 1

