"""
Tests for Min Cost Climbing Stairs (LeetCode 746)
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




def test_example_one():
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15

def test_example_two():
    s = Solution()
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

def test_two_elements():
    s = Solution()
    assert s.minCostClimbingStairs([10, 15]) == 10

