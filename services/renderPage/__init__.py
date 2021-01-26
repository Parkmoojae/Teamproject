from services import app
from flask import request, jsonify, render_template, session

@app.route('/')
def indexPage():
    return render_template('login.html')

