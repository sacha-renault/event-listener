""" utils functions for listener """
from typing import Callable, Tuple, Any, List, get_origin, get_args
import inspect
from inspect import Parameter, _empty

def _safe_invoke(self, listener: Callable, *args, **kwargs) -> None:
    try:
        listener(*args, **kwargs)
    except Exception as e:
        print(f"Exception occurred during listener callback: {e}")

def _get_signature(func: Callable) -> List[Parameter]:
    return [param for param in inspect.signature(func).parameters.values()]

def _is_signature_match(base_signature: List[Parameter], callback_signature: List[Parameter]) -> bool:
    if base_signature is None:
        return True # bypass the type check
    
    # TODO
    # There might be better things to do in this function
    # For example, some positional args could be inlcuided in the *args 
    # and keyword argument only could be included in the **kwargs
    # So a good thing to do would have multiple _is_signature_match policies
    # (Strict, Moderate, None)
    # Right now, the current implementation is strict.+
    if len(base_signature) != len(callback_signature):
        return False
    
    # Else check for every parameter
    for base_param, callback_param in zip(base_signature, callback_signature): 
        # Check if parameters are of the same kind
        if base_param.kind == callback_param.kind:

            # Check if both have a default value
            if (base_param.default is _empty) != (callback_param.default is _empty):
                return False

            # Check if parameters type
            if base_param.annotation is not _empty and callback_param.annotation is not _empty:
                
                # Get the base type for comparison
                base_origin = get_origin(base_param.annotation) or base_param.annotation
                callback_origin = get_origin(callback_param.annotation) or callback_param.annotation
                
                if base_origin != callback_origin:
                    return False
                
                # Check for generic type parameters if both are generic
                if get_args(base_param.annotation) != get_args(callback_param.annotation):
                    return False
        else:
            return False
    return True

def test_function(arg1 : int, arg2 : float, *args, papap: Callable, pipo: Tuple = None, **kwargs):
    pass

def test_function2(arg1: int, arg2 : float, *args, papap: Callable, pipo: tuple = None, **kwargs):
    pass

if __name__ == "__main__":
    s1 = _get_signature(test_function)
    s2 = _get_signature(test_function2)
    print(_is_signature_match(s1, s2))

