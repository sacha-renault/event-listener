from typing import Callable, Tuple, Any, List
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
    for base_param, callback_param in zip(base_signature, callback_signature):
        # Check if both 
        if (base_param.default is _empty) != (callback_param.default is _empty):
            return False
    return True

for v in _get_signature(_is_signature_match):
    print(v.default)