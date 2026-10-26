"""
Tests for Min Cost to Connect All Points (LeetCode 1584)
Advanced Graphs / Medium
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
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert s.minCostConnectPoints(points) == 20

def test_example_two():
    s = Solution()
    points = [[3, 12], [-2, 5], [-4, 1]]
    assert s.minCostConnectPoints(points) == 18

def test_two_points():
    s = Solution()
    assert s.minCostConnectPoints([[0, 0], [1, 1]]) == 2

