from typing import List, Callable, Optional, Union
import threading
from inspect import Parameter

from .event_functions import (
    _safe_invoke, 
    _is_signature_match, 
    _get_signature)

class EventListener:
    def __init__(self, 
                name: str = None, 
                signature: Union[List[Parameter], Callable, None]= None) -> None:
        
        self.__listeners: List[Callable] = []
        self.name = name
        self.signature = signature

    def subscribe(self, callback : Callable) -> None:
        # Check if object is callable
        if not callable(callback):
            raise Exception(
                "Callback must be a callable (e.g., a function or a method).")
        
        # Check if the signature match 
        if not _is_signature_match(self.signature, _get_signature(callback)):
            raise Exception(
                "Callback doesn't match the event listener signature."
                f"Expecting : {self.signature}, got : {_get_signature(callback)}")
        
        # Add the callback in the listeners list
        if callback not in self.__listeners:
            self.__listeners.append(callback)

    def unsubscribe(self, callback: Callable) -> None:
        if callback in self.__listeners: 
            self.__listeners.remove(callback)

    def clear(self) -> None:
        self.__listeners.clear()

    def invoke(self, *args, **kwargs) -> None:
        threads: List[threading.Thread] = []
        for listener in self.__listeners:
            thread = threading.Thread(target=_safe_invoke, args=(listener,) + args, kwargs=kwargs)
            thread.start()
            threads.append(thread)

        # Wait all the thread to complete
        for thread in threads:
            thread.join()
                