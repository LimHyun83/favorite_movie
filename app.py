from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.favorite_movie
collection = db.reviewer_score

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

# 평론가 이름과 코드로 호출
for reviewer_name, reviewer_code in zip(reviewer_dict.keys(), reviewer_dict.values()):
    print("==={} : {}===".format(reviewer_name, reviewer_code))

# 평론가 코드별 collection에서 리뷰 찾아서 갯수 세
review_counts = collection.find({'reviewer_code' : reviewer_dict.values()})
for review_count in review_counts:
    print(review_count)


# # HTML을 주는 부분
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# # 평론가별로 평론가 리스트 호출
# @app.route('/api/list', methods=['GET'])
# def show_list():



# API 역할을 하는 부분
# @app.route('/api/review', methods=['GET'])
# def show_reviews():
#     # 1. favorite_movie db에서 reviewer_score 목록 전체를 검색합니다. ID는 제외하고 Score 높은 순 정렬
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     reviewes = list(db.reviewer_score.find({}, {'_id': False}).sort('score', -1))
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success', 'reviewes_list': reviewes})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)