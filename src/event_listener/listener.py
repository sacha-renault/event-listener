from typing import List, Callable, Optional, Union
import threading
from inspect import Parameter

from .event_functions import _safe_invoke

class EventListener:
    def __init__(self, name: str = None, signature: Union[List[Parameter], Callable, None]= None) -> None:
        self.__listeners: List[Callable] = []
        self.name = name

    def subscribe(self, callback : Callable) -> None:
        assert callable(callback), "Callback must be a callable (e.g., a function or a method)."
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

        # Optionally, wait for all threads to complete
        for thread in threads:
            thread.join()
                