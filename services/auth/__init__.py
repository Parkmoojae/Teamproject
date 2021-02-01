from services import app
from flask import request, jsonify, render_template, session, redirect
from services.auth import service as authService
from flask import session as flaskSession

@app.route('/test/authList', methods=['POST'])
def test_authList():
    data = {}
    data['user_id'] = flaskSession.get('loginUserData')['user_id']
    return authService.authority_groupAuthority_getList(data)
