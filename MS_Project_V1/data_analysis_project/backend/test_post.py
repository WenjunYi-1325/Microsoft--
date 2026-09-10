import requests

url = "http://127.0.0.1:5000/test2?param=Tom&age=18"

data = {
    "body": "Jack"
}

response = requests.post(
    url,
    json=data
)

print(response.text)