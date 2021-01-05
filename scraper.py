# selenium imports
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
# email imports
import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os

user = os.getenv("jobScraper_user")
reciever = os.getenv("jobScraper_reciever")
app_password = os.getenv("jobScraper_app_password")

PATH = "/Users/philiplee/Desktop/Personal Projects/chromedriver"

driver = webdriver.Chrome(PATH)
# url is only for posts that happened within last week
url = "https://www.linkedin.com/jobs/search/??f_TPR=r604800&keywords=software%20engineer%20%20intern&location=United%20States&f_TP=1%2C2"
driver.get(url)

# empty lists to store data
title = []
company = []
location = []
post_time = []
apply_link = []

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-card__full-card-link"))
    )
    elements = driver.find_elements_by_class_name("result-card__full-card-link")
    href_links = []

    # get per posting link
    for elem in elements:
        href_links.append(elem.get_attribute("href"))
    # for each posting, grab the job details
    for link in href_links:
        try:
            driver.get(link)
            job_title = driver.find_element_by_class_name("topcard__title")
            job_company = driver.find_element_by_class_name("topcard__org-name-link")
            job_location = driver.find_element_by_class_name("topcard__flavor--bullet")
            posting_time = driver.find_element_by_class_name("posted-time-ago__text")
            job_link = driver.find_element_by_class_name("apply-button").get_attribute("href")
            title.append(job_title.text)
            company.append(job_company.text)
            location.append(job_location.text)
            post_time.append(posting_time.text)
            apply_link.append(job_link)

        except:
            print("Error'd out at one point")

finally:
    driver.quit()

# convert lists in dictionary, then convert into pd df
dictionary_ = {
    "title":title,
    "company":company,
    "location":location,
    "post_time":post_time,
    "apply_link":apply_link}

df = pd.DataFrame(dictionary_)
print(df)

# MIME email
sender = user
recievers = reciever
body_of_email = "This is a test email"
msg = MIMEMultipart()
msg["subject"] = "This is the test subject"
msg["From"] = sender
msg["To"] = recievers

html = """\
    <html>
    <head></head>
    <body>
    {}
    </body>
    </html>
    """.format(df.to_html())

msg_1 = MIMEText(html,"html")
msg.attach(msg_1)

# connect to gmail SMTP server
s = smtplib.SMTP_SSL(host = "smtp.gmail.com",port = 465)
s.login(user=user,password=app_password)
s.sendmail(sender,recievers,msg.as_string())
s.quit()