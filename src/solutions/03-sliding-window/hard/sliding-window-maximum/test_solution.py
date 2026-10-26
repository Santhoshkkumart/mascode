"""
Tests for Sliding Window Maximum (LeetCode 239)
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




def test_max_sliding_window_basic():
    s = Solution()
    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

def test_max_sliding_window_single():
    s = Solution()
    assert s.maxSlidingWindow([1], 1) == [1]

def test_max_sliding_window_full_window():
    s = Solution()
    assert s.maxSlidingWindow([1, 2, 3, 4], 4) == [4]

def test_max_sliding_window_decreasing():
    s = Solution()
    assert s.maxSlidingWindow([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]

