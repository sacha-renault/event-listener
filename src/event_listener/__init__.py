from .listeners import EventListener, EventListenerAsync

try:
    from ._version import VERSION as __version__
except:
    __version__ = "0.0.0"