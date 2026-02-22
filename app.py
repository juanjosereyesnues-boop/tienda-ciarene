from flask import Flask, jsonify, send_from_directory
import os

# Definimos la carpeta raíz para que Flask encuentre los archivos
app = Flask(__name__, static_url_path='', static_folder='.')

# --- CATÁLOGO ---
CATALOGO = [
    {"id": 1, "nombre": "Pijama Satin Luxe", "precio": 55000, "precio_old": 85000, "imagen": "https://images.unsplash.com/photo-1583321500900-82807e458f3c?q=80&w=600", "cat": "Pijamas"},
    {"id": 2, "nombre": "Conjunto Power Gym", "precio": 70000, "precio_old": 95000, "imagen": "https://images.unsplash.com/photo-1518310383802-640c2de311b2?q=80&w=600", "cat": "Deportivo"},
    {"id": 3, "nombre": "Pantalon Taches Pro", "precio": 89000, "precio_old": 120000, "imagen": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=600", "cat": "Pantalones"}
]

# --- RUTAS MEJORADAS ---

@app.route('/')
def home():
    # Obligamos a Flask a buscar el index.html en la raíz
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/carrito')
def carrito():
    # Obligamos a Flask a buscar el carrito.html en la raíz
    return send_from_directory(app.static_folder, 'carrito.html')

@app.route('/api/productos')
def get_productos():
    return jsonify(CATALOGO)

# Ruta de seguridad para archivos estáticos (evita el 404 de CSS/JS)
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
