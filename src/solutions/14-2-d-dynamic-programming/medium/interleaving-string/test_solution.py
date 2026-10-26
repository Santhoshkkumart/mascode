"""
Tests for Interleaving String (LeetCode 97)
2-D Dynamic Programming / Medium
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




def test_example_one():
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True

def test_example_two():
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False

def test_empty_strings():
    s = Solution()
    assert s.isInterleave("", "", "") == True

def test_one_empty():
    s = Solution()
    assert s.isInterleave("", "abc", "abc") == True

