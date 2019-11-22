import requests
res = requests.get('http://127.0.0.1:5000/Naruto/Random')
if res.ok:
    print (res.content)