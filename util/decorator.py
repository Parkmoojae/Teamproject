from functools import wraps
from flask import session as flaskSession
from flask import request, redirect
from services.board import service as boardService
import traceback

def authDecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if(flaskSession.get('loginUserData') is None):
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

