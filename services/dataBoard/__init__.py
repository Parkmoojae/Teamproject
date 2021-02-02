from services import app
from flask import request, jsonify, render_template, session
from services.dataBoard import service as BService
from util import *

@app.route('/board', methods=["GET", "POST"])
def boardPage():
    data = request.args.get('board_list_id')
    print("!!!!!!!!!!!!!!!!!!!!")
    print(data)
    if data is None:
        data = 1
    boardList = BService.selectBoard(data)
    # boardList['board_regdate'] = to_user_timezone(boardList['board_regdate'])
    result = {}
    result['data']=boardList

    # result['boardList']=boardList
    convertDatetimeToString_list(result)
    result['boardList'] = result['data']
    return render_template('data.html',result= result)  

