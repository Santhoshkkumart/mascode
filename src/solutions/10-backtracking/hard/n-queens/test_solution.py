"""
Tests for N-Queens (LeetCode 51)
Backtracking / Hard
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




def _is_valid(board, n):
    # Check no two queens attack each other.
    cols = set()
    for r in range(n):
        c = board[r].index("Q")
        if c in cols:
            return False
        cols.add(c)
        for rr in range(n):
            if rr == r:
                continue
            cc = board[rr].index("Q")
            if abs(rr - r) == abs(cc - c):
                return False
    return True

def test_n_equals_4():
    s = Solution()
    result = s.solveNQueens(4)
    assert len(result) == 2
    for board in result:
        assert _is_valid(board, 4)

def test_n_equals_1():
    s = Solution()
    assert s.solveNQueens(1) == [["Q"]]

def test_n_equals_3_no_solution():
    s = Solution()
    assert s.solveNQueens(3) == []

