"""UTILS
Misc helpers/utils functions
"""

# # Native # #
from time import time
from uuid import uuid4

__all__ = ("get_time", "get_uuid")


def get_time(seconds_precision=True):
    """Returns the current time as Unix/Epoch timestamp, seconds precision by default"""
    return time() if not seconds_precision else int(time())


def get_uuid():
    """Returns an unique UUID (UUID4)"""
    return str(uuid4())