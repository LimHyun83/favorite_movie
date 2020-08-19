import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.cine21.com/db/writer/info/?pre_code=E20041947', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
reviews = soup.select('#write_view_review20_holder > table > tbody > tr')

# reviews (tr들) 의 반복문을 돌리기
for review in reviews:
    # review안에 a가 있으며느,
    a_tag = review.select_one('td:nth-child(3) > p.mov_tit > a')
    if a_tag is not None:
        movie_title = a_tag.text
        print(movie_title)

