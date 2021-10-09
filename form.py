from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    input = StringField(
        'Input',
        [DataRequired()])
    # Username format by hackersandclasckers

    cat = ['Rent', 'Gas', 'Food']

    category = SelectField(
        label='Categories',
        choices=cat)

    submit = SubmitField('Submit!')