"""
Tests for Kth Largest Element in a Stream (LeetCode 703)
Heap / Priority Queue / Easy
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
KthLargest = _solution_mod.KthLargest




def test_kth_largest_basic():
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8

def test_kth_largest_single():
    kth = KthLargest(1, [])
    assert kth.add(1) == 1
    assert kth.add(2) == 2

def test_kth_largest_empty_init():
    kth = KthLargest(2, [0])
    assert kth.add(-1) == -1
    assert kth.add(1) == 0
    assert kth.add(-2) == 0

def test_kth_largest_all_same():
    kth = KthLargest(3, [5, 5, 5, 5])
    assert kth.add(5) == 5
    assert kth.add(1) == 5

