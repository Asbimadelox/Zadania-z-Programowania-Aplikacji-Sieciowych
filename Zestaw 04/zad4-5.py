# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 20:28:32 2021

@author: Modecom
"""
import requests

url = "https://httpbin.org/forms/post"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":	"gzip, deflate, br",
    "Accept-Language":	"pl,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Length":	"155",
    "Content-Type":	"application/x-www-form-urlencoded",
    "Host":	"httpbin.org",
    "Origin":	"https://httpbin.org",
    "Referer":	"https://httpbin.org/forms/post",
    "Sec-Fetch-Dest":	"document",
    "Sec-Fetch-Mode":	"navigate",
    "Sec-Fetch-Site":	"same-origin",
    "Sec-Fetch-User":	"?1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests":	"1",
    "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

payload={
    "comments": "Fast!",
    "custemail":	"Damianex.wp@wp.pl",
    "custname":	"Damianex",
    "custtel":	"345345354",
    "delivery":	"15:00",
    "size":	"large",
    "topping": {
        "0": "bacon",
        "1": "onion",
        "2": "mushroom"
    }
}

params = {'guestbook_name' : 'main'}

odp = ""


req = requests.post(url, data=payload, headers=header, params=params, allow_redirects=True)
req.encoding
print(req.text)

#odp = s.receive(1024)
