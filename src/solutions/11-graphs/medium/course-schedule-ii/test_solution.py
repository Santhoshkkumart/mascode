"""
Tests for Course Schedule II (LeetCode 210)
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




def _valid_order(order, prereqs, n):
    if len(order) != n:
        return False
    pos = {c: i for i, c in enumerate(order)}
    for a, b in prereqs:
        if pos[b] > pos[a]:
            return False
    return True

def test_two_courses():
    s = Solution()
    result = s.findOrder(2, [[1, 0]])
    assert _valid_order(result, [[1, 0]], 2)

def test_four_courses():
    s = Solution()
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = s.findOrder(4, prereqs)
    assert _valid_order(result, prereqs, 4)

def test_cycle_returns_empty():
    s = Solution()
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []

