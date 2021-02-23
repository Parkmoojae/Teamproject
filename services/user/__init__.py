from services import app
from flask import request, jsonify, render_template, session, redirect
from services.user import service as userService
from mq.receiver import receivequeue



@app.route("/register", methods=['POST'])
def signUp():
    print('sendUserData 도착')
    result = {}
    data = request.form
    print("sendUserData: ", data)
    # checkIdVal = signUpService.checkId(data['userId'])
    result["resultDB"] = userService.userInsert(data)
    print("@@@@@@@@@")
    print(result)
    print("@@@@@@@@@")
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def userLogin():
    print("login 도착")
    result = {}
    data = request.form
    print(data['userId'])
    print(data['userPw'])
    resultService = userService.userLogin(data)
    print(resultService)
    print(type(resultService))
    
    if(len(resultService) == 0):
        # 아이디 없음
        result['resultDB'] = '0'
       
        #로그인 성공
    elif(resultService[0]['user_pw'] == data['userPw']):
        # 로그인 후 세션에 저장
        session["loginUserData"] = resultService[0]
        receivequeue(data)

    else:
        # 비밀번호 불일치
        result['resultDB'] = '-1'

    # return render_template("moojaeData.html")
    # return render_template("ainData.html")
    return redirect('/board')

@app.route("/sessionCheck")
def sessionCheck():
    print(session.get("loginUserData"))
    return session.get("loginUserData")

@app.route("/logout")
def logout():
    print("logout 도착!")
    print(session.get("loginUserData"))
    session.pop("loginUserData", None)
    print(session.get("loginUserData"))
    # return render_template("/")
    return redirect('/')
