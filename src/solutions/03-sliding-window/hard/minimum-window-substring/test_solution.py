"""
Tests for Minimum Window Substring (LeetCode 76)
Sliding Window / Hard
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




def test_min_window_basic():
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"

def test_min_window_single_char():
    s = Solution()
    assert s.minWindow("a", "a") == "a"

def test_min_window_not_found():
    s = Solution()
    assert s.minWindow("a", "aa") == ""

def test_min_window_full_string():
    s = Solution()
    assert s.minWindow("a", "a") == "a"

