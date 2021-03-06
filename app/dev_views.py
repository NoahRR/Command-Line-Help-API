from app import app, db, api
from app.models import Hints, Tags
from app.functions import does_hint_exist
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

# THIS FILE CONTAINS ALL FUNCTIONALITY FOR /DEV ENDPOINT

class db_config(Resource):

    # shows all data
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
        dev_changes_new.add_argument(
            'tags',
            type=str,
        )
        args = dev_changes_new.parse_args()

        # create new hint
        newHint = Hints(name=args['name'], description=args['description'])

        # saving info
        newHint_name = args['name']
        newHint_description = args['description']

        # save new hint to database
        db.session.add(newHint)
        db.session.commit()
        newHint_id = newHint.id

        # save tags associated with hint
        tag_names = []
        if args.tags:
            for tag in args.tags.split(','):
                new_tag_name = tag.strip()
                new_tag = Tags(parent_hint=newHint_id, name=new_tag_name)
                tag_names.append(new_tag_name)
                db.session.add(new_tag)
                db.session.commit()


        return {
            'Added new hint': {
                'id': newHint_id,
                'name': newHint_name,
                'description': newHint_description,
            },
            'Added the following tags': tag_names,
        }, 201

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

        # delete hint
        hint_to_del = Hints.query.filter_by(id=args['id']).first()
        del_id = hint_to_del.id
        del_name = hint_to_del.name

        # delete related tags
        tags_to_del = Tags.query.filter_by(parent_hint=del_id).all()
        for tag in tags_to_del:
            db.session.delete(tag)
            db.session.commit()

        db.session.delete(hint_to_del)
        db.session.commit()

        return {
            'Deleted hint!': {
                'id': del_id,
                'name': del_name
            }
        }, 200

    # updates data
    def put(self):

        # ensure correct arguments are passed
        dev_changes_update = reqparse.RequestParser()
        dev_changes_update.add_argument(
            'id',
            type=int,
            help="The 'id' parameter is required to update a hint",
            required=True
        )
        dev_changes_update.add_argument(
            'name',
            type=str,
        )
        dev_changes_update.add_argument(
            'description',
            type=str,
        )
        dev_changes_update.add_argument(
            'tags',
            type=str
        )
        args = dev_changes_update.parse_args()

        # updates hint
        hint_update = Hints.query.filter_by(id=args['id']).first()
        if args['name']:
            hint_update.name = args['name']
        if args['description']:
            hint_update.description = args['description']

        # remove previous tags associated with hint
        tag_names = []
        if args.tags:
            tags_to_del = Tags.query.filter_by(parent_hint=args['id']).all()
            for tag in tags_to_del:
                db.session.delete(tag)
                db.session.commit()

            # save tags associated with hint
            if args.tags:
                for tag in args.tags.split(','):
                    new_tag_name = tag.strip()
                    new_tag = Tags(parent_hint=args['id'], name=new_tag_name)
                    tag_names.append(new_tag_name)
                    db.session.add(new_tag)
                    db.session.commit()

        db.session.add(hint_update)
        db.session.commit()

        return {
            'Updated hint': {
                'id': args['id'],
                'name': hint_update.name,
                'description': hint_update.description,
            },
            'Added the following tags': tag_names,
        }, 200


"""

    ENDPOINTS / URLS

"""

api.add_resource(db_config, "/dev")
