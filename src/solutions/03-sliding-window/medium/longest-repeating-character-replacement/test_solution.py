"""
Tests for Longest Repeating Character Replacement (LeetCode 424)
Sliding Window / Medium
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




def test_character_replacement_basic():
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4

def test_character_replacement_second():
    s = Solution()
    assert s.characterReplacement("AABABBA", 1) == 4

def test_character_replacement_no_replacements():
    s = Solution()
    assert s.characterReplacement("ABCD", 0) == 1

def test_character_replacement_all_same():
    s = Solution()
    assert s.characterReplacement("AAAA", 2) == 4

