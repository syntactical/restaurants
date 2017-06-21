from app import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String())
    zip_code = db.Column(db.String())
    phone = db.Column(db.String())
    grade = db.Column(db.String())
    address = db.Column(db.String())

    def __init__(id, name, city, zip_code, phone, grade, address):
        self.id = id
        self.name = name
        self.city = city
        self.zip_code = zip_code
        self.phone = phone
        self.grade = grade
        self.address = address

    def __repr__(self):
        return '<id {}>'.format(self.id)


        