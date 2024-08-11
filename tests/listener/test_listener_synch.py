from unittest.mock import Mock
import pytest
import time
from src.event_listener.listeners import EventListener
from src.event_listener.exceptions.exceptions import NotCallableException

def func1():
    ...

def func2(): 
    ...

def test_subscribe():
    event = EventListener()
    event.subscribe(func1)
    event.subscribe(func1)
    event.subscribe(func2)
    assert func1 in event.listeners
    assert func2 in event.listeners
    assert len(event.listeners) == 2
    event.clear()
    assert len(event.listeners) == 0

def test_subscribe_many():
    event = EventListener()
    event.subscribe_many(func1, func2)
    assert func1 in event.listeners
    assert func2 in event.listeners

def test_unsubscribe():
    event = EventListener()
    event.subscribe_many(func1, func2)
    assert func1 in event.listeners
    assert func2 in event.listeners
    event.unsubscribe(func1)
    assert func1 not in event.listeners

def test_unsubscribe_many():
    event = EventListener()
    event.subscribe_many(func1, func2)
    assert func1 in event.listeners
    assert func2 in event.listeners
    event.unsubscribe_many(func1, func2)
    assert func1 not in event.listeners
    assert func2 not in event.listeners

def test_invoke():
    event = EventListener()

    # Create mock functions
    mock_listener1 = Mock()
    mock_listener2 = Mock()
    
    # Sub
    event.subscribe_many(mock_listener1, mock_listener2)
    event.invoke()

    # Assert functions were called
    mock_listener1.assert_called_once()
    mock_listener2.assert_called_once()

def test_subscribe_not_callable():
    event = EventListener()
    
    # Sub
    with pytest.raises(NotCallableException):
        event.subscribe("Anything not callable")

def test_sequential():
    event = EventListener()

    func1_timer_end = None
    def func1(*args):
        time.sleep(0.2)
        nonlocal func1_timer_end
        func1_timer_end = time.time()
        

    func2_timer_end = None
    def func2(*args):
        time.sleep(0.1)
        nonlocal func2_timer_end
        func2_timer_end = time.time()
        

    func3_timer_end = None
    def func3(*args):
        nonlocal func3_timer_end
        func3_timer_end = time.time()

    event.subscribe_many(func1, func2, func3)
    event.invoke()
    assert func1_timer_end < func2_timer_end
    assert func2_timer_end < func3_timer_end