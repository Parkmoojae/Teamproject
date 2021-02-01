from services.board import service as boardService
from flask import session as flaskSession
from flask import request
from functools import wraps

def kys_authDecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        requestPath = request.path
        currentUserData = flaskSession.get('loginUserData')
        print('check requestPath(kys_authDecorator) :', requestPath)
        print('userData : ', flaskSession.get('loginUserData'))
        return func(*args, **kwargs)
    return wrapper