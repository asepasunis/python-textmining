import requests

link = "https://news.detik.com/berita"
f = requests.get(link)
print(f.text)
