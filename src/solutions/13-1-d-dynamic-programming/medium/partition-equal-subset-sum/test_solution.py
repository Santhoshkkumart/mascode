"""
Tests for Partition Equal Subset Sum (LeetCode 416)
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
    assert s.canPartition([1, 5, 11, 5]) == True

def test_example_two():
    s = Solution()
    assert s.canPartition([1, 2, 3, 5]) == False

def test_single_element():
    s = Solution()
    assert s.canPartition([1]) == False

def test_two_equal():
    s = Solution()
    assert s.canPartition([1, 1]) == True

