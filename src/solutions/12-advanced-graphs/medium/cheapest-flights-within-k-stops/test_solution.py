"""
Tests for Cheapest Flights Within K Stops (LeetCode 787)
Advanced Graphs / Medium
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




def test_one_stop_cheaper():
    s = Solution()
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert s.findCheapestPrice(n, flights, 0, 3, 1) == 700

def test_direct_vs_one_stop():
    s = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert s.findCheapestPrice(3, flights, 0, 2, 1) == 200

def test_zero_stops_forces_direct():
    s = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert s.findCheapestPrice(3, flights, 0, 2, 0) == 500

def test_no_route():
    s = Solution()
    assert s.findCheapestPrice(3, [[0, 1, 100]], 0, 2, 1) == -1

