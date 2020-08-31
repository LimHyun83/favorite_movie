from flask import Flask, render_template, jsonify, request
import requests

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.reviewer  # 'reviewer'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')

# mongoDB에서 모든 reviewer 데이터 조회하기
@app.route('/reviewer', methods=['GET'])
def read_reviewer():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    reviewer_find = db.reviewer.find({}, {'_id': 0})

    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify({'result': 'success',
                    'articles': list(articles_find)})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)