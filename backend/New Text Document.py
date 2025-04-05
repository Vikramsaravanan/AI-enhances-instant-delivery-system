from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/new_order', methods=['POST'])
def add_order():
    data = request.json
    orders.append(data)
    return jsonify({"status": "Order added!"})

@app.route('/assign_agent', methods=['GET'])
def assign_agent():
    # Logic to assign nearest agent (using routing & Hungarian)
    return jsonify({"agent": "Driver_5", "ETA": "15 mins"})

if __name__ == '__main__':
    app.run(debug=True)