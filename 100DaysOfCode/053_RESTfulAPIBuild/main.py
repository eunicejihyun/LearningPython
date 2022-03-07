from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
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


@app.route("/random")
def random():
    cafe_count = Cafe.query.count()
    random_cafe = Cafe.query.offset(randint(0, cafe_count - 1)).first()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    # This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_location)
    if cafes.count() > 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/update", methods=['PATCH'])
def update():
    cafe_id = request.args.get("id")
    new_price = request.args.get("price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated!~"), 200
    else:
        return jsonify(error={"Not Found": "There isn't a cafe with that ID in the database."}), 404


@app.route("/delete/<int:id>", methods=['DELETE'])
def delete():
    cafe_id = request.args.get(id)
    cafe = db.session.query(Cafe).get(cafe_id)
    api_key = request.args.get("api-key")
    acceptable_api_keys = ['1', '2', '3']
    if api_key in acceptable_api_keys:
        if cafe:
            cafe.delete()
            return jsonify(success="Successfully Deleted."), 200
        else:
            return jsonify(error={"Not Found": "There isn't a cafe with that ID in the database."}), 404
    else:
        return jsonify(error={"Error": "Not allowed - Check your API key"}), 403





## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
