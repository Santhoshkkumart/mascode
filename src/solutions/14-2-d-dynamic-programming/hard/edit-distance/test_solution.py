"""
Tests for Edit Distance (LeetCode 72)
2-D Dynamic Programming / Hard
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




def test_horse_ros():
    s = Solution()
    assert s.minDistance("horse", "ros") == 3

def test_intention_execution():
    s = Solution()
    assert s.minDistance("intention", "execution") == 5

def test_empty_word1():
    s = Solution()
    assert s.minDistance("", "abc") == 3

def test_same_words():
    s = Solution()
    assert s.minDistance("abc", "abc") == 0

