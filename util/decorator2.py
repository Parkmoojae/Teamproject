from functools import wraps
from flask import session as flaskSession
from flask import request
from services.boardContent.service import *

def jai_authDecorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("decorator!!!!")
        requestPath = request.path
        print(requestPath)
        data = {}
        data = request.get_json()
        print(data)
        if(flaskSession.get('loginUserData')):
            data['userId'] = flaskSession.get('loginUserData')['user_id']
        
        # 댓글 입력 권한 비교
        # if(requestPath=='/insertComment'):

        # 댓글 삭제 권한 비교
        # if(requestPath=='/delComment'):
            

        return f(*args, **kwargs)

    return decorated_function