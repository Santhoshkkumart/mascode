"""
Tests for Kth Largest Element in an Array (LeetCode 215)
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




def test_kth_largest_basic():
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

def test_kth_largest_duplicates():
    s = Solution()
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

def test_kth_largest_single():
    s = Solution()
    assert s.findKthLargest([1], 1) == 1

def test_kth_largest_largest():
    s = Solution()
    assert s.findKthLargest([3, 1, 2, 4], 1) == 4

