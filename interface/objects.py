"""
Objects module, in interface module.
Contains imports, all variables and objects that are referenced across the interface module.
"""

import smtplib, configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from platform import system
from IPy import IP
import basics
from abuseipdb import AbuseIpDbV2

log_platform = None # name of host platform, overwritten by __init__

notification_allow = None # boolean as a signal to not send email notifications, overwritten by __init__

notification_mailing_list = [] # list of recipient address(es) for notifications to be dispatched to, appended to by __init__

notification_smtp_service = None # SMTP object, overwritten by __init__

notification_host_email = None # address notifications are sent from, overwritten by __init__
notification_host_email_no_domain = None # address notifications are sent from, overwritten by __init__
notification_host_password = None # password for address which notifications are sent from, overwritten by __init__

safe_list = [] # list of IP address(es) that are whitelisted from any reports, such as admin hosts, overwritten by __init__

api_allow = None # boolean as signal to not interface with AbuseIPDB, overwritten by __init__
api_key = None # API key for AbuseIPDB, overwritten by __init__
api_interface = None # AbuseIPDB API object, overwritten by __init__
