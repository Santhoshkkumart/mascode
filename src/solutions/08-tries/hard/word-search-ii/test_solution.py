"""
Tests for Word Search II (LeetCode 212)
Tries / Hard
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




def test_word_search_ii_basic():
    s = Solution()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    result = sorted(s.findWords(board, words))
    assert result == ["eat", "oath"]

def test_word_search_ii_none():
    s = Solution()
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    assert s.findWords(board, words) == []

def test_word_search_ii_single():
    s = Solution()
    board = [["a"]]
    words = ["a"]
    assert s.findWords(board, words) == ["a"]

def test_word_search_ii_duplicates_handling():
    s = Solution()
    board = [["a", "b"], ["c", "d"]]
    words = ["abdc", "abcd"]
    result = sorted(s.findWords(board, words))
    assert result == ["abdc"]

