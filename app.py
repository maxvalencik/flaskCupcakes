"""Flask app for Cupcakes"""

from crypt import methods
from flask import Flask, request, jsonify, render_template, flash, redirect
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "vansusopen"

connect_db(app)


################################
# HOME

@app.route("/", methods=["GET", "POST"])
def root():
    """homepage with cupcake form"""
    form = AddCupcakeForm()

    return render_template("home.html", form=form)


################################
# GET Requests

@app.route("/api/cupcakes", methods=["GET"])
def list_cupcakes():
    """Return all cupcakes in system.
    Returns JSON:
        {cupcakes: [{id, flavor, rating, size, image}, ...]}
    """
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["GET"])
def get_cupcake(cupcake_id):
    """Return data on specific cupcake.
    Returns JSON:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id).to_dict()
    return jsonify(cupcake=cupcake)

################################
# POST Requests


@app.route("/api/cupcakes", methods=["POST"])
def add_cupcakes():
    form = AddCupcakeForm()
    if form.validate_on_submit():

        flavor = form.flavor.data
        rating = form.rating.data
        size = form.size.data
        image = form.photo_url.data or None

        cupcake = Cupcake(
            flavor=flavor,
            rating=rating,
            size=size,
            image=image
        )

        db.session.add(cupcake)
        db.session.commit()

    return redirect("/")

################################
# PATCH  Requests


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake from data in request. Return updated data.
    Returns JSON:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


################################
# DELETE  Requests

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete cupcake and return confirmation message.

    Returns JSON of {message: "Deleted"}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
