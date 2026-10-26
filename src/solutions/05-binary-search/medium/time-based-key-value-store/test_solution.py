"""
Tests for Time Based Key-Value Store (LeetCode 981)
Binary Search / Medium
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
TimeMap = _solution_mod.TimeMap




def test_basic_operations():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"

def test_multiple_values():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

def test_no_value_before_timestamp():
    tm = TimeMap()
    tm.set("foo", "bar", 5)
    assert tm.get("foo", 1) == ""

def test_key_not_found():
    tm = TimeMap()
    assert tm.get("missing", 10) == ""

