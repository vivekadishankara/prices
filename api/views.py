from api import app
from flask import render_template
from flask import request

from metashopper.shopper import simple_search


SHOPS = ['Amazon', 'Flipkart', 'Snapdeal']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results1')
def results1():
    item = 'Redmi 5'
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


@app.route('/results', methods=['POST'])
def results():
    item = request.form['q']
    num = int(request.form['nums'])
    nums = [num, num, num]
    search_results = simple_search(item, SHOPS, nums)

    return render_template('results.html', item=item, shops=SHOPS, results=search_results)
