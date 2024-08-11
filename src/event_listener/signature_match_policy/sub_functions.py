from inspect import Parameter, _empty
from typing import List, get_args, get_origin


def _is_param_match(param1: Parameter, param2: Parameter) -> bool:
    # Check if parameters are of the same kind
    if param1.kind == param2.kind:

        # Check if both have a default value
        if (param1.default is _empty) != (param2.default is _empty):
            return False

        # Check if parameters type
        if param1.annotation is not _empty and param2.annotation is not _empty:
            
            # Get the base type for comparison
            base_origin = get_origin(param1.annotation) or param1.annotation
            callback_origin = get_origin(param2.annotation) or param2.annotation
            
            if base_origin != callback_origin:
                return False
            
            # Check for generic type parameters if both are generic
            if get_args(param1.annotation) != get_args(param2.annotation):
                return False

def _is_signature_match_strict(base_signature: List[Parameter], callback_signature: List[Parameter]) -> bool:
    """
    Compares two function signatures to determine if they match based on certain criteria.

    This function checks whether the signature of a callback function matches the signature of a base function.
    The comparison is strict and includes checking the number of parameters, the type and kind of each parameter,
    as well as whether the parameters have default values. The function returns `True` if the signatures match 
    according to these criteria, and `False` otherwise.

    Args:
        base_signature (List[Parameter]): The list of `Parameter` objects representing the signature of the base function.
        callback_signature (List[Parameter]): The list of `Parameter` objects representing the signature of the callback function.

    Returns:
        bool: `True` if the signatures match; `False` otherwise.
    """

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
        if not _is_param_match(base_param, callback_param):
            return False
    return True


def _is_signature_match_moderate(base_signature: List[Parameter], callback_signature: List[Parameter]) -> bool:
    """
    Compares two function signatures to determine if they match based on certain criteria.

    This function checks whether the signature of a callback function matches the signature of a base function.
    The comparison is strict and includes checking the number of parameters, the type and kind of each parameter,
    as well as whether the parameters have default values. The function returns `True` if the signatures match 
    according to these criteria, and `False` otherwise.

    Args:
        base_signature (List[Parameter]): The list of `Parameter` objects representing the signature of the base function.
        callback_signature (List[Parameter]): The list of `Parameter` objects representing the signature of the callback function.

    Returns:
        bool: `True` if the signatures match; `False` otherwise.
    """
    # get positional or kw
    base_positional = [p for p in base_signature if p.kind in {
        Parameter.POSITIONAL_OR_KEYWORD or Parameter.VAR_POSITIONAL}]
    callback_positional = [p for p in callback_signature if p.kind in {
        Parameter.POSITIONAL_OR_KEYWORD or Parameter.VAR_POSITIONAL}]

    # Init two pointers
    cp = bp = 0

    # iterate to see if there is match
    while bp < len(base_positional) and cp < len(callback_positional):
        if not _is_param_match(base_positional[bp], callback_positional[cp]):
            return False
        
        if bp + 1 == len(base_positional) and base_positional[bp] is Parameter.VAR_POSITIONAL:
            cp += 1
        else:
            return False
    
    return True

    

    