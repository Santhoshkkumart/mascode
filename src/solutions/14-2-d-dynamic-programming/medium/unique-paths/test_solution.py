"""
Tests for Unique Paths (LeetCode 62)
2-D Dynamic Programming / Medium
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




def test_three_by_seven():
    s = Solution()
    assert s.uniquePaths(3, 7) == 28

def test_three_by_two():
    s = Solution()
    assert s.uniquePaths(3, 2) == 3

def test_one_by_one():
    s = Solution()
    assert s.uniquePaths(1, 1) == 1

def test_two_by_two():
    s = Solution()
    assert s.uniquePaths(2, 2) == 2

