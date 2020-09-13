"""
Basics module, in basics module.
Handles exiting and timestamp generation.
Copied from Raspbot RCA.
"""

from basics import objects

def make_timestamp():
    """
    Generates timestamp from current UTC time.
    :return: none.
    """
    timestamp = objects.strftime("%B %d, %Y"), objects.gmtime()
    return str(timestamp[0])
pass

def exit(status):
    """
    Stops application.
    :return: none.
    """
    objects.sys.exit(status)
pass
