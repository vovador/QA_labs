import pytest
from utils.helpers import format_string, process_data

def test_format_string():
    assert format_string("hello") == "HELLO"
    assert format_string("world") == "WORLD"

def test_process_data():
    assert set(process_data([1, 2, 2, 3])) == {1, 2, 3}
    assert set(process_data(["a", "b", "a"])) == {"a", "b"}
