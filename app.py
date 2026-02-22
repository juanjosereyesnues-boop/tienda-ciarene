from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# Catálogo simple
CATALOGO = [
    {"id": 1, "nombre": "Pijama Satin Luxe", "precio": 55000, "imagen": "https://images.unsplash.com/photo-1583321500900-82807e458f3c?w=500"},
    {"id": 2, "nombre": "Conjunto Power Gym", "precio": 70000, "imagen": "https://images.unsplash.com/photo-1518310383802-640c2de311b2?w=500"},
    {"id": 3, "nombre": "Pantalon Taches Pro", "precio": 89000, "imagen": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500"}
]

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/carrito')
def cart():
    return send_from_directory('.', 'carrito.html')

@app.route('/api/productos')
def api():
    return jsonify(CATALOGO)

if __name__ == '__main__':
    # Railway necesita esto sí o sí
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
