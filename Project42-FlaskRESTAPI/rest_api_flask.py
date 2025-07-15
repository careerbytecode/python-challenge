from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": items}), 200

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
        return jsonify({"message": "Name and price are required"}), 400

    name = data["name"].strip()
    price = data["price"]

    if not isinstance(price, (int, float)):
        return jsonify({"message": "Price must be a number"}), 400

    item = {
        "name": name,
        "price": float(price)
    }
    items.append(item)

    return jsonify({
        "message": "Item added successfully",
        "item": item
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
