""" Module that contain the definition of the `EventListenerAsync`
class. It has same logic as the parent class `EventListener` but 
add asynchronous call of invoke. """

from typing import List
import threading
from ..utils.event_functions import _safe_invoke
from .listener import EventListener

class EventListenerAsync(EventListener):
    def invoke_async(self, *args, **kwargs) -> None:
        """
        Invokes all registered listener callbacks in separate threads with the provided arguments.

        This method iterates over all registered listeners and invokes each one in a separate thread,
        passing the provided positional and keyword arguments. The method waits for all threads to complete
        before returning, ensuring that all listeners have finished processing.

        Args:
            *args: Variable length argument list passed to each listener.
            **kwargs: Arbitrary keyword arguments passed to each listener.

        Notes:
            - Each listener is executed in its own thread, allowing for concurrent execution.
            - The method waits for all threads to complete before returning, which ensures that all
            listeners have finished their execution.
        """
        threads: List[threading.Thread] = []
        for listener in self.listeners:
            thread = threading.Thread(target=_safe_invoke, args=(listener,) + args, kwargs=kwargs)
            thread.start()
            threads.append(thread)

        # Wait all the thread to complete
        for thread in threads:
            thread.join()