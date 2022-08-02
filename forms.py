from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddCupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField(
        "Flavor",
        validators=[InputRequired()],
    )

    size = StringField(
        "Size",
        validators=[InputRequired()],
    )

    rating = IntegerField(
        "Rating",
        validators=[InputRequired(), NumberRange(min=0, max=10)],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )
