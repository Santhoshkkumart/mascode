"""
Tests for Alien Dictionary (LeetCode 269)
Advanced Graphs / Hard
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




def _valid(order, words):
    pos = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        min_len = min(len(a), len(b))
        if a[:min_len] == b[:min_len] and len(a) > len(b):
            return False
        for j in range(min_len):
            if a[j] != b[j]:
                if pos.get(a[j], -1) > pos.get(b[j], -1):
                    return False
                break
    return True

def test_example_one():
    s = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    result = s.alienOrder(words)
    assert set(result) == set("wertf")
    assert _valid(result, words)

def test_example_two():
    s = Solution()
    result = s.alienOrder(["z", "x"])
    assert _valid(result, ["z", "x"])

def test_cycle():
    s = Solution()
    assert s.alienOrder(["z", "x", "z"]) == ""

