"""
Tests for Daily Temperatures (LeetCode 739)
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
Solution = _solution_mod.Solution




def test_example_1():
    s = Solution()
    assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

def test_increasing():
    s = Solution()
    assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]

def test_short():
    s = Solution()
    assert s.dailyTemperatures([30,60,90]) == [1,1,0]

def test_single():
    s = Solution()
    assert s.dailyTemperatures([50]) == [0]

