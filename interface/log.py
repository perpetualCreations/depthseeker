"""
Log module, in interface module.
Handles reading access logs and writing its own incident logs.
"""

from interface import objects

def collect():
    """
    Collects access log entries for the day.
    :return: multiline string
    """
    with open(objects.log_platform) as log_read:
        return log_read.read()
    pass
pass

def log(message):
    """
    Generate report for the day.
    :param message: Report message.
    :return: none.
    """
    with open(objects.basics.basics.make_timestamp() + ".txt", "w") as log_write:
        log_write.write("Daily Report from Depthseeker Access Log Analysis Service. \nGenerated for date: " + objects.basics.basics.make_timestamp() + " UTC+0 \n\n" + message + "\n\nEnd of report. \nThank you for using Depthseeker. \nDepthseeker Project, by perpetualCreations, MIT license since 2020. \nSee https://dreamerslegacy.xyz for documentation and more.")
    pass
pass
