"""
Tests for Implement Trie (Prefix Tree) (LeetCode 208)
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
Trie = _solution_mod.Trie




def test_trie_basic():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

def test_trie_insert_then_search():
    trie = Trie()
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.startsWith("app") is True

def test_trie_not_found():
    trie = Trie()
    assert trie.search("a") is False
    assert trie.startsWith("a") is False

def test_trie_multiple_words():
    trie = Trie()
    trie.insert("banana")
    trie.insert("band")
    assert trie.search("banana") is True
    assert trie.search("band") is True
    assert trie.startsWith("ban") is True
    assert trie.startsWith("bandana") is False

