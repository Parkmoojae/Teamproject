from services import app
from flask import request, jsonify, render_template, session
from services.boardContent import service as baordContentService


@app.route('/getBoardContent/<boardId>/<boardListId>/<nowPageNum>')
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
    print(result['resultDB'])
    print(result['nowPageNum'])

    return render_template('ainBoardContent copy.html', data=result)


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