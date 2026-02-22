from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# Catálogo optimizado con tus archivos reales
CATALOGO = [
    {"id": 1, "nombre": "Colección Camisetas", "precio": 45000, "imagen": "camisetas.png", "desc": "Algodón premium 100%"},
    {"id": 2, "nombre": "Pantalón Elegance", "precio": 85000, "imagen": "pantalon.png", "desc": "Corte estilizado y cómodo"},
    {"id": 3, "nombre": "Pijama Dreamer", "precio": 65000, "imagen": "pijama.png", "desc": "Seda fría para el mejor descanso"},
    {"id": 4, "nombre": "Sudadera Urban", "precio": 75000, "imagen": "sudadera.png", "desc": "Estilo deportivo y moderno"}
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
