"""
API module, in interface module.
Interfacing with AbuseIPDB API.
"""

from interface import objects, friendlyfire

def check(address):
    """
    Checks address for reports through AbuseIPDB API, formats returning JSON automatically.
    :param address: address for check.
    :return: list with number of reports, abuse confidence score, and time last reported as a timestamp string formatted YYYY-MM-DDTHH:MM:SS+00:00.
    """
    result = objects.api_inteface.check(ip_address = address, max_age_in_days = 182)
    return [result["totalReports"], result["abuseConfidenceScore"]]
pass

def report(address, category, comments):
    """
    Wrapper function merely for completeness, reports address through AbuseIPDB API.
    Will not report local addresses, for obvious reasons.
    :param address: address to report.
    :param category: category report is under, as a list.
    :param comments: additional report comments.
    :return: none.
    """
    if objects.IP(address).iptype() != "PRIVATE" and friendlyfire.check(address) == False:
        objects.api_interface.report(ip_address = address, categories = category, comment = comments)
    else:
        return None
    pass
pass
