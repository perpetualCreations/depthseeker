"""
friendlyfire module, in interface module.
Prevents request reports from IPs listed in safe.list.
As the module name suggests, this is to prevent friendly fire.
"""

from interface import objects

def check(address):
    """
    Checks if given address is in the list of safe IPs.
    If return is True, address is safe and should not be reported.
    :param address:
    :return: bool
    """
    if address in objects.safe_list:
        return True
    else:
        return False
    pass
pass
