from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "Primeiro item"},
    {"id": 2, "name": "Item 2", "description": "Segundo item"},
]
next_id = 3


@app.route("/")
def index():
    return jsonify({"message": "API RESTful Flask na Azure"})


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


@app.route("/items", methods=["POST"])
def create_item():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    new_item = {"id": next_id, "name": data["name"], "description": data.get("description", "")}
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])
    return jsonify(item)


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    items = [i for i in items if i["id"] != item_id]
    return jsonify({"message": f"Item {item_id} deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True, port=5002)
