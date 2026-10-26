"""
Tests for Network Delay Time (LeetCode 743)
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
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert s.networkDelayTime(times, 4, 2) == 2

def test_single_edge():
    s = Solution()
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1

def test_unreachable():
    s = Solution()
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1

