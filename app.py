"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm, EditPetForm

from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """Render homepage and show all pets and their availability"""
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Render add pet form and validate form inputs"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        note = form.note.data

        photo_url = None if form.photo_url.data == '' else form.photo_url.data


        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            note=note
        )

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=["POST", "GET"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = None if form.photo_url.data == '' else form.photo_url.data
        note = form.note.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.note = note
        pet.available = available

        db.session.commit()
        flash(f"Pet {pet_id} updated!")

        return redirect(f'/{pet_id}')

    else:
        return render_template('edit_pet.html', form=form, pet=pet)



