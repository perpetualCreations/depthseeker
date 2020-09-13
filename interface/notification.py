"""
Notification module, in interface module.
Handles dispatching notifications to administrators through notify() function.

This module has its own configuration file and additional mailing list configuration file, named notify.cfg and mail-to.list respectively.
"""

from interface import objects

def notify(message: str):
    """
    Issues an email notification to address(es) in mailing list.
    :param message: Notification message.
    :return: none.
    """
    msg = objects.MIMEMultipart()
    msg['From'] = ", ".join(objects.notification_mailing_list)
    msg['To'] = objects.notification_mailing_list
    msg['Subject'] = "Daily Report, Depthseeker Access Log Analysis Service"
    msg.attach(MIMEText("Daily Report from Depthseeker Access Log Analysis Service. \nGenerated for date: " + objects.basics.basics.make_timestamp() + " UTC+0 \n\n" + message + "\n\nEnd of report. \nThank you for using Depthseeker. \nDepthseeker Project, by perpetualCreations, MIT license since 2020. \nSee https://dreamerslegacy.xyz for documentation and more.", 'plain'))
    objects.notification_smtp_service.sendmail(objects.notification_host_email, objects.notification_mailing_list, msg.as_string())
pass
