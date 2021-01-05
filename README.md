**<h3>Automation Scripts</h3>**
<br>
This will be a repo consisting of small scripts that I use on a daily / weekly basis. These will range from simple push notifications when the stock market opens, to automating job postings. As I get more ideas I'll update this README.

**Market Alert**
<br>
This is a simple push notification using the "Pushover" application on IOS.

The CRON job will run every week day at 6:30AM PST to notify me of the SPY's open price, and previous close price. The idea is to get a general notification
of how the markets are going that day.

This is not to be used as a trading signal of any kind, more so of a general tool to figure out to contribute on that day or not.

**Documentation for Market Alert** 
<br>
python-pushover docs - https://github.com/Thibauth/python-pushover <br>
Pushover API - https://pushover.net/api <br>
yfinance - https://github.com/ranaroussi/yfinance <br>

**Job Scraper Script** <br>
This is a simple script using selenium to scrape jobs off of posting websites to send myself in a weekly email.
<br>
CRON Job runs weekly on Monday @ 7AM PST

**Documentation for Job Scraper**
<br>
Selenium - https://selenium-python.readthedocs.io/
SMTP - https://docs.python.org/3/library/smtplib.html
Article for emails - https://realpython.com/python-send-email/
