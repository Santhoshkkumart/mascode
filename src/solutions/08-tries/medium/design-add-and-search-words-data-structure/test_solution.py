"""
Tests for Design Add and Search Words Data Structure (LeetCode 211)
Tries / Medium
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
WordDictionary = _solution_mod.WordDictionary




def test_word_dict_basic():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True

def test_word_dict_empty():
    wd = WordDictionary()
    assert wd.search("a") is False

def test_word_dict_wildcard_all():
    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("b")
    assert wd.search(".") is True
    assert wd.search("a") is True
    assert wd.search("c") is False

def test_word_dict_longer():
    wd = WordDictionary()
    wd.addWord("at")
    wd.addWord("and")
    wd.addWord("an")
    wd.addWord("add")
    assert wd.search("a") is False
    assert wd.search(".at") is False
    assert wd.search("an.") is True

