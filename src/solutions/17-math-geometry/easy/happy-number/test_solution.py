"""
Tests for Happy Number (LeetCode 202)
Math & Geometry / Easy
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




def test_happy_number():
    s = Solution()
    assert s.isHappy(19) == True

def test_unhappy_number():
    s = Solution()
    assert s.isHappy(2) == False

def test_one():
    s = Solution()
    assert s.isHappy(1) == True

def test_seven():
    s = Solution()
    assert s.isHappy(7) == True

