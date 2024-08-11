""" 
This module store the exception used in the package
"""

class EventListenerException(Exception):
    """ Base library exception """
    pass

class WrongSignatureException(EventListenerException):
    """ Exception triggered when the signature of two callable doesn't match
    """
    pass

class NotCallableException(EventListenerException):
    """ Exception triggered when the object isn't a callable object. """
    pass

class UnknownCaseException(EventListenerException):
    """ The switch case arrived in an unknown state, 
    probably something wrong was passed in argument. """
    pass