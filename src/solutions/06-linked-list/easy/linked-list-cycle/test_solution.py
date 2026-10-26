"""
Tests for Linked List Cycle (LeetCode 141)
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


def test_has_cycle():
    s = Solution()
    from lib import Node
    n0 = Node(3)
    n1 = Node(2)
    n2 = Node(0)
    n3 = Node(-4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1  # cycle at pos 1
    assert s.hasCycle(n0) == True

def test_no_cycle():
    s = Solution()
    head = build_linked_list([1,2,3,4])
    assert s.hasCycle(head) == False

def test_single_no_cycle():
    s = Solution()
    head = build_linked_list([1])
    assert s.hasCycle(head) == False

def test_self_cycle():
    s = Solution()
    from lib import Node
    n = Node(1)
    n.next = n
    assert s.hasCycle(n) == True

