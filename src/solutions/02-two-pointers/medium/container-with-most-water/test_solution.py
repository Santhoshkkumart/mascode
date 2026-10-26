"""
Tests for Container With Most Water (LeetCode 11)
Two Pointers / Medium
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




def test_max_area_basic():
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_max_area_two_lines():
    s = Solution()
    assert s.maxArea([1, 1]) == 1

def test_max_area_decreasing():
    s = Solution()
    assert s.maxArea([4, 3, 2, 1]) == 4

