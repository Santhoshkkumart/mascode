"""
Tests for Remove Nth Node From End of List (LeetCode 19)
Linked List / Medium
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


def test_remove_from_middle():
    s = Solution()
    head = build_linked_list([1,2,3,4,5])
    result = s.removeNthFromEnd(head, 2)
    assert linked_list_to_array(result) == [1,2,3,5]

def test_remove_single():
    s = Solution()
    head = build_linked_list([1])
    result = s.removeNthFromEnd(head, 1)
    assert linked_list_to_array(result) == []

def test_remove_last():
    s = Solution()
    head = build_linked_list([1,2])
    result = s.removeNthFromEnd(head, 1)
    assert linked_list_to_array(result) == [1]

def test_remove_first():
    s = Solution()
    head = build_linked_list([1,2,3])
    result = s.removeNthFromEnd(head, 3)
    assert linked_list_to_array(result) == [2,3]

