from app import db

class Hints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f"Name: {self.name}"

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_hint = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Name: {self.name}"
