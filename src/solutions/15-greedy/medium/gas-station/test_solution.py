"""
Tests for Gas Station (LeetCode 134)
Greedy / Medium
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




def test_valid_circuit():
    s = Solution()
    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

def test_impossible():
    s = Solution()
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1

def test_single_station():
    s = Solution()
    assert s.canCompleteCircuit([5], [4]) == 0

def test_start_at_zero():
    s = Solution()
    assert s.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 4, 4, 4]) == -1

