from datetime import datetime
from api import db
from metashopper.shopper import RESULT_SUB_ELEMENTS


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(64), index=True, unique=True)
    itemtime = db.Column(db.String(20))
    results = db.relationship('Result', backref='search_item', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        if not 'itemtime' in kwargs.keys():
            self.itemtime = datetime.now().strftime("%Y-%m-%d %H:%M")


    def __repr__(self):
        return '<Item {}>'.format(self.itemname)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    shop = db.Column(db.String(64))

    def __repr__(self):
        return '<Result:\n{}\n{}\n>'.format(self.shop, self.price)


for attr in RESULT_SUB_ELEMENTS:
    if attr == 'name':
        attr_column = db.Column(db.String(64))
    elif attr in ['image', 'link']:
        attr_column = db.Column(db.String(400))
    elif attr in ['price', 'reviews_num']:
        attr_column = db.Column(db.Integer)
    elif attr == 'stars':
        attr_column = db.Column(db.Float)
    else:
        attr_column = db.Column(db.String(120))
    setattr(Result, attr, attr_column)
