"""
Initiation for interface module.
"""

from interface import log, notification, objects

# configuration parsing
config_parser_read = objects.configparser.ConfigParser()
config_parser_read.read("notify.cfg")
objects.notification_host_email = config_parser_read["EMAIL"]["host_email"]
objects.notification_host_email_no_domain = objects.notification_host_email.rstrip("@gmail.com")
objects.notification_host_password = config_parser_read["EMAIL"]["host_password"]

config_parser_read.read("platform.cfg")
platform_raw = config_parser_read["PLATFORM"]["distro"]
if platform_raw in ["RHEL", "Red Hat", "CentOS", "Fedora Linux"]:
    objects.log_platform = "/var/log/httpd/access_log"
elif platform_raw in ["Debian", "Ubuntu"]:
    objects.log_platform = "/var/log/apache2/access.log"
elif platform_raw in ["FreeBSD"]:
    objects.log_platform = "/var/log/httpd-access.log"
else:
    objects.log_platform = "/var/log/apache2/access.log"
pass

config_parser_read.read("api.cfg")
objects.api_key = config_parser_read["API"]["key"]

if objects.api_key == "":
    objects.api_allow = False
else:
    objects.api_allow = True
    # AbuseIPDB API initiation
    objects.api_interface = objects.AbuseIpDbV2(api_key=objects.api_key)
pass

# SMTP mailing initialization
objects.notification_smtp_service = objects.smtplib.SMTP('smtp.gmail.com', 587)
objects.notification_smtp_service.ehlo()
objects.notification_smtp_service.starttls()
objects.notification_smtp_service.login(objects.notification_host_email_no_domain, objects.notification_host_password)

with open("mail-to.list") as mailing_list_read:
    while mailing_list_loop != "### DO NOT DELETE LINE TERMINATOR ###":
        mailing_list_line = 8
        mailing_list_loop = mailing_list_read.readline(mailing_list_line)
        objects.notification_mailing_list.append(mailing_list_loop)
        mailing_list_line += 1
    pass
pass

if not objects.notification_mailing_list:
    objects.notification_allow = False
else:
    objects.notification_allow = True
pass
