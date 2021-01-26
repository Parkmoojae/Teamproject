from services import app
from flask import request, jsonify, render_template, session

@app.route('/login', methods=['POST'])
def userLogin():
    print("login")
    return render_template('data.html')