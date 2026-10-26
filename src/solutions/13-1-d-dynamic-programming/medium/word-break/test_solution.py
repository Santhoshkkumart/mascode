"""
Tests for Word Break (LeetCode 139)
1-D Dynamic Programming / Medium
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




def test_leetcode():
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) == True

def test_applepenapple():
    s = Solution()
    assert s.wordBreak("applepenapple", ["apple", "pen"]) == True

def test_catsandog():
    s = Solution()
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

def test_single_word():
    s = Solution()
    assert s.wordBreak("a", ["a"]) == True

