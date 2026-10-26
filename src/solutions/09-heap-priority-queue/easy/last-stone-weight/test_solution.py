"""
Tests for Last Stone Weight (LeetCode 1046)
Heap / Priority Queue / Easy
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




def test_last_stone_weight_basic():
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

def test_last_stone_weight_single():
    s = Solution()
    assert s.lastStoneWeight([1]) == 1

def test_last_stone_weight_all_destroyed():
    s = Solution()
    assert s.lastStoneWeight([2, 2]) == 0

def test_last_stone_weight_two_diff():
    s = Solution()
    assert s.lastStoneWeight([10, 3]) == 7

