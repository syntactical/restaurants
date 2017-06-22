import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from models.restaurant import Restaurant, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/restaurants'
db.init_app(app)
with app.app_context():
        db.create_all()
from data.etl import load_restaurant_data
load_restaurant_data('./data/inspections.csv')

@app.route('/')
def hello():
    restaurants = Restaurant.query.limit(5).all()
    return render_template('restaurants.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run()
