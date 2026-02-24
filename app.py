from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# Catálogo con tus archivos locales de la barra lateral
CATALOGO = [
    {"id": 1, "nombre": "Camiseta Ciarené", "precio": 45000, "precio_antes":62000, "imagen": "camisetas.png", "categoria": "Camisas"},
    {"id": 2, "nombre": "Pantalón Premium", "precio": 85000, "imagen": "pantalon.png", "categoria": "Pantalones"},
    {"id": 3, "nombre": "Pijama Seda", "precio": 65000, "imagen": "pijama.png", "categoria": "Casual"},
    {"id": 4, "nombre": "Sudadera Sport", "precio": 75000, "imagen": "sudadera.png", "categoria": "Deportivo"},
    {"id": 5, "nombre": "Pijama Estilo", "precio": 35000, "imagen": "estilo.png", "categoria": "Casual"}
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

# Ruta para que el navegador encuentre tus fotos locales
@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)








