from api import app
from flask import render_template
from flask import request, redirect, url_for

from api import db
from api.models import Item, Result

import configuration as config
from metashopper.shopper import simple_search, ITEM_ATTR


SHOPS = ['Amazon', 'Flipkart', 'Snapdeal']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results1', methods=['POST'])
def results1():
    item = request.form['q']
    try:
        pums = request.form['gums']
        print(pums)
    except:
        pass
    fp = open('results.csv')
    lines = fp.readlines()
    res = []
    for line in lines:
        a = eval(line)
        res.append(a)
    results = {}
    for i in range(len(SHOPS)):
        results[SHOPS[i]] = res[(i)*5 : (i+1)*5-1]

    return render_template('results.html', item=item, shops=SHOPS, results=results)


@app.route('/results2', methods=['POST'])
def results2():
    item = request.form['q']
    num = int(request.form['nums'])
    nums = [num, num, num]
    search_results = simple_search(item, SHOPS, nums)

    return render_template('results.html', item=item, shops=SHOPS, results=search_results)


@app.route('/results', methods=['POST'])
def results():
    item, num, nums = get_search_items()
    item_filter = Item.query.filter_by(itemname=item).first()

    if item_filter:
        search_results = {}
        for shop, num_i in zip(SHOPS, nums):
            results_filter = item_filter.results.filter_by(shop=shop).all()
            if len(results_filter) < num_i:
                return redirect(url_for('results_new'), code=307)
            shop_results = []
            for resf in results_filter[:num]:
                res = {}
                for attr in ITEM_ATTR:
                    res[attr] = getattr(resf, attr)
                shop_results.append(res)
            search_results[shop] = shop_results
    else:
        return redirect(url_for('results_new'), code=307)  # code=307 for post method
    return render_template('results.html', item=item, shops=SHOPS, results=search_results)


@app.route('/results_new', methods=['POST'])
def results_new():
    item, num, nums = get_search_items()
    search_results = simple_search(item, SHOPS, nums)
    it = Item.query.filter_by(itemname=item).first()
    if it:
        it.results.delete()
        db.session.commit()
    else:
        it = Item(itemname=item)
        db.session.add(it)
        db.session.commit()

    for shop, num_i in zip(SHOPS, nums):
        for i in range(num_i):
            result_db = Result(shop=shop, search_item=it, **search_results.get(shop)[i])
            db.session.add(result_db)

    db.session.commit()
    return redirect(url_for('results'), code=307)


def get_search_items():
    item = request.form['q']
    num = int(request.form['nums'])
    num_op = num
    if num < config.SEARCH_RESERVE:
        num_op = config.SEARCH_RESERVE
    nums = [num_op, num_op, num_op]
    return item, num, nums


def read_csv():
    fp = open('results.csv')
    lines = fp.readlines()
    res = []
    for line in lines:
        a = eval(line)
        res.append(a)
    search_results = {}
    for i in range(len(SHOPS)):
        search_results[SHOPS[i]] = res[(i) * 5: (i + 1) * 5]
    return search_results


if __name__ == '__main__':
    app.run()