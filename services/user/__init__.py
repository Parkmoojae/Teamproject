from services import app
from flask import request, jsonify, render_template, session
from services.user import service as userService


@app.route('/login', methods=['POST'])
def userLogin():
    print("login 도착")
    result = {}
    data = request.form
    print(data['userId'])
    print(data['userPw'])
    resultService = userService.userLogin(data)
    # print(result)
    # print(type(result))

    # if(len(resultService) == 0):
    #     # 아이디 없음
    #     result['resultDB'] = '0'
    # elif(resultService[0]['USER_PW'] == data['userPw']):
    #     # 로그인 성공
    #     loginUpdate = userService.userLastlogin(resultService[0]['USER_NO'])
        
    #     # 게시판 별 권한 가져오기
    #     userAuth = userService.getAuth(resultService[0]['USER_NO'])

    #     if(loginUpdate=='200'):
    #         result['resultDB'] = '1'
        
    #     # 로그인 후 세션에 저장
    #     session["loginUserData"] = resultService[0]
    #     session['userAuth'] = userAuth
    # else:
    #     # 비밀번호 불일치
    #     result['resultDB'] = '-1'


    # return render_template('data.html')
    return render_template('ainData.html')