#!/usr/bin/env python

import requests
import os

base="https://api.nasa.gov"
resource="/planetary/apod?api_key=00yAUYdird37sY60Q31K8NnkLsnq1iKcd6DapaK4"

resp = requests.get(base+resource)
respJson = resp.json()
#print(respJson)
imageUrl = respJson["url"]

#print("downloading from {0}".format(base+imageUrl))
imageResp = requests.get(imageUrl, stream=True)
with open('apod.jpg','wb') as f:
  for chunk in imageResp:
    f.write(chunk)

os.system("xfdesktop --reload")
