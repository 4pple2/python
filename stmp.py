
import smtplib
from email.mime.text import MIMEText
import random as rand
import schedule
import time
import datetime
def message():
    file = open(file='quotes.txt')
    f=(file.readlines())
    li = []
    for i in f:
        li.append(i)

    message = str(li[rand.randint(0, len(li))])
    return message


def send_mail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.ehlo()

    smtp.starttls()
    #
    from_id = 'kjs11945@gmail.com'
    to_id = 'kjs1194562@gmail.com'

    app_pw = 'pbgy ropj dweu uwos'
    smtp.login(from_id,app_pw)
    #내용
    content = message()
    msg = MIMEText(content)
    msg['Subject'] = '[파이썬 테스트] 월요 명언'

    smtp.sendmail('kjs11945@gmail.com', 'kjs119456@gmail.com', msg.as_string())

    smtp.quit()

schedule.every().monday.at('08:00').do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)

"""

##파일 역리
import datetime as dt
dt = dt.datetime(2023,10,30,8)
for i in range(0,393,7):
    dt + i
    if

while(i <393):
    dt+ 7
    if dt == dt.datetime.now():
"""
