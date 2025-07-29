import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = 'items.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(load_data())

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    items = load_data()
    item = next((i for i in items if i['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

@app.route('/items', methods=['POST'])
def create_item():
    items = load_data()
    new_item = request.json
    new_id = max(i['id'] for i in items) + 1 if items else 1
    new_item['id'] = new_id
    items.append(new_item)
    save_data(items)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    items = load_data()
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        return '', 404
    item.update(request.json)
    save_data(items)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = load_data()
    items = [i for i in items if i['id'] != item_id]
    save_data(items)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)