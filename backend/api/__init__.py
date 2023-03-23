from flask import Flask, jsonify
import psycopg2
from api.models.venue import Venue
from api.models.category import Category
import json # to fix decimal error when running the venue route

def create_app(database, db_user):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database, 
        DB_USER=db_user
        )

    @app.route('/venues')
    def venues():
        conn = psycopg2.connect(database = app.config['DATABASE'], 
                                user = app.config['DB_USER'], 
                                password = 'postgres')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM venues;')
        venues = cursor.fetchall()
        venue_objs = [Venue(venue).__dict__ for venue in venues]
        #return jsonify(venue_objs)
        return json.dumps(venue_objs, default=str ) #to fix decimal error in route

    @app.route('/venues/<id>')
    def show_venue(id):
        conn = psycopg2.connect(database = app.config['DATABASE'], 
                                user = app.config['DB_USER'], 
                                password = 'postgres')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM venues WHERE id = %s LIMIT 1;", id)
        venue_values = cursor.fetchone()
        venue_dict = Venue(venue_values).__dict__
        return json.dumps(venue_dict, default=str)

    return app

