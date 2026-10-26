"""
Tests for Trapping Rain Water (LeetCode 42)
Two Pointers / Hard
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




def test_trap_basic():
    s = Solution()
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

def test_trap_second_example():
    s = Solution()
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9

def test_trap_flat():
    s = Solution()
    assert s.trap([0, 0, 0, 0]) == 0

def test_trap_single():
    s = Solution()
    assert s.trap([5]) == 0

