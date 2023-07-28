"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional




"""
Pet name
Species
Photo URL
Age
Notes
"""

class AddPetForm(FlaskForm):
    name = StringField("Pet Name",
           validators=[InputRequired()])
    species = StringField("Species",
           validators=[InputRequired()])
    photo_url = StringField("Photo URL",
           validators=[Optional()])
    age = SelectField("Age",
           choices=[('baby', "Baby"), ('young', "Young"),
           ('adult', "Adult"), ('senior', "Senior")],
           validators=[InputRequired()])
    notes = TextAreaField("Notes",
           validators=[Optional()])


