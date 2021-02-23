from services import app
from flask import request, jsonify, render_template, session
from services.boardContent import service as baordContentService
import datetime
# from util.decorator import authDecorator
from util.decorator2 import jai_authDecorator
from util.decorator3 import authDecorator
from ainUtil import *
# from util.decorator3 import authDecorator, kys_authDecorator

# 게시글 data 가져오기
@app.route('/getBoardContent/<boardId>/<boardListId>/<nowPageNum>')
@authDecorator
@jai_authDecorator
def getBoardContent(boardId, boardListId, nowPageNum):
    print("getBoardContent 도착!!")
    result = {}
    # data = request.get_json()
    data = {}
    data['boardId'] = boardId
    data['boardListId'] = boardListId

    print(data)
    result['resultDB'] = baordContentService.getBoardContent(data)
    result['nowPageNum'] = nowPageNum

    # comment 가져오기
    result['commentList'] = baordContentService.getComment(data)
    
    # 시간표기 변경 - content
    if result['resultDB'][0]['board_regdate']:
        time = timeFormat(result['resultDB'][0]['board_regdate'])
        result['resultDB'][0]['board_regdate'] = time
    

    # 시간표기 변경 - comment
    temp = commentTimeFormat(result['commentList']['data'])
    result['commentList']['data'] = temp
            

    print(result['resultDB'])
    print(result['nowPageNum'])

    return render_template('ainBoardContent.html', data=result)
    # return render_template('dd.html', data=result)

@app.route('/ainBoardContent')
def test():
    return render_template('ainBoardContent.html')

# 댓글 입력

@app.route('/insertComment', methods=['POST'])
@jai_authDecorator
def insertComment():
    print("insertComment 도착!")
    result={}
    data = request.get_json()
    
    loginUser = session.get("loginUserData")
    print(loginUser)
    data['userId'] = loginUser['user_id']

    if data['commentPid']==None:
        data['commentPid']= 0
    
    print(data)
    result['resultDB'] = baordContentService.insertComment(data)
    
    # comment 가져오기
    result['commentList'] = baordContentService.getComment(data)
    # 시간표기 변경 - comment
    temp = commentTimeFormat(result['commentList']['data'])
    result['commentList']['data'] = temp

    from mq.sender import sendqueue
    sendqueue(data)


    print('@@@@@@@@@@@@')
    print(result)

    return result

# 댓글 삭제
@app.route('/delComment', methods=['POST'])
@jai_authDecorator
def delComment():
    print("delComment 도착")
    result = {}
    data = request.get_json()

    loginUser = session.get("loginUserData")
    print(loginUser)
    # 댓글 작성자 id와 로그인 유저 비교
    result['resultDB'] = baordContentService.delComment(data)

     # comment 가져오기
    result['commentList'] = baordContentService.getComment(data)
    # 시간표기 변경 - comment
    temp = commentTimeFormat(result['commentList']['data'])
    result['commentList']['data'] = temp


    print('@@@@@@@@@@@@')
    print(result)

    return result

# 권한없는 경우의 html로 이동
@app.route('/render/warningAuthority')
def warningAuthority():
    return render_template('warningAuthority.html')




# @app.route('/getBoardContent', methods=['POST'])
# def getBoardContent():
#     print("getBoardContent 도착!!")
#     result = {}
#     data = {}
#     data = request.get_json()
#     # data['boardId'] = boardId
#     # data['boardListId'] = boardListId

#     print(data)
#     result['resultDB'] = baordContentService.getBoardContent(data)
#     result['nowPageNum'] = data['nowPageNum']
#     print(result['resultDB'])
#     print(result['nowPageNum'])

#     # return jsonify(result)
#     return result


# @app.route('/render/boardContent/<data>/<nowPageNum>')
# def renderBoardContent(data, nowPageNum):
#     print("render boardContent 도착!!")
#     print(data)
#     print(nowPageNum)
#     # print(data['resultDB'])
#     # print(data['info'])
#     return render_template('ainBoardContent copy.html')