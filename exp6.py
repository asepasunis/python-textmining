import requests
from bs4 import BeautifulSoup

link = "https://news.detik.com/berita"
response = requests.get(link)
textHtml = BeautifulSoup(response.text,'html.parser') 
print(textHtml.get_text())
