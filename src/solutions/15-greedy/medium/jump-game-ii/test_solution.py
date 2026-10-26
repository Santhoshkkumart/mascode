"""
Tests for Jump Game II (LeetCode 45)
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




def test_basic():
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2

def test_with_zero():
    s = Solution()
    assert s.jump([2, 3, 0, 1, 4]) == 2

def test_single_element():
    s = Solution()
    assert s.jump([0]) == 0

def test_long_jump():
    s = Solution()
    assert s.jump([1, 1, 1, 1, 1]) == 4

