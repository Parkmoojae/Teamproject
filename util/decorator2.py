from functools import wraps
from flask import session as flaskSession
from flask import request, redirect
from services.boardContent.service import *
from services.auth.service import *

def jai_authDecorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("decorator!!!!")
        print(flaskSession.get('loginUserData'))
        result = {}
        requestPath = request.path
        pathList = requestPath.split('/')
        print(pathList)
        data ={}
        data = request.get_json()
        serviceResult = {}
        print(data)

        # 로그인 아이디와 게시글 작성자 비교
        loginData = {}
        loginData['user_id'] = flaskSession.get('loginUserData')['user_id']
        loginData['user_group_id'] = flaskSession.get('loginUserData')['user_group_id']
        serviceResult = authority_groupAuthority_getList(loginData)

        # 댓글 입력 권한 비교
        if(pathList[1]=='insertComment'):
            if(serviceResult[data['boardListId']]['auth_comment_write']!=1):
                result['code'] = 22
                return result

        # 댓글 삭제 권한 비교
        if(pathList[1]=='delComment'):                
            if(serviceResult[data['boardListId']]['auth_comment_del']==0):
                if(data['userId']!=loginData['user_id']):
                    result['code'] = 22
                    return result
        
        # 조회 권한 비교
        if(pathList[1]=='getBoardContent'):
            print("boardListId: ", pathList[3])
            print(flaskSession.get('loginUserData'))
            if(serviceResult[pathList[3]]['auth_board_read']==0):
                return redirect('/render/warningAuthority')
                
            
        return f(*args, **kwargs)

    return decorated_function