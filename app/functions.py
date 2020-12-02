from flask_restful import abort
from app import db
from app.models import Hints

def does_hint_exist(id):
    print(Hints.query.filter_by(id=id).first())

    try:
        test_hint = Hints.query.filter_by(id=id).first()
        test_existence = test_hint.name
    except:
        abort(404, message="No hint exists with that id!")
