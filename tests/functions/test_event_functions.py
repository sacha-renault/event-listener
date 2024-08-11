from unittest.mock import Mock
import pytest
from src.event_listener.utils.event_functions import _safe_invoke, _get_signature

def test_safe_invoke_with_exception():
    def mock_listener(*args, **kwargs):
        raise Exception("Test exception")

    # Assert that the warning is raised when _safe_invoke is called
    with pytest.warns(UserWarning):
        _safe_invoke(mock_listener)

def test_get_signature():
    def mock_listener(*args, **kwargs):
        raise Exception("Test exception")

    # Assert that the warning is raised when _safe_invoke is called
    assert len(_get_signature(mock_listener)) == 2
