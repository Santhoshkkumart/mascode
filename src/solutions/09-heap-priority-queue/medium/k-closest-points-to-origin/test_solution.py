"""
Tests for K Closest Points to Origin (LeetCode 973)
Heap / Priority Queue / Medium
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




def test_k_closest_basic():
    s = Solution()
    result = s.kClosest([[1, 3], [-2, 2]], 1)
    assert sorted([sorted(p) for p in result]) == sorted([sorted([-2, 2])])

def test_k_closest_multiple():
    s = Solution()
    result = s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    result_set = set(tuple(sorted(p)) for p in result)
    expected = set(tuple(sorted(p)) for p in [[3, 3], [-2, 4]])
    assert result_set == expected

def test_k_closest_all():
    s = Solution()
    result = s.kClosest([[1, 1], [2, 2], [3, 3]], 3)
    result_set = set(tuple(p) for p in result)
    expected = set(tuple(p) for p in [[1, 1], [2, 2], [3, 3]])
    assert result_set == expected

def test_k_closest_origin():
    s = Solution()
    result = s.kClosest([[0, 1], [1, 0]], 1)
    assert len(result) == 1

