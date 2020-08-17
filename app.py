import requests
from bs4 import BeautifulSoup

url = '여기에 스크래핑할 영화 주소가 들어간다.'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbreview