from flask import jsonify
from flask_restplus import Resource

from application import api
from kaltura_api_sessions.kaltura_envoke_sessions import delete, get_entry
from kaltura_api_sessions import list


@api.route('/api', '/api/')
class Get(Resource):

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


@api.route('/api/<idx>')
class GetUpdateDelete(Resource):

    # GET ONE
    def get(self, idx):
        try:
            result = get_entry(idx)
            return result
        except:
            return jsonify({'message': 'Failed to get entry!'})

    # DELETE ONE
    def delete(self, idx):

        try:
            delete(idx)
            return jsonify({'message': 'Entry item deleted!'})
        except:
            return jsonify({'message': 'Entry deleted Failed!'})
