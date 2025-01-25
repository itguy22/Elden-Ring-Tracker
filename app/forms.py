from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired

class ZoneForm(FlaskForm):
    name = StringField('Zone Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Zone')


class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    description = StringField('Description')
    acquired = BooleanField('Acquired')
    zone_id = SelectField('Zone', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
