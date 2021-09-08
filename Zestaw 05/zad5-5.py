# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:04:18 2021

@author: Modecom
"""

import smtplib #, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "https://poczta.interia.pl"
port = 587
file_name = "zestaw_5_zadania.txt"
password = ""
password = input("Podaj haslo: ")
user = "damian.sub@interia.pl"


nadawca = user
odbiorca = input("Podaj odbiorcę(ów): ")
temat = input("Podaj temat e-maila: ")


wiad = MIMEMultipart()
wiad["To"] = odbiorca
wiad["From"] = nadawca
wiad["Subject"] = temat

wiad_wst = ""
linia = "" 
linia = input("Wpisz wiadomosc. Wolna linia konczy tresc.\n")
while linia != "":
    wiad_wst += linia + "\n"
    linia = input("")

czesc = MIMEText('text', "plain")
czesc.set_payload(wiad_wst)
wiad.attach(czesc)

#context = ssl.create_default_context()

session = smtplib.SMTP("217.74.64.236", 587)
    #session.set_debuglevel(1)
session.ehlo()
    #session.starttls(context=context)
    #session.ehlo()
session.login(user, password)
text = wiad.as_string()
session.sendmail(nadawca, odbiorca, text)
print("Wysłałe wiadomosć do "+str(nadawca))
session.quit()



