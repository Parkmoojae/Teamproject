from functools import wraps
from flask import session as flaskSession
from flask import request
from services.boardContent.service import *
from services.auth.service import *

def jai_authDecorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("decorator!!!!")
        result = {}
        requestPath = request.path
        print(requestPath)
        data = {}
        data = request.get_json()
        serviceResult = {}
        print(data)

        # 로그인 아이디와 게시글 작성자 비교
        data['user_id'] = flaskSession.get('loginUserData')['user_id']
        serviceResult = authority_groupAuthority_getList(data)

        # 댓글 입력 권한 비교
        if(requestPath=='/insertComment'):
            if(serviceResult[data['boardListId']]['auth_comment_write']!=1):
                result['code'] = 22
                return result

        # 댓글 삭제 권한 비교
        if(requestPath=='/delComment'):                
            if(serviceResult[data['boardListId']]['auth_comment_del']==0):
                if(data['userId']!=data['user_id']):
                    result['code'] = 22
                    return result
                
            
        return f(*args, **kwargs)

    return decorated_function