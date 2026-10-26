"""
Tests for Clone Graph (LeetCode 133)
Graphs / Medium
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

from lib import build_graph, graph_to_adjacency


def test_clone_four_nodes():
    s = Solution()
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = build_graph(adj)
    cloned = s.cloneGraph(node)
    assert graph_to_adjacency(cloned) == adj

def test_clone_single_node():
    s = Solution()
    adj = [[]]
    node = build_graph(adj)
    cloned = s.cloneGraph(node)
    assert graph_to_adjacency(cloned) == adj

def test_clone_empty():
    s = Solution()
    assert s.cloneGraph(None) is None

