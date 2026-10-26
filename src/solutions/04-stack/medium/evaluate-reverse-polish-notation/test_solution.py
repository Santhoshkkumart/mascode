"""
Tests for Evaluate Reverse Polish Notation (LeetCode 150)
Stack / Medium
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




def test_simple_addition():
    s = Solution()
    assert s.evalRPN(["2","1","+","3","*"]) == 9

def test_division_truncation():
    s = Solution()
    assert s.evalRPN(["4","13","5","/","+"]) == 6

def test_complex_expression():
    s = Solution()
    assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

def test_single_token():
    s = Solution()
    assert s.evalRPN(["42"]) == 42

