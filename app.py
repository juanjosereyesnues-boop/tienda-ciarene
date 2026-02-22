from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

CATALOGO = [
    {"id": 1, "nombre": "Camiseta Ciarené", "precio": 45000, "imagen": "camisetas.png"},
    {"id": 2, "nombre": "Pantalón Premium", "precio": 85000, "imagen": "pantalon.png"},
    {"id": 3, "nombre": "Pijama Seda", "precio": 65000, "imagen": "pijama.png"},
    {"id": 4, "nombre": "Sudadera Sport", "precio": 75000, "imagen": "sudadera.png"}
]

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/carrito')
def cart_page():
    return send_from_directory('.', 'carrito.html')

@app.route('/api/productos')
def api_productos():
    return jsonify(CATALOGO)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
