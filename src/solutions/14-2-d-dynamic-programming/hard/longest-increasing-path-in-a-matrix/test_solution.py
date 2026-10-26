"""
Tests for Longest Increasing Path in a Matrix (LeetCode 329)
2-D Dynamic Programming / Hard
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
    assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4

def test_example_two():
    s = Solution()
    assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4

def test_single_cell():
    s = Solution()
    assert s.longestIncreasingPath([[1]]) == 1

def test_all_same():
    s = Solution()
    assert s.longestIncreasingPath([[1, 1], [1, 1]]) == 1

