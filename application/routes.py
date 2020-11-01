from application import app
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from datetime import datetime, timedelta
import list
# from application.models import User, Course, Enrollment
# from application.forms import LoginForm, RegistratinForm
# from flask_restplus import Resource
# from application.courses_list import course_list




@app.route("/index")
@app.route("/")
def index():
    return 'hey'

@app.route("/videos_data/")
def videos_data():

    videos = sorted(list.result.objects, key=lambda k: k.createdAt, reverse=True)[:20]
    dt_object = datetime.fromtimestamp
    sec_converter = timedelta

    return render_template('demo_table.html', videos=videos, dt_object=dt_object, sec_converter=sec_converter)

@app.route("/delete_video", methods=["GET", "POST"])
def delete_video():
    entry_id = request.form.get('id')
    list.client.media.delete(entry_id)

@app.route("/error")
def error_page():
    pass

    return  render_template('error.html')
