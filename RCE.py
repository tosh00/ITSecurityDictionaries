import requests

url = 'http://ubuntu:4400/ping'

d = {"host": "8.8.8.8"}


res = requests.post(url, data=d)
