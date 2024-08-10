from typing import Callable, Tuple, Any, List, get_type_hints
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
    
    # Else check for every parameter
    # TODO zip makes the check on the shortest ... it can lead to errors ...
    for base_param, callback_param in zip(base_signature, callback_signature): 
        # Check if param are same kind
        if base_param.kind == callback_param.kind:

            # Check if both have a default value
            if (base_param.default is _empty) != (callback_param.default is _empty):
                return False

            # Check if params type !
            # TODO
        else:
            return False
    return True

def test_function(arg1 : int, arg2 : float, *args, papap: Callable, pipo: List = None, **kwargs):
    pass

def test_function2(arg1, arg2 : float, *args, papap: Callable, pipo: List = None):
    pass

if __name__ == "__main__":
    s1 = _get_signature(test_function)
    s2 = _get_signature(test_function2)
    print(_is_signature_match(s1, s2))


