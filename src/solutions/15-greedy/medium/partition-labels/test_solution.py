"""
Tests for Partition Labels (LeetCode 763)
Greedy / Medium
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




def test_multiple_partitions():
    s = Solution()
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]

def test_single_partition():
    s = Solution()
    assert s.partitionLabels("eccbbbbdec") == [10]

def test_each_char_separate():
    s = Solution()
    assert s.partitionLabels("abcdef") == [1, 1, 1, 1, 1, 1]

def test_repeated_chars():
    s = Solution()
    assert s.partitionLabels("aaa") == [3]

