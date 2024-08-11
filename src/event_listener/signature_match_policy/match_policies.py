from enum import auto, Enum
from inspect import Parameter
from typing import List

from .sub_functions import _is_signature_match_strict
from ..exceptions.exceptions import UnknownCaseException

class MatchPolicy(Enum):
    NONE = auto()
    """ no need to match the signature of the function. """

    MODERATE = auto()
    """ the signature needs to match the number of argument but not the types. """

    STRICT = auto()
    """ the signature needs to match perfectlythe number of argument. """

def is_signature_match(
        base_signature: List[Parameter], 
        callback_signature: List[Parameter], 
        policy: MatchPolicy) -> bool:
    
    match policy:
        case MatchPolicy.NONE:
            return True
        
        case MatchPolicy.MODERATE:
            return True # return _is_signature_match_moderate(base_signature, callback_signature)
        
        case MatchPolicy.STRICT:
            return _is_signature_match_strict(base_signature, callback_signature)
        
        case _:
            UnknownCaseException(f"Unknown match policy : {policy}") 