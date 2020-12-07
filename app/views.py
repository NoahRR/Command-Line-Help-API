from app import app, db, api
from app.models import Hints, Tags
from app.functions import does_hint_exist
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

# THIS FILE CONTAINS ALL FUNCTIONALITY FOR ALL ENDPOINTS, EXCEPT /DEV 
# (which is located in dev_views.py)

class show_all(Resource):

    def get(self):

        context = {}
        all_data = Hints().query.all()
        for hint in all_data:

            # get related tags
            display_tags = ""
            tags = Tags.query.filter_by(parent_hint=hint.id).all()
            for i in range(len(tags)):
                #  display_tags.append(str(tags[i]).split(' ')[1])
                display_tags += str(tags[i]).split(' ')[1] + ', '
            display_tags = display_tags[:-2]

            context[hint.id] = {
                'name': hint.name,
                'description': hint.description,
                'tags': display_tags
            }


        return context, 200

class start_up(Resource):

    def get(self):

        return {
            'NAVIGATION PATHS:': {
                '.../all': 'display all hints',
                '.../search/<query>': 'search for what you need to know',
                '.../dev': 'modify the database',
            }
        }, 200

class query_needed(Resource):
    def get(self):
        return {
            'Message': 'Must provide a query to search for!',
            'Example': ".../search/cd to search for 'cd'"
        }, 404

class search(Resource):
    def get(self, query):

        display_hints = {}

        # search for hint names
        #  hints = Hints.query.filter_by(name=query).all()
        hints = Hints.query.filter(Hints.name.ilike('%' + query + '%')).all()
        for hint in hints:

            # get related tags
            display_tags = ""
            tags = Tags.query.filter_by(parent_hint=hint.id).all()
            #  tags = Tags.query.filter(Tags.parent_hint.ilike(hint.id))
            for i in range(len(tags)):
                display_tags += str(tags[i]).split(' ')[1] + ', '
            display_tags = display_tags[:-2]

            display_hints[hint.id] = {
                'name': hint.name,
                'description': hint.description,
                'tags': display_tags
            }

        # search for tags
        #  maching_tags = Tags.query.filter_by(name=query).all()
        maching_tags = Tags.query.filter(Tags.name.ilike('%' + query + '%')).all()
        for tag in maching_tags:

            hint = Hints.query.filter_by(id=tag.parent_hint).first()

            # get related tags
            display_tags = ""
            tags = Tags.query.filter_by(parent_hint=hint.id).all()
            for i in range(len(tags)):
                display_tags += str(tags[i]).split(' ')[1] + ', '
            display_tags = display_tags[:-2]

            display_hints[hint.id] = {
                'name': hint.name,
                'description': hint.description,
                'tags': display_tags
            }

        if not display_hints:
            return {
                'Message': f"There were no matches for '{query}'"
            }, 404
        else:
            return display_hints, 200


"""

    ENDPOINTS / URLS

"""

api.add_resource(start_up, "/")
api.add_resource(show_all, "/all")
api.add_resource(query_needed, "/search")
api.add_resource(search, "/search/<string:query>")

