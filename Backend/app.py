from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
     return jsonify({ "message": " Welcome to K8s E-commerce Backend API"})

@app.route('/api/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Headphones", "price": 2000},
        {"id": 3, "name": "Keyboard", "price": 1500}
    ])

@app.route('/api/users')
def users():
    return jsonify([
        {"id": 1, "name": "Pawan Patil"},
        {"id": 2, "name": "Customer User"}
    ])

@app.route('/api/orders')
def orders():
    return jsonify([
        {"order_id": 101, "product": "Laptop", "user": "Pawan Patil"},
        {"order_id": 102, "product": "Headphones", "user": "Customer User"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

