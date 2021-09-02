# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:22:48 2021

@author: Modecom
"""


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = "https://poczta.interia.pl/"
port = 587
#damian.sub@interia.pl

nadawca = input("Podaj nadawcę: ")
odbiorca = input("Podaj odbiorcę(ów): ")
temat = input("Podaj temat e-maila: ")
password = ""


wiad = MIMEMultipart()
wiad['To'] = odbiorca
wiad['From'] = nadawca
wiad['Subject'] = temat

wiad_wst = ""
linia = "" 
linia = input("Wpisz wiadomosc. Wolna linia konczy tresc.\n")
while linia != "":
    wiad_wst += linia + "\n"
    linia = input("")

czesc = MIMEText('text', "plain")
czesc.set_payload(wiad_wst)
wiad.attach(czesc)


session = smtplib.SMTP('217.74.64.236', 587)

user = input('Podaj login: ')
password = input('Podaj haslo: ')


session.starttls()

session.login(user, password)
text = wiad.as_string()
session.sendmail(nadawca, odbiorca, text)

print("Wysłałe wiadomosć do "+str(nadawca))

session.quit()