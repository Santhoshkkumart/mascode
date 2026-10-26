"""
Tests for Meeting Rooms II (LeetCode 253)
Intervals / Medium
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




def test_need_two_rooms():
    s = Solution()
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2

def test_need_one_room():
    s = Solution()
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1

def test_all_overlap():
    s = Solution()
    assert s.minMeetingRooms([[1, 5], [2, 6], [3, 7]]) == 3

def test_single_meeting():
    s = Solution()
    assert s.minMeetingRooms([[1, 5]]) == 1

