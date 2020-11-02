from application import app, api
from flask import render_template, request, jsonify
from datetime import datetime, timedelta
from kaltura_api_sessions import delete_entry, list, get_entry
from flask_restplus import Resource


# from application.models import User, Course, Enrollment
# from application.forms import LoginForm, RegistratinForm
# from flask_restplus import Resource
# from application.courses_list import course_list


##################################################
@api.route('/api', '/api/')
class GetAndPost(Resource):

    # GET ALL
    def get(self):
        entries = sorted(list.result.objects, key=lambda k: k.createdAt, reverse=True)
        output = []

        for entry in entries:
            entry_data = {}
            entry_data['id'] = entry.id
            entry_data['name'] = entry.name
            output.append(entry_data)
        return jsonify({'entries': output})

    def post(self):
        pass


@api.route('/api/<idx>')
class GetUpdateDelete(Resource):

    # GET ONE
    def get(self, idx):
        try:
            result = get_entry.get_entry(idx)
            return result
        except:
            return jsonify({'message': 'Failed to get entry!'})

    # DELETE
    def delete(self, idx):

        try:
            delete_entry.delete(idx)
            return jsonify({'message': 'Entry item deleted!'})
        except:
            return jsonify({'message': 'Entry deleted Failed!'})


##################################################

@app.route("/index")
@app.route("/")
def index():
    return 'hey'


@app.route("/videos_data/")
def videos_data():
    try:
        videos = sorted(list.result.objects, key=lambda k: k.createdAt, reverse=True)
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
