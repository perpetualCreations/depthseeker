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
objects.web_root = config_parser_read["WEBROOT"]["root"]

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

# robots.txt check, otherwise crawler blocking may not work
try:
    with open(objects.web_root + "robots.txt") as robot_test:
        pass
    pass
except FileNotFoundError:
    with open(objects.web_root + "robots.txt", "w") as robot_create:
        robot_create.write("User-agent: *\nDisallow: ")
    pass
pass
