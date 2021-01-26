from services import app
from flask import request, jsonify, render_template, session

@app.route('/')
def startPage():
    return render_template('starter.html')