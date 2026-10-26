"""
Tests for Number of Connected Components in an Undirected Graph (LeetCode 323)
Graphs / Medium
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




def test_two_components():
    s = Solution()
    assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2

def test_single_component():
    s = Solution()
    assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1

def test_no_edges():
    s = Solution()
    assert s.countComponents(4, []) == 4

