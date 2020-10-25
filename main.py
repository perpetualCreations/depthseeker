"""
Depthseeker

Report service for Apache that reads access logs, and highlights malicious activity.
Intended to be ran alongside Apache modules evasive and security.
It handles mainly interfacing with various other services and endpoints.
These include daily reports that can be dispatched to a mailing list and API interfacing with AbuseIPDB.

Depthseeker can deny hosts and disallow crawlers, however these are best handled by ModSecurity.

The service can be configured. Read documentation on proper usage and available options.

Made by perpetualCreations

Main module.
Handles parsing the log file, and exporting results through interface modules.
"""

import interface, process, basics

log = interface.log.collect().split("\n")
end = len(log)
index = 0

for x in range(0, len(log)):
    if log[index].find(["/vendor", "/wp-content"]) != -1:

