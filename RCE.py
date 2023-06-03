import requests

url = 'http://ubuntu:4400/ping'


res = requests.post(url, "host;id")
