"""
Tests for Min Stack (LeetCode 155)
Stack / Medium
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
MinStack = _solution_mod.MinStack




def test_min_stack_basic():
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2

def test_min_stack_single():
    ms = MinStack()
    ms.push(5)
    assert ms.top() == 5
    assert ms.getMin() == 5

def test_min_stack_pop_updates_min():
    ms = MinStack()
    ms.push(1)
    ms.push(2)
    ms.push(0)
    assert ms.getMin() == 0
    ms.pop()
    assert ms.getMin() == 1

