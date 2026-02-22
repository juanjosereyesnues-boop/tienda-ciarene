from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

# CATALOGO DE LUJO
CATALOGO = [
    {"id": 1, "nombre": "Pijama Satin Luxe", "precio": 55000, "precio_old": 85000, "imagen": "https://images.unsplash.com/photo-1583321500900-82807e458f3c?q=80&w=600", "cat": "Pijamas"},
    {"id": 2, "nombre": "Conjunto Power Gym", "precio": 70000, "precio_old": 95000, "imagen": "https://images.unsplash.com/photo-1518310383802-640c2de311b2?q=80&w=600", "cat": "Deportivo"},
    {"id": 3, "nombre": "Pantalon Taches Pro", "precio": 89000, "precio_old": 120000, "imagen": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=600", "cat": "Pantalones"},
    {"id": 4, "nombre": "Body Lace Premium", "precio": 45000, "precio_old": 70000, "imagen": "https://images.unsplash.com/photo-1612601006505-1254db3e290d?q=80&w=600", "cat": "Pijamas"}
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/carrito')
def cart_page():
    return send_from_directory('.', 'carrito.html')

@app.route('/api/productos')
def get_prods():
    return jsonify(CATALOGO)

# Evita el error 404 buscando cualquier archivo local (imágenes, css, js)
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
