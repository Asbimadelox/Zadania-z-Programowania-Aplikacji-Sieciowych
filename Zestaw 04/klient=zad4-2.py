# -*- coding: utf-8 -*-

import requests

url = "https://httpbin.org/html"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64 rv:91.0.2) Gecko/20100101 Firefox/91.0.2'}

odp = requests.get(url, headers=headers)
print(type(odp))

print(" ")
print(odp.text)

with open("strona.html", "w") as file:
    file.write(odp.text)
file.close()
odp.close()


    
