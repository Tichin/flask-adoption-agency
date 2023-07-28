"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL


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
    species = SelectField("Species",
                          choices=[('cat', "Cat"), ('dog', "Dog"),
                                   ('porcupine', "Porcupine")],
                          validators=[InputRequired()])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[('baby', "Baby"), ('young', "Young"),
                               ('adult', "Adult"), ('senior', "Senior")],
                      validators=[InputRequired()])
    note = TextAreaField("Notes",
                         validators=[Optional()])
