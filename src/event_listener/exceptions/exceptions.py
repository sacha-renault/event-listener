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