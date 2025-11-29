import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




from app.calc import add


def test_add():
    assert add(2,3) == 5
    assert add(3, -9) == -6
    assert add(-2, -1) == -3

