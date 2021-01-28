from services import app
from flask import request, jsonify, render_template, session
from services.board import service as boardService

@app.route('/test/api')
def test_api():
    return render_template('test_api.html')

@app.route('/test/list', methods=['POST'])
def test_list():
    data={}
    return boardService.test_list(data)

@app.route('/board/write', methods=['POST'])
def board_write():
    requestData = request.get_json()
    print('requestData : ', requestData)
    return boardService.board_write(requestData)

@app.route('/board/update', methods=["POST"])
def board_update():
    requestData = request.get_json()
    print('requestData : ', requestData)
    return boardService.board_update(requestData)

@app.route('/board/delete', methods=["POST"])
def board_delete():
    requestData = request.get_json()
    print('requestData : ', requestData)
    return boardService.board_delete(requestData)