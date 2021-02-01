from functools import wraps
from flask import session as flaskSession
from flask import request
from services.boardContent.service import *

def jai_authDecorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("decorator!!!!")
        data = {}
        data = request.get_json()
        print(data)
        if(flaskSession.get('loginUserData')):
            data['userId'] = flaskSession.get('loginUserData')['user_id']
        return f(*args, **kwargs)

    return decorated_function