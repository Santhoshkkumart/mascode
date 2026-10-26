"""
Tests for Set Matrix Zeroes (LeetCode 73)
Math & Geometry / Medium
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




def test_single_zero():
    s = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

def test_corner_zeros():
    s = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

def test_no_zeros():
    s = Solution()
    matrix = [[1, 2], [3, 4]]
    s.setZeroes(matrix)
    assert matrix == [[1, 2], [3, 4]]

