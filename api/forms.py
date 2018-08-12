from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import IntegerField


class SearchForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()], render_kw={'autofocus':True})
    results = IntegerField('Results', render_kw={'style':"width:60px", 'min':"1", 'value':"1"})
    submit = SubmitField('Compare', render_kw={'class':"btn-primary"})