"""
Tests for Task Scheduler (LeetCode 621)
Heap / Priority Queue / Medium
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




def test_task_scheduler_basic():
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8

def test_task_scheduler_no_idle():
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6

def test_task_scheduler_complex():
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16

def test_task_scheduler_single_task():
    s = Solution()
    assert s.leastInterval(["A", "A", "A"], 2) == 7

