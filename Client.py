import requests
res = requests.get('http://127.0.0.1:5000/NarutoQuotes?character=Naruto')
if res.ok:
    print (res.content)