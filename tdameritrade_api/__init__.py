##-----------------------------##
## TDAmeritrade PyAPI          ##
## Written By: Ryan Smith      ##
##-----------------------------##

## Imports
from .profile import Profile

## Constants
__author__ = "Ryan Smith"
__project__ = "TDAmeritrade PyAPI"
__version__ = (1, 0, 0)
__all__ = [
    Profile
]


## Functions
def get_version_string() -> str:
    """Returns project version as a string"""
    return ".".join([str(i) for i in __version__])
