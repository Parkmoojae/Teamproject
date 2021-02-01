from services import app
from flask import request, jsonify, render_template, session
from services.dataBoard import service as BService

@app.route('/board', methods=["GET", "POST"])
def boardPage():
    data = request.args.get('board_list_id')
    nowPageNum = request.args.get('nowPageNum')
    print("!!!!!!!!!!!!!!!!!!!!")
    print(data)
    if data is None:
        data = 1
    boardList = BService.selectBoard(data)
    result = {}
    result['boardList']=boardList
    result['nowPageNum']=nowPageNum
    return render_template('data.html',result= result)  