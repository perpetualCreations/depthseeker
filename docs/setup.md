# Setup
Installation instructions for Depthseeker.

## Extraction
Download files from release, and extract. Upload the entire Depthseeker directory to your web server.

## Configuration
There are 4 separate configuration files that need to be edited, and are all under the interface module. 

notify.cfg contains the address and password of the email account which notifications are dispatched from.

platform.cfg contains the Linux distro running, which determines the directory access logs are stored under.

mail-to.list is the list of recipients to receive daily reports. This can be left empty to disable.

api.cfg contains the API key for AbuseIPDB. This can be left empty to disable. 

## Dependencies
Please install all dependencies specified under the requirements.txt file, through PIP.

## Crontab
Create a cronjob, schedule it to run the main module at 11:59 PM UTC+0, as Apache will clear the access log at 12:00 AM UTC+0. 

Example:
```
59 23 * * 0-6 python /home/admin/depthseeker/main.py >/dev/null 2>&1
```

You may choose to select a custom time to run the main module, however please keep in mind that the access log for that day may not be compelete.

## End of Setup
If you have any questions please send them to the developer.
Any issues, bugs, and suggestions should be submitted to the Github repository issues tab.

Please see modules.md for information on each module in Depthseeker.

Main website:
[dreamerslegacy.xyz](https://dreamerslegacy.xyz)
