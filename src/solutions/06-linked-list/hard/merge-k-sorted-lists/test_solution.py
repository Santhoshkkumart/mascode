"""
Tests for Merge k Sorted Lists (LeetCode 23)
Linked List / Hard
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


def test_merge_three_lists():
    s = Solution()
    lists = [
        build_linked_list([1,4,5]),
        build_linked_list([1,3,4]),
        build_linked_list([2,6]),
    ]
    result = s.mergeKLists(lists)
    assert linked_list_to_array(result) == [1,1,2,3,4,4,5,6]

def test_merge_empty():
    s = Solution()
    result = s.mergeKLists([])
    assert linked_list_to_array(result) == []

def test_merge_all_empty():
    s = Solution()
    result = s.mergeKLists([build_linked_list([])])
    assert linked_list_to_array(result) == []

def test_merge_single_list():
    s = Solution()
    lists = [build_linked_list([1,2,3])]
    result = s.mergeKLists(lists)
    assert linked_list_to_array(result) == [1,2,3]

