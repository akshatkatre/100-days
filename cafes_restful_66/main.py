from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/cafes", methods=['GET'])
def get_cafes():
    cafes = [cafe.to_dict() for cafe in db.session.query(Cafe).all()]
    return jsonify(cafes)


@app.route("/search", methods=['GET'])
def search():
    loc = request.args.get("loc")
    print(loc)
    results = db.session.query(Cafe).filter(Cafe.location == loc).all()
    print(results)
    if len(results) == 0:
        return jsonify({"error": {
            "Not found": "Sorry, we don't have any cafes in this location"
        }})
    return jsonify({"cafes": [
        cafe.to_dict() for cafe in results
    ]})


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    print('Inside add...')
    for fieldname, value in request.json.items():
        print(fieldname, value)
    new_cafe = Cafe(can_take_calls=request.json['can_take_calls'],
                    coffee_price=request.json['coffee_price'],
                    has_sockets=request.json['has_sockets'],
                    has_toilet=request.json['has_toilet'],
                    has_wifi=request.json['has_wifi'],
                    img_url=request.json['img_url'],
                    location=request.json['location'],
                    map_url=request.json['map_url'],
                    name=request.json['name'],
                    seats=request.json['seats']
                    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"success": True})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    print('Inside PATCH update_price()')
    new_coffee_price = request.args.get("coffee_price")
    record_to_be_updated = Cafe.query.get(cafe_id)
    if record_to_be_updated is None:
        return jsonify({'error': {'description': f'Cafe with ID {cafe_id} not found '}}), 404
    print(f'old price: {record_to_be_updated.coffee_price} vs new price: {new_coffee_price}')
    record_to_be_updated.coffee_price = new_coffee_price
    db.session.commit()
    return jsonify({"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
@app.route('/cafe/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    print(f'Inside DELETE delete_cafe(), id: {cafe_id}')

    if request.args.get('api_key') != 'Top-Secret-API-Key':
        return jsonify({'error': "Sorry this isn't allowed. Invalid api key"}), 403

    cafe = Cafe.query.get(cafe_id)
    if cafe:
        print('Cafe found. Proceeding with delete.')
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({'success': f"Cafe with id {cafe_id} has been deleted."})
    else:
        return jsonify({'error': f"Cafe with id {cafe_id} does not exist"}), 404


if __name__ == '__main__':
    app.run(debug=True)
