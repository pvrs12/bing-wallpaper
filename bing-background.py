import requests
import shutil

base="http://www.bing.com"
resource="/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

resp = requests.get(base+resource)
respJson = resp.json()

imageUrl = respJson["images"][0]["url"]

#print("downloading from {0}".format(base+imageUrl))
imageResp = requests.get(base+imageUrl, stream=True)
with open('image.jpg','wb') as f:
  for chunk in imageResp:
    f.write(chunk)

