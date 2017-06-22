import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models.restaurant import Restaurant
from models.restaurant import db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    from data.etl import load_restaurant_data
    load_restaurant_data('./data/inspections.csv')
    app.run()

