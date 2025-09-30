import requests

url = "http://127.0.0.1:5000/extract"
payload = { "url": "https://www.tiktok.com/@fragsonly/video/7544194412297850126" }

response = requests.post(url, json=payload)
print(response.json())