"""
Tests for Copy List with Random Pointer (LeetCode 138)
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
Node = _solution_mod.Node
Node = _solution_mod.Node

from lib import build_linked_list, linked_list_to_array


def test_copy_with_random():
    s = Solution()
    # Build list: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # Node imported via importlib above
    n0 = Node(7)
    n1 = Node(13)
    n2 = Node(11)
    n3 = Node(10)
    n4 = Node(1)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n0.random = None
    n1.random = n0
    n2.random = n4
    n3.random = n2
    n4.random = n0
    result = s.copyRandomList(n0)
    # Verify values and structure
    assert result.val == 7
    assert result.random is None
    assert result.next.val == 13
    assert result.next.random.val == 7
    assert result.next.next.next.next.val == 1
    assert result.next.next.next.next.random.val == 7

def test_copy_empty():
    s = Solution()
    assert s.copyRandomList(None) is None

def test_copy_single():
    s = Solution()
    # Node imported via importlib above
    node = Node(5)
    node.random = node
    result = s.copyRandomList(node)
    assert result.val == 5
    assert result.random is result
    assert result is not node

