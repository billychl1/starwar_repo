from flask import Flask, jsonify, make_response
from starwar.models import db, ShipRecord
from starwar.config import configure_app

app = Flask(
    __name__)            

configure_app(app)

db.init_app(app)

@app.route('/starwarships', methods=['GET'])
def get_starwarships():
    ships = [ship for ship in ShipRecord.query.order_by(ShipRecord.hyperdriverating).all()]

    return jsonify(data=[ship.serialize for ship in ships])

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

