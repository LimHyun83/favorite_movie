import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.favorite_movie  # 스크래핑한 데이터를 'favorite_movie'라는 이름의 db를 만들거나 사용합니다.

# 스크래핑 위한 브라우져 양식
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 평론가코드별로 딕셔너리를 만들어낸다.
# 평론가코드별로 리뷰가 몇페이지 까지 있는지(last_page) 찾아낸다.

#평론가별로 딕셔너리
reviewer_dict = {
    "김소미" : 'E20042186',
    "김용언" : 'E20041217',
    "김성훈" : 'E20041648',
    "김현수" : 'E20041946',
    "김혜리" : 'C20030816',
    "박평식" : 'E20041252',
    "송경원" : 'E20041673',
    "송형국" : 'E20041841',
    "이동진" : 'E20041283',
    "이용철" : 'E20041291',
    "이주현" : 'E20041646',
    "이화정" : 'E20041565',
    "임수연" : 'E20042151',
    "장영엽" : 'E20041590',
    "주성철": 'E20041598',
    "황진미" : 'E20041338',
    "남선우" : 'E20042329',
    "조현나" : 'E20042315',
    "김철홍" : 'E20042369',
    "배동미" : 'E20042345',
    "박정원" : 'E20042314',
    "허남웅" : 'E20042045',
    "오진우" : 'E20042370',
    "이나경" : 'E20042265',
    "홍은애" : 'E20042174',
    "우혜경" : 'E20041758',
    "이지현" : 'E20041639',
    "홍은미" : 'E20042249',
    "이다혜" : 'C20041001',
    "김소희" : 'E20041806',
    "김송희" : 'E20041952',
    "유지나" : 'E20041279',
    "송효정" : 'E20041579',
    "전효진" : 'E20042250',
    "한동원" : 'E20041330',
    "김보연" : 'E20041797',
    "곽민해" : 'E20042139',
    "정지혜" : 'E20041783',
    "김수빈" : 'E20042015',
    "김태훈" : 'E20041534',
    "이예지" : 'E20041950',
    "윤혜지" : 'E20041721',
    "김지미" : 'E20041390',
    "조재휘" : 'E20041959',
    "문동명" : 'E20041947',
    "박소미" : 'E20041917',
    "안현진" : 'E20041487',
    "안시환" : 'E20041391',
    "이현경" : 'E20041520',
    "정한석" : 'C20030819',
    "김소희2" : 'E20041214',
    "이후경" : 'E20041717',
    "정예찬" : 'E20041799',
    "김효선" : 'E20041716',
    "김종철" : 'E20041228',
    "이기준" : 'E20041779',
    "김봉석" : 'C20030805',
    "이영진" : 'C20030818',
    "강병진" : 'E20041463',
    "김도훈" : 'C20040204',
    "남민영" : 'E20041719',
    "신두영" : 'E20041678',
    "달시 파켓" : 'E20041243',
    "김태훈2" : 'E20041693',
    "문석" : 'C20040801',
    "오세형" : 'E20041694',
    "장미" : 'E20041488',
    "정재혁" : 'E20041465',
    "고경태" : 'E20041570',
    "박혜명" : 'C20030825',
    "남동철" : 'C20030813',
    "최하나" : 'E20041464',
    "오정연" : 'C20040203',
    "남다은" : 'E20041237',
    "김은형" : 'E20041220',
    "이성욱" : 'C20030808',
    "심영섭" : 'E20041269',
    "강한섭" : 'E20041369',
    "김영진" : 'E20041370',
    "이명인" : 'E20041368',
    "하재봉" : 'E20041445',
    "안정숙" : 'E20041273',
    "홍성남" : 'E20041334',
    "김소영" : 'E20041213',
    "임범" : 'E20041301'
}

#평론가 항목(이름)과 값(코드)로 반복하
for reviewer_name, reviewer_code in zip(reviewer_dict.keys(), reviewer_dict.values()):
    # print("==={} : {}===".format(reviewer_name, reviewer_code))

    # 아래 url 주소에서 평론가별 코드로 데이터 호출
    data = requests.post('http://www.cine21.com/db/writer/info_review20', data={'pre_code': reviewer_code},  headers=headers)
    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup)

    # 리뷰가 몇페이지 까지 있는지 체크
    pagination = soup.select_one('div.pagination > a.btn_end')

    # 마지막 페이지에 해당되는 숫자만 뽑아내서 숫자로 변환하고 last_page 로규정
    last_page = int(pagination.get('href').split('(')[-1][:-1])

    # last_page의 숫자+1로 조회할 페이지를 현재페이지(current_page) 라는 딕셔너리로 만들어낸다.
    # 그리고 평론가코드와 현재페이지를 기준으로 리뷰를 반복해서 조회한다.
    for current_page in range(1, last_page+1):
        data = requests.post('http://www.cine21.com/db/writer/info_review20',
                             data={'pre_code': reviewer_code, 'p': current_page}, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        # 리뷰가 등록된 영화제목이 있는 a 태그를 기준으로 reviews 를 딕셔너리로 만들어낸다.
        reviews = soup.select('td')

        image_td_list = reviews[0::3]
        score_td_list = reviews[1::3]
        movie_td_list = reviews[2::3]

        # reviews 안에서 review로 반복문을 돌리기
        for image_td, score_td, movie_td in zip(image_td_list, score_td_list, movie_td_list):

            # 이미지 가져오기
            image_url = image_td.select_one('img.thumb').get('src')

            # 스코어 가져오기
            score = int(score_td.select_one('span.num').text)

            # 영화 정보 및 코멘트 가져오기
            title = movie_td.select_one('p.mov_tit > a').text
            year = movie_td.select_one('span.year').text
            comment = movie_td.select_one('.comment').text

            # print(image_url, score, title, year, comment)

            # DB에 스크래핑한 리뷰 정보를 저장한다.
            doc = {
                'reviewer_name': reviewer_name,
                'reviewer_code': reviewer_code,
                'image_url': image_url,
                'title' : title,
                'year' : year,
                'score' : score,
                'comment' : comment
            }

            db.reviewer_score.insert_one(doc)




