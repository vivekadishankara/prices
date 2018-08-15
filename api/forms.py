from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import IntegerField
import configuration as global_config


class SearchForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()], render_kw={'autofocus':True})
    results = IntegerField('Results', render_kw={'style':"width:60px", 'min':"1", 'value':"1"})
    submit = SubmitField('Search', render_kw={'class':"btn-primary"})
    submit_new = SubmitField('new Search', render_kw={'class':"btn-primary"})

    def get_search_items(self):
        item = self.item.data
        num = int(self.results.data)
        num_op = num
        if num < global_config.SEARCH_RESERVE:
            num_op = global_config.SEARCH_RESERVE
        nums = [num_op, num_op, num_op]
        return item, num, nums