from app import app, db, api
from app.models import Hints
from app.functions import does_hint_exist
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy


class db_config(Resource):

    # shows all data
    def get(self):

        context = {}
        all_data = Hints().query.all()
        for hint in all_data:
            context[hint.name] = {
                'id': hint.id,
                'description': hint.description,
                'class': hint.classification
            }
        return context

    # inserts new data
    def post(self):

        # ensure correct arguments are passed
        dev_changes_new = reqparse.RequestParser()
        dev_changes_new.add_argument(
            'name',
            type=str,
            help="The 'name' parameter is required",
            required=True
        )
        dev_changes_new.add_argument(
            'description',
            type=str,
            help="The 'description' parameter is required",
            required=True
        )
        args = dev_changes_new.parse_args()

        # create new hint
        newHint = Hints(name=args['name'], description=args['description'])
        db.session.add(newHint)
        db.session.commit()

        return {'Added new hint': args['name']}

    # deletes data
    def delete(self):
        
        # ensure correct arguments are passed
        dev_changes_del = reqparse.RequestParser()
        dev_changes_del.add_argument(
            'id',
            type=int,
            help="The 'id' parameter is required to perform a delete",
            required=True
        )
        args = dev_changes_del.parse_args()

        # check hint exists
        does_hint_exist(args['id'])

        # delete
        hint_to_del = Hints.query.filter_by(id=args['id']).first()
        del_id = hint_to_del.id
        del_name = hint_to_del.name
        db.session.delete(hint_to_del)
        db.session.commit()

        return {
            'Deleted hint!': {
                'id': del_id,
                'name': del_name
            }
        }

    # updates data
    def put(self):

        # ensure correct arguments are passed
        dev_changes_update = reqparse.RequestParser()
        dev_changes_update.add_argument(
            'id',
            type=int,
            help="The 'id' parameter is required to perform a delete",
            required=True
        )
        dev_changes_update.add_argument(
            'name',
            type=str,
            help="The 'name' parameter is required",
        )
        dev_changes_update.add_argument(
            'description',
            type=str,
            help="The 'description' parameter is required",
        )
        args = dev_changes_update.parse_args()

        # updates hint
        hint_update = Hints.query.filter_by(id=args['id']).first()
        if args['name']:
            hint_update.name = args['name']
        if args['description']:
            hint_update.description = args['description']
        db.session.add(hint_update)
        db.session.commit()

        return {'Updated hint with id of': args['id']}

class show_all(Resource):
    def get(self):
        context = {}
        all_data = Hints().query.all()
        for hint in all_data:
            context[hint.name] = {
                'id': hint.id,
                'description': hint.description,
                'class': hint.classification
            }
        return context

class start_up(Resource):
    def get(self):
        context = {
            'NAVIGATION PATHS:': {
                '.../all': 'display all hints',
                '.../dev': 'modify the database'
            }
        }
        return context


"""

    ENDPOINTS / URLS

"""

api.add_resource(start_up, "/")
api.add_resource(db_config, "/dev")
#  api.add_resource(, "/beginner")
api.add_resource(show_all, "/all")
#  api.add_resource(, "/navigation")
#  api.add_resource(, "/file-commands")
#  api.add_resource(, "/viewing")
#  api.add_resource(, "/system-information")
#  api.add_resource(, "/process-management")
#  api.add_resource(, "/file-permissions")
#  api.add_resource(, "/ssh")
#  api.add_resource(, "/searching")
#  api.add_resource(, "/compression")
#  api.add_resource(, "/network")
#  api.add_resource(, "/installation")
#  api.add_resource(, "/key-shortcuts")
