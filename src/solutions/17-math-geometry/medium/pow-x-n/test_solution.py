"""
Tests for Pow(x, n) (LeetCode 50)
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




def test_positive_power():
    s = Solution()
    result = s.myPow(2.0, 10)
    assert abs(result - 1024.0) < 0.0001

def test_fractional_base():
    s = Solution()
    result = s.myPow(2.1, 3)
    assert abs(result - 9.261) < 0.0001

def test_negative_power():
    s = Solution()
    result = s.myPow(2.0, -2)
    assert abs(result - 0.25) < 0.0001

def test_zero_power():
    s = Solution()
    result = s.myPow(2.0, 0)
    assert abs(result - 1.0) < 0.0001

