"""
Tests for Add Two Numbers (LeetCode 2)
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


def test_basic_addition():
    s = Solution()
    l1 = build_linked_list([2,4,3])
    l2 = build_linked_list([5,6,4])
    result = s.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [7,0,8]

def test_zeros():
    s = Solution()
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = s.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [0]

def test_carry_overflow():
    s = Solution()
    l1 = build_linked_list([9,9,9,9,9,9,9])
    l2 = build_linked_list([9,9,9,9])
    result = s.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [8,9,9,9,0,0,0,1]

