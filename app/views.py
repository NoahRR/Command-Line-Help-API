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


        return context

class start_up(Resource):

    def get(self):

        context = {
            'NAVIGATION PATHS:': {
                '.../all': 'display all hints',
                '.../search/<query>': 'search for hint or tag',
                '.../search-tag/<query>': 'search for tag',
                '.../search-hint/<query>': 'search for hint',
                '.../dev': 'modify the database',
            }
        }

        return context

class search(Resource):
    def get(self, query):

        display_hints = {}

        # search for hint names
        hints = Hints.query.filter_by(name=query).all()
        for hint in hints:

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

        # search for tags
        maching_tags = Tags.query.filter_by(name=query).all()
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
            return f"There were no hints or tags under the name '{query}'"
        else:
            return display_hints

class search_hint(Resource):
    def get(self, query):

        display_hints = {}
        hints = Hints.query.filter_by(name=query).all()

        for hint in hints:

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
            return f"There were no hints under the name '{query}'"
        else:
            return display_hints

class search_tag(Resource):
    def get(self, query):

        display_hints = {}
        maching_tags = Tags.query.filter_by(name=query).all()
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
            return f"There were no hints with the tag '{query}'"
        else:
            return display_hints




"""

    ENDPOINTS / URLS

"""

api.add_resource(start_up, "/")
api.add_resource(show_all, "/all")
api.add_resource(search, "/search/<string:query>")
api.add_resource(search_hint, "/search-hint/<string:query>")
api.add_resource(search_tag, "/search-tag/<string:query>")

