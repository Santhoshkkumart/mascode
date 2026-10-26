"""
Tests for Detect Squares (LeetCode 2013)
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
DetectSquares = _solution_mod.DetectSquares




def test_basic_count():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    assert ds.count([11, 10]) == 1

def test_duplicate_points():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    ds.add([11, 2])
    assert ds.count([11, 10]) == 2

def test_no_square():
    ds = DetectSquares()
    ds.add([1, 1])
    ds.add([2, 2])
    assert ds.count([1, 2]) == 0

def test_add_duplicate():
    ds = DetectSquares()
    ds.add([1, 1])
    ds.add([1, 1])
    ds.add([2, 2])
    ds.add([2, 1])
    assert ds.count([1, 2]) == 2

