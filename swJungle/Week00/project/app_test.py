from bson.objectid import ObjectId
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def read_memos():
    # 1. 모든 memo 찾기
    results = list(db.memos.find({}))
    allMemos = []
    for result in results:
      information = {'_id':str(result['_id']), 'title':result['title'], 'comment' : result['comment']}
      allMemos.append(information)
    # 2. memos라는 키 값으로 정보 내려주기
    return jsonify({'result':'success','memos':allMemos,'msg':'조회 완료!'})

## API 역할을 하는 부분
@app.route('/memo/post', methods=['POST'])
def post_memo():
		# 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']
    # 2. mongoDB 에 입력
    memo = {'title': title_receive, 'comment': comment_receive}
		
    db.memos.insert_one(memo)

    return jsonify({'result': 'success', 'msg':'저장완료!'})

@app.route('/memo/delete', methods=['POST'])
def delete_memo():
		# 1. 클라이언트로부터 데이터를 받기
    id_delete = ObjectId(request.form['id_give'])
    
    # id와 일치하는 메모 삭제
    db.memos.delete_one({'_id':id_delete})

    return jsonify({'result': 'success', 'msg':'삭제완료!'})

@app.route('/memo/update', methods=['POST'])
def update_memo():
		# 1. 클라이언트로부터 데이터를 받기
    title_update = request.form['titleUpdate_give']
    comment_update = request.form['commentUpdate_give']
    id_update = ObjectId(request.form['id_give'])
  
		# 2. mongoDB에서 id와 일치하는 메모의 제목 및 내용 업데이트
    db.memos.update_one({'_id': id_update},{'$set':{'title':title_update}})
    db.memos.update_one({'_id': id_update},{'$set':{'comment':comment_update}})
    
    return jsonify({'result': 'success', 'msg':'수정완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)