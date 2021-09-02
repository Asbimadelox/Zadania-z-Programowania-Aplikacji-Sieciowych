# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:06:26 2021

@author: Modecom
"""

import requests
import shutil

url = "https://httpbin.org/image/png"

ima = requests.get(url, stream=True)

print(" ")

with open("zdjecie.png", "wb") as file:
    shutil.copyfileobj(ima.raw, file)
    
print("Gotowe!")  
file.close()
