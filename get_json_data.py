import json
import requests
# urllib의 urlretrieve 메소드로 이미지 다운
import urllib.request

url = requests.get("http://api.tvmaze.com/singlesearch/shows?q=Homeland&embed=episodes")
dic = json.loads(url.text)

logo = dic["image"]["medium"]
urllib.request.urlretrieve(logo, "logo.png")