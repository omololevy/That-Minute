from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired

CATEGORY_CHOICES = [('Pickup_lines', 'Pickup_lines'), ('Interview', 'Interview'), ('Advertisement', 'Advertisement'), ('Humour', 'Humour')]

class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[DataRequired()])
    category = SelectField('Click to select category',choices=CATEGORY_CHOICES,validators=[DataRequired()])
    pitch = TextAreaField('Write a one minute pitch.',validators = [DataRequired()])
    
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Write your comment.',validators = [DataRequired()])
    
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write more about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')
