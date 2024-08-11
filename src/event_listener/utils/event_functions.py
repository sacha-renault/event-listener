""" utils functions for listener """
from typing import Callable, Tuple, Any, List, get_origin, get_args
import inspect
from inspect import Parameter, _empty

def _safe_invoke(listener: Callable, *args, **kwargs) -> None:
    """
    Safely invokes a listener callback with the provided arguments, handling any exceptions that occur.

    This method attempts to call the provided listener with the given positional and keyword arguments.
    If the listener raises any exceptions during its execution, the exception is caught and logged, preventing it 
    from propagating further and potentially causing disruptions in the application.

    Args:
        listener (Callable): The listener function or method to be invoked. This should be a callable that 
                             accepts the provided arguments.
        *args: Variable length argument list passed to the listener.
        **kwargs: Arbitrary keyword arguments passed to the listener.

    Returns:
        None: This method does not return any value.

    Raises:
        None: Any exceptions raised during the listener invocation are caught and logged, not re-raised.
    """
    try:
        listener(*args, **kwargs)
    except Exception as e:
        print(f"Exception occurred during listener callback: {e}")

def _get_signature(func: Callable) -> List[Parameter]:
    """
    Retrieves the signature of a function and returns it as a list of parameters.

    Args:
        func (Callable): The function whose signature is to be retrieved.

    Returns:
        List[Parameter]: A list of `Parameter` objects representing the parameters of the function. 
                         Each `Parameter` object contains details about an individual parameter 
                         of the function, such as its name, type, and default value (if any).
    """
    return [param for param in inspect.signature(func).parameters.values()]


