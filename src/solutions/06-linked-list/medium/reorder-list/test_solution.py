"""
Tests for Reorder List (LeetCode 143)
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


def test_even_length():
    s = Solution()
    head = build_linked_list([1,2,3,4])
    s.reorderList(head)
    assert linked_list_to_array(head) == [1,4,2,3]

def test_odd_length():
    s = Solution()
    head = build_linked_list([1,2,3,4,5])
    s.reorderList(head)
    assert linked_list_to_array(head) == [1,5,2,4,3]

def test_single_node():
    s = Solution()
    head = build_linked_list([1])
    s.reorderList(head)
    assert linked_list_to_array(head) == [1]

