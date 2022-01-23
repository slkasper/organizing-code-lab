from flask import Flask, jsonify
import psycopg2
from venue import Venue
from category import Category

app = Flask(__name__)


@app.route('/venues')
def venues():
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM venues;')
    venues = cursor.fetchall()
    venue_objs = [Venue(venue).__dict__ for venue in venues]
    return jsonify(venue_objs)

@app.route('/venues/<id>')
def show_venue(id):
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM venues WHERE id = %s LIMIT 1;", id)
    venue_values = cursor.fetchone()
    return jsonify(Venue(venue_values).__dict__)

app.run(debug = True)