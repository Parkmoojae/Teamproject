from services import app
from flask import request, jsonify, render_template, session, redirect
from services.board import service as boardService
from util.decorator3 import kys_authDecorator
# from util.decorator import kys_authDecorator

@app.route('/test/api')
def test_api():
    return render_template('/test/test_api.html')
    # return render_template('.../test/test_api.html')

@app.route('/test/kys')
def test_kys():
    return render_template('test_kys.html')

@app.route('/test/list', methods=['POST'])
def test_list():
    data={}
    return boardService.test_list(data)

@app.route('/test/auth', methods=['POST'])
@kys_authDecorator
def test_auth():
    data={}
    return boardService.test_list(data)

@app.route('/render/invalidRequest')
def render_invalidRequest():
    return render_template('invalidRequest.html')

@app.route('/render/insufficientAuthority')
def render_insufficientAuthorityRequest():
    return render_template('insufficientAuthority.html')

@app.route('/render/tempPage')
def render_tempPage():
    return render_template('tempPage.html')

@app.route('/render/board/write')
@kys_authDecorator
def render_boardWrite():
    requiredArgList = ['board_list_id']
    requestArgList = request.args.to_dict()
    # requiredArgList에 있는 인자가 들어오지 않으면 화면이동 X
    for requiredArg in requiredArgList:
        if requiredArg not in requestArgList.keys():
            return redirect('/render/invalidRequest')
    print(requestArgList)
    return render_template('boardWrite.html', data=requestArgList)

@app.route('/render/board/update')
@kys_authDecorator
def render_boardUpdate():
    requiredArgList = ['board_list_id', 'board_id']
    requestArgList = request.args.to_dict()
    # requiredArgList에 있는 인자가 들어오지 않으면 화면이동 X
    for requiredArg in requiredArgList:
        if requiredArg not in requestArgList.keys():
            return redirect('/render/invalidRequest')
    # print(requestArgList)
    
    boardContent = boardService.board_getContent({"board_id":requestArgList['board_id']})['data'][0]
    # print('boardContent : ', boardContent)
    # print(requestArgList)
    # print(boardContent['board_title'])
    requestArgList['board_title']     = boardContent['board_title']
    requestArgList['board_content']   = boardContent['board_content']
    
    return render_template('boardUpdate.html', data=requestArgList)

@app.route('/board/write', methods=['POST'])
def board_write():
    requestData = request.get_json()
    print('requestData : ', requestData)
    requestData['user_id'] = session.get("loginUserData")['user_id']
    result = boardService.board_write(requestData)
    return result

@app.route('/board/update', methods=["POST"])
def board_update():
    requestData = request.get_json()
    print('requestData : ', requestData)
    result = boardService.board_update(requestData)
    result['board_id']      = requestData.get('board_id', None)
    result['board_list_id']   = requestData.get('board_list_id', None)
    result['nowPageNum']   = requestData.get('nowPageNum', None)
    return result

@app.route('/board/delete', methods=["POST"])
def board_delete():
    requestData = request.get_json()
    print('requestData : ', requestData)
    result = boardService.board_delete(requestData)
    result['nowPageNum']    = requestData.get('nowPageNum', None)
    result['boardListId']   = requestData.get('boardListId', None)
    return result