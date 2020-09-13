"""
Block module, in interface module.
Blacklists abusive IP addresses, and disallows crawlers.

Crawler blocking through robots.txt is useless against malicious crawlers, and an IP blacklist is better.
This limits crawler blocking to ones that aren't malicious, but are undesired and eat up bandwidth.
"""

from interface import objects

def ip(address):
    """
    Blocks an IP address.
    :param address: host to be blocked.
    :return: none.
    """
    with open("/etc/hosts.deny") as blacklist_read:
        blacklist_contents = blacklist_read.read().splitlines()
        blacklist_line = len(blacklist_contents)
        while blacklist_line >= 0:
            if "http : " in blacklist_contents[blacklist_line]:
                if address not in blacklist_contents[blacklist_line]:
                    while open("/etc/hosts.deny") as blacklist_write:
                else:
                    return
                pass
            elif

            else:

                blacklist_line -= 1
            pass
        pass
    pass
pass

def crawler(name):
    """
    Reads defined user-agents to prevent duplicate statements, and blocks targeted crawler through robots.txt.
    This function will not overwrite a rule already in place.
    Please note that malicious web crawlers will not follow robots.txt rules.
    :param name: User-agent name.
    :return: None
    """
    with open(objects.web_root + "robots.txt") as robots_read:
        robots_contents = robots_read.read().splitlines()
        if ("User-agent: " + name) in robots_contents:
            return None
        else:
            with open(objects.web_root + "robots.txt", "r+") as robots_write:
                robots_write.write("\n\nUser-agent: " + name + "\nDisallow: /")
            pass
        pass
    pass
pass
