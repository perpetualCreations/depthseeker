"""
Interfacing with AbuseIPDB API.
"""

from interface import objects

def check(address):
    """
    Checks address for reports through AbuseIPDB API, formats returning JSON automatically.
    :param address: address for check.
    :return: integer being the number of reports in the last 28 days.
    """
    objects.api_inteface.check(ip_address = address, max_age_in_days = 28)
pass

def report(address, category, comments):
    """
    Wrapper function merely for completeness, reports address through AbuseIPDB API.
    :param address: address to report.
    :param category: category report is under, as a list.
    :param comments: additional report comments.
    :return: none.
    """
    objects.api_interface.report(ip_address = address, categories = category, comment = comments)
pass
