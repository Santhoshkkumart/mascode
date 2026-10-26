"""
Tests for Reverse Nodes in k-Group (LeetCode 25)
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


def test_k_equals_2():
    s = Solution()
    head = build_linked_list([1,2,3,4,5])
    result = s.reverseKGroup(head, 2)
    assert linked_list_to_array(result) == [2,1,4,3,5]

def test_k_equals_3():
    s = Solution()
    head = build_linked_list([1,2,3,4,5])
    result = s.reverseKGroup(head, 3)
    assert linked_list_to_array(result) == [3,2,1,4,5]

def test_k_equals_1():
    s = Solution()
    head = build_linked_list([1,2,3])
    result = s.reverseKGroup(head, 1)
    assert linked_list_to_array(result) == [1,2,3]

def test_k_equals_length():
    s = Solution()
    head = build_linked_list([1,2,3,4])
    result = s.reverseKGroup(head, 4)
    assert linked_list_to_array(result) == [4,3,2,1]

