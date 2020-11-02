from datetime import datetime, timedelta

from flask import render_template, request

from application import app
from kaltura_api_sessions import list


@app.route("/index")
@app.route("/home")
def index():
    return render_template('home.html')


@app.route("/videos_data/")
def videos_data():
    try:
        videos = sorted(list.result.objects, key=lambda k: k.createdAt, reverse=True)[:20]
        dt_object = datetime.fromtimestamp
        sec_converter = timedelta
        return render_template('final.html', videos=videos, dt_object=dt_object, sec_converter=sec_converter)

    except:
        return render_template('some_thing_went_wrong.html')


@app.route("/delete_video", methods=["GET", "POST"])
def delete_video():
    entry_id = request.form.get('id')
    list.client.media.delete(entry_id)


@app.route("/error")
def error_page():
    pass

    return render_template('error.html')
