"""
Tests for Meeting Rooms (LeetCode 252)
Intervals / Easy
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




def test_overlap_exists():
    s = Solution()
    assert s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == False

def test_no_overlap():
    s = Solution()
    assert s.canAttendMeetings([[7, 10], [2, 4]]) == True

def test_empty():
    s = Solution()
    assert s.canAttendMeetings([]) == True

def test_touching_meetings():
    s = Solution()
    assert s.canAttendMeetings([[1, 5], [5, 10]]) == True

