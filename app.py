from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

# 1. CONFIGURACIÓN DEL CATÁLOGO (Aquí puedes cambiar precios o fotos)
# Nota: He usado imágenes de alta calidad para que luzcan las animaciones
CATALOGO_ROPA = [
    {
        "id": 1, 
        "nombre": "Pijama Satin Luxe", 
        "precio": 55000, 
        "precio_old": 85000, 
        "imagen": "https://images.unsplash.com/photo-1583321500900-82807e458f3c?q=80&w=600", 
        "cat": "Pijamas"
    },
    {
        "id": 2, 
        "nombre": "Conjunto Power Gym", 
        "precio": 70000, 
        "precio_old": 95000, 
        "imagen": "https://images.unsplash.com/photo-1518310383802-640c2de311b2?q=80&w=600", 
        "cat": "Deportivo"
    },
    {
        "id": 3, 
        "nombre": "Pantalon Taches Pro", 
        "precio": 89000, 
        "precio_old": 120000, 
        "imagen": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=600", 
        "cat": "Pantalones"
    },
    {
        "id": 4, 
        "nombre": "Camisa Silk Dream", 
        "precio": 45000, 
        "precio_old": 65000, 
        "imagen": "https://images.unsplash.com/photo-1603400521630-9f2de124b33b?q=80&w=600", 
        "cat": "Pijamas"
    },
    {
        "id": 5, 
        "nombre": "Leggings Sculpt", 
        "precio": 62000, 
        "precio_old": 80000, 
        "imagen": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?q=80&w=600", 
        "cat": "Deportivo"
    }
]

# 2. RUTAS PARA SERVIR LOS ARCHIVOS HTML
@app.route('/')
def home():
    """Sirve la página principal de la tienda"""
    return send_from_directory('.', 'index.html')

@app.route('/carrito')
def ver_carrito():
    """Sirve la página del carrito de compras"""
    return send_from_directory('.', 'carrito.html')

# 3. API PARA LOS PRODUCTOS
@app.route('/api/productos')
def get_productos():
    """Devuelve la lista de productos en formato JSON para el frontend"""
    return jsonify(CATALOGO_ROPA)

# 4. INICIO DEL SERVIDOR
if __name__ == '__main__':
    # Railway usa la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' es necesario para que sea accesible desde internet
    app.run(host='0.0.0.0', port=port, debug=True)
