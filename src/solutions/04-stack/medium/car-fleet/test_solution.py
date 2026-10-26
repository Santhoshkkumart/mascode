"""
Tests for Car Fleet (LeetCode 853)
Stack / Medium
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




def test_example_1():
    s = Solution()
    assert s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3

def test_single_car():
    s = Solution()
    assert s.carFleet(10, [3], [3]) == 1

def test_all_fleet():
    s = Solution()
    assert s.carFleet(100, [0,2,4], [4,2,1]) == 1

def test_no_fleet_merge():
    s = Solution()
    assert s.carFleet(10, [0,4,8], [1,1,1]) == 3

