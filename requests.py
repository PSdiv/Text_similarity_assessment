import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'text1':"text one for comparision", 'text2':"text two for comparision"})

print(r.json())