from flask import Flask, request, render_template, redirect, flash, url_for, jsonify
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ThisMyapp"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """Lists of all pets
    name
    pet_photo if available
    and if pet is available for adoption or not"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """This will display a form to add new pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")

        return redirect(url_for('list_pets'))

    else:
        return render_template("pet_add_form.html", form=form)

# @app.route('/pet/<int:pet_id>')
# def showPet_info(pet_id):
#     """This will provide more info about the pet"""

#     pet = Pet.query.get_or_404(pet_id)
#     return render_template('show_pet.html', pet=pet)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data

        db.session.commit()
        flash(f"{pet.name} updated.")

        return redirect(url_for('list_pets'))
    else:
        return render_template('edit_pet.html', form=form, pet=pet)

@app.route('/api/pets/<int:per_id>', methods=["GET"])
def api_get_pet(pet_id):
    """Returns a basic info about pet in JSON"""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "species": pet.species, "age": pet.age}

    return jsonify(info)