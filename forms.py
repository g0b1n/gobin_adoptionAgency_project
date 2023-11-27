from flask_wtf import FlaskForm
from wtforms import StringField,  IntegerField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name", validators=[InputRequired(message="Pet Name Cannot be Blank")])
    species = StringField("Species", validators=[InputRequired(message="Pet Species Cannot be Blank")])
    age = IntegerField("Age", validators=[InputRequired(message="Age Cannot be Blank"), NumberRange(min=1, max=100)])
    notes = TextAreaField("About Pet", validators=[Optional(), Length(min=50)])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

class EditPetForm(FlaskForm):
    """Form for editing pet details"""

    name = StringField("Name", validators=[InputRequired(message="Pet Name Cannot be Blank")])
    species = StringField("Species", validators=[InputRequired(message="Pet Species Cannot be Blank")])
    age = IntegerField("Age", validators=[InputRequired(message="Age Cannot be Blank"), NumberRange(min=1, max=100)])
    notes = TextAreaField("About Pet", validators=[Optional(), Length(min=50)])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    available = BooleanField("Available")