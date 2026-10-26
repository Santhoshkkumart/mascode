"""
Tests for Multiply Strings (LeetCode 43)
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
Solution = _solution_mod.Solution




def test_simple():
    s = Solution()
    assert s.multiply("2", "3") == "6"

def test_multi_digit():
    s = Solution()
    assert s.multiply("123", "456") == "56088"

def test_with_zero():
    s = Solution()
    assert s.multiply("0", "123") == "0"

def test_large_numbers():
    s = Solution()
    assert s.multiply("999", "999") == "998001"

