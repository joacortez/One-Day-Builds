#this code will scrape any website
# things needed:

import requests
from bs4 import BeautifulSoup
import smtplib
import time

#set variables
URL = "https://www.google.com/search?q=my+user+agent&rlz=1C1CHBF_deEC909EC909&oq=my+user+agent&aqs=chrome..69i57j69i64.4277j0j7&sourceid=chrome&ie=UTF-8"
set_price = float(1.300)
update_time = 24

#headers: check user agent by searching my user agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}


def get_things():
    page = requests.get(URL, headers=headers)

    #page parser
    page = requests.get(URL, headers=headers)

    html = BeautifulSoup(page.content, "html.parser")
    soup = BeautifulSoup(html.prettify(), "html.parser")
    
    #get the things you want
    #if the price is what you want use float for numbers <1000 and int for the rest and call de [a:b]
    name = soup.find(id="search ID in the browser").get_text()

    converted_price = float(name[0,5])
    
    #check price
    if converted_price < set_price:
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("joaprogramms@gmail.com", "quesoconcarne")

    #set email settings
    subject = "Precio de name bajo"
    body = "chequea el link *inserta link aca*"

    #format the message
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "joaprogramms@gmail.com",
        "joacortez@outlook.com",
        msg
    )

    server.quit()

# run program periodically
while(True):
    get_things()
    time.sleep(update_time * 3600)

send_mail()
    