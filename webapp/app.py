import utils
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>nice</p>'


@app.route('/item/new', methods=['POST'])
def add_item():
    req_data = request.get_json()
    item = req_data['item']

    res_data = utils.add_to_list(item)

    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')

    return response
