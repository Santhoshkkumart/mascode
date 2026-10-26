"""
Tests for Merge Two Sorted Lists (LeetCode 21)
Linked List / Easy
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

from lib import build_linked_list, linked_list_to_array


def test_merge_both():
    s = Solution()
    l1 = build_linked_list([1,2,4])
    l2 = build_linked_list([1,3,4])
    result = s.mergeTwoLists(l1, l2)
    assert linked_list_to_array(result) == [1,1,2,3,4,4]

def test_merge_both_empty():
    s = Solution()
    l1 = build_linked_list([])
    l2 = build_linked_list([])
    result = s.mergeTwoLists(l1, l2)
    assert linked_list_to_array(result) == []

def test_merge_one_empty():
    s = Solution()
    l1 = build_linked_list([])
    l2 = build_linked_list([0])
    result = s.mergeTwoLists(l1, l2)
    assert linked_list_to_array(result) == [0]

