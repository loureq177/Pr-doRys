"""
This type stub file was generated by pyright.
"""

from datetime import datetime

def datetime_exists(dt):
    """Check if a datetime exists. Taken from: https://pytz-deprecation-shim.readthedocs.io/en/latest/migration.html"""
    ...

def datetime_ambiguous(dt: datetime): # -> bool:
    """Check whether a datetime is ambiguous. Taken from: https://pytz-deprecation-shim.readthedocs.io/en/latest/migration.html"""
    ...

def valid_datetime(dt): # -> bool:
    """Returns True if the datetime is not ambiguous or imaginary, False otherwise."""
    ...

