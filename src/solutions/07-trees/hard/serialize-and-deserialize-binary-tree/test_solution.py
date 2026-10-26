"""
Tests for Serialize and Deserialize Binary Tree (LeetCode 297)
Trees / Hard
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
Codec = _solution_mod.Codec

from lib import build_tree, tree_to_array


def test_serialize_deserialize_basic():
    ser = Codec()
    deser = Codec()
    root = build_tree([1, 2, 3, None, None, 4, 5])
    tree = deser.deserialize(ser.serialize(root))
    assert tree_to_array(tree) == [1, 2, 3, None, None, 4, 5]

def test_serialize_deserialize_empty():
    ser = Codec()
    deser = Codec()
    tree = deser.deserialize(ser.serialize(None))
    assert tree is None

def test_serialize_deserialize_single():
    ser = Codec()
    deser = Codec()
    root = build_tree([1])
    tree = deser.deserialize(ser.serialize(root))
    assert tree_to_array(tree) == [1]

def test_serialize_deserialize_complex():
    ser = Codec()
    deser = Codec()
    root = build_tree([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5])
    tree = deser.deserialize(ser.serialize(root))
    assert tree_to_array(tree) == tree_to_array(root)

