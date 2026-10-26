"""
Tests for Subsets II (LeetCode 90)
Backtracking / Medium
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




def test_with_duplicates():
    s = Solution()
    result = s.subsetsWithDup([1, 2, 2])
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert sorted(tuple(sorted(x)) for x in result) == sorted(tuple(sorted(x)) for x in expected)

def test_single_element():
    s = Solution()
    result = s.subsetsWithDup([0])
    expected = [[], [0]]
    assert sorted(tuple(sorted(x)) for x in result) == sorted(tuple(sorted(x)) for x in expected)

def test_all_duplicates():
    s = Solution()
    result = s.subsetsWithDup([4, 4, 4])
    expected = [[], [4], [4, 4], [4, 4, 4]]
    assert sorted(tuple(sorted(x)) for x in result) == sorted(tuple(sorted(x)) for x in expected)

