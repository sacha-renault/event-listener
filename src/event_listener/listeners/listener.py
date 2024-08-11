"""
This module contains the definition of the `EventListener` class, which provides
an event-driven mechanism for subscribing, unsubscribing, and invoking listeners
(or callbacks). The `EventListener` class is designed to manage a list of callable
functions or methods that can be triggered with specified arguments.

The class is particularly useful in scenarios where an event-driven architecture is
needed, such as in GUI applications, asynchronous programming, or handling custom
events in an application.
"""

from typing import List, Callable

from ..utils.event_functions import (
    _safe_invoke)
from ..exceptions.exceptions import NotCallableException

class EventListener:
    def __init__(self, 
                name: str = None) -> None:
        """
        Initializes the `EventListener` instance.

        Args:
            name (str, optional): The name of the event listener. This is useful
            for identifying the event listener in more complex applications..
        """
        # Init the list of __listeners
        self.__listeners: List[Callable] = []

        # Init name
        self.name = name

    @property
    def listeners(self) -> List[Callable]:
        """get the list off all the listeners subscribed to this event.
        """
        return self.__listeners

    def subscribe(self, callback : Callable) -> None:
        """subscribe a callable to this event

        Args:
            callback (Callable): a callable that will subscribe to the event
            i.e. be called with `cls.invoke(*args, **kwargs)`

        Raises:
            NotCallableException: the argument isn't a callable
            WrongSignatureException: the signature of the callable doesn't match
            the specified signature
        """
        # Check if object is callable
        if not callable(callback):
            raise NotCallableException(
                "Callback must be a callable (e.g., a function or a method).")
        
        # Add the callback in the listeners list
        if callback not in self.listeners:
            self.listeners.append(callback)

    def subscribe_many(self, *callbacks: Callable) -> None:
        """
        Subscribes multiple callback functions to an event or listener.
        Each callback will be individually subscribed using the `subscribe` method of the class.

        Args:
            *callbacks (Callable): A variable number of callback functions to be subscribed. 
            Each should be a callable that will be invoked when the event occurs 
            or the listener is triggered.
        """
        for callback in callbacks:
            self.subscribe(callback)

    def unsubscribe(self, callback: Callable) -> None:
        """Unsubscribe a function from the event listener.

        Args:
            callback (Callable): the callable that should be cleared from the 
            list of listeners.
        """
        if callback in self.listeners: 
            self.listeners.remove(callback)

    def unsubscribe_many(self, *callbacks: Callable) -> None:
        """
        Unsubscribes multiple callback functions to an event or listener.
        Each callback will be individually unsubscribed using the `unsubscribe` 
        method of the class.

        Args:
            *callbacks (Callable): A variable number of callback functions to be unsubscribed. 
        """
        for callback in callbacks:
            self.unsubscribe(callback)

    def clear(self) -> None:
        """Clear all callback from the listeners list.
        """
        self.listeners.clear()

    def invoke(self, *args, **kwargs) -> None:
        """
        Invokes all registered listener callbacks in the current thread with the provided argument.

        This method iterates over all registered listeners, passing the provided 
        positional and keyword arguments.

        Args:
            *args: Variable length argument list passed to each listener.
            **kwargs: Arbitrary keyword arguments passed to each listener.

        Notes:
        - Each listener is executed sequentially in the current thread.
        - The method does not return until all listeners have been executed.
        """
        for listener in self.listeners:
            _safe_invoke(listener, *args, **kwargs)
                