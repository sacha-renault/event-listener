from unittest.mock import Mock
import time
import pytest
from src.event_listener.listeners import EventListenerAsync

def test_not_sequential():
    event = EventListenerAsync()

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
    event.invoke_async()
    assert func3_timer_end < func2_timer_end
    assert func2_timer_end < func1_timer_end