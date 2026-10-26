"""
Tests for Encode and Decode Strings (LeetCode 271)
Arrays & Hashing / Medium
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




def test_encode_decode_basic():
    codec = Codec()
    strs = ["Hello", "World"]
    encoded = codec.encode(strs)
    assert codec.decode(encoded) == strs

def test_encode_decode_empty_list():
    codec = Codec()
    strs = []
    encoded = codec.encode(strs)
    assert codec.decode(encoded) == strs

def test_encode_decode_empty_string():
    codec = Codec()
    strs = [""]
    encoded = codec.encode(strs)
    assert codec.decode(encoded) == strs

def test_encode_decode_special_chars():
    codec = Codec()
    strs = ["abc#def", "123#456", ""]
    encoded = codec.encode(strs)
    assert codec.decode(encoded) == strs

