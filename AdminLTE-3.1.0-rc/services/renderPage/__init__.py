from services import app
from flask import request, jsonify, render_template, session

@app.route('/')
def indexPage():
    return render_template('index2.html')

@app.route('/pages/tables/data.html')
def startPage():
    return render_template('pages/tables/data.html')