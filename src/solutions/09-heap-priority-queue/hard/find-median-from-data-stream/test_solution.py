"""
Tests for Find Median from Data Stream (LeetCode 295)
Heap / Priority Queue / Hard
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
MedianFinder = _solution_mod.MedianFinder




def test_median_finder_basic():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

def test_median_finder_single():
    mf = MedianFinder()
    mf.addNum(5)
    assert mf.findMedian() == 5.0

def test_median_finder_negative():
    mf = MedianFinder()
    mf.addNum(-1)
    mf.addNum(-2)
    assert mf.findMedian() == -1.5
    mf.addNum(-3)
    assert mf.findMedian() == -2.0

def test_median_finder_order():
    mf = MedianFinder()
    for num in [6, 10, 2, 6, 5, 0, 6]:
        mf.addNum(num)
    assert mf.findMedian() == 6.0

