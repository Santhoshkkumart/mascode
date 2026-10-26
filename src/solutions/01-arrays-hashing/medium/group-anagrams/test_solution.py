"""
Tests for Group Anagrams (LeetCode 49)
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




def test_group_anagrams_basic():
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort each group and the overall list for comparison
    sorted_result = sorted([sorted(g) for g in result])
    expected = sorted([["ate", "eat", "tea"], ["nat", "tan"], ["bat"]])
    assert sorted_result == expected

def test_group_anagrams_empty_string():
    s = Solution()
    result = s.groupAnagrams([""])
    assert result == [[""]]

def test_group_anagrams_single_char():
    s = Solution()
    result = s.groupAnagrams(["a"])
    assert result == [["a"]]

