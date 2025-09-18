from diamond import create_diamond
from diamond import build_string

def test_a():
    assert create_diamond("A") == "A"
    assert build_string("A", "   ") == " A "