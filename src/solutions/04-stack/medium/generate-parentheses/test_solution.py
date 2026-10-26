"""
Tests for Generate Parentheses (LeetCode 22)
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




def test_n_equals_3():
    s = Solution()
    result = s.generateParenthesis(3)
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    assert sorted(result) == sorted(expected)

def test_n_equals_1():
    s = Solution()
    result = s.generateParenthesis(1)
    assert result == ["()"]

def test_n_equals_2():
    s = Solution()
    result = s.generateParenthesis(2)
    expected = ["(())","()()"]
    assert sorted(result) == sorted(expected)

