"""
Tests for Top K Frequent Elements (LeetCode 347)
Arrays & Hashing / Medium
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




def test_top_k_frequent_basic():
    s = Solution()
    result = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2]

def test_top_k_frequent_single():
    s = Solution()
    result = s.topKFrequent([1], 1)
    assert result == [1]

def test_top_k_frequent_all_unique():
    s = Solution()
    result = s.topKFrequent([1, 2, 2, 3, 3, 3], 3)
    assert sorted(result) == [1, 2, 3]

