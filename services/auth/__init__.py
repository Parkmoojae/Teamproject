from services import app
from flask import request, jsonify, render_template, session, redirect
from services.auth import service as authService