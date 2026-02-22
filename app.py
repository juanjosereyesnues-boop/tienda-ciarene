from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# Agregamos static_folder='.' para que Flask sepa buscar el HTML en la raíz
app = Flask(__name__, static_folder='.')
CORS(app)

# Configuración de carpetas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_FOTOS = os.path.join(BASE_DIR, 'imagenes')

# --- ESTO ES LO QUE SOLUCIONA EL ERROR 404 EN RAILWAY ---
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/carrito.html')
def carrito():
    return send_from_directory('.', 'carrito.html')
# -------------------------------------------------------

# Servir imágenes locales de forma profesional
@app.route('/fotos/<path:filename>')
def servir_foto(filename):
    return send_from_directory(CARPETA_FOTOS, filename)

# Catálogo actualizado con Tallas y Colores para el Modal tipo Temu
CATALOGO_ROPA = [
    {
        "id": 1,
        "nombre": "Pijama Satin",
        "precio": 50000,
        "precio_viejo": 85000,
        "imagen": "https://ciarene.up.railway.app/fotos/pijama.png",
        "categoria": "Pijamas",
        "tallas": ["S", "L"],
        "colores": ["<h1>Consulte En La Compra"]
    },
    {
        "id": 2,
        "nombre": "Conjunto Deportivo",
        "precio": 65000,
        "precio_viejo": None,
        "imagen": "https://ciarene.up.railway.app/fotos/sudadera.png",
        "categoria": "Deportivo",
        "tallas": ["Única"],
        "colores": ["Rojo", "Negro"]
    },
    {
        "id": 3,
        "nombre": "Camisas Tela Fria",
        "precio": 30000,
        "precio_viejo": 48000,
        "imagen": "https://ciarene.up.railway.app/fotos/camisetas.png",
        "categoria": "Camisas",
        "tallas": ["S", "M", "L", "XL"],
        "colores": ["Blanco", "Negro", "Rojo"]
    },
    {
        "id": 4,
        "nombre": "Pantalon Tache Bota Ancha",
        "precio": 85000,
        "precio_viejo": 105000,
        "imagen": "https://ciarene.up.railway.app/fotos/pantalon.png",
        "categoria": "Pantalones",
        "tallas": ["6", "8", "10", "12"],
        "colores": ["Azul Oscuro", "Negro"]
    },
    {
        "id": 5,
        "nombre": "Pijamas Con Diseño",
        "precio": 35000,
        "precio_viejo": None,
        "imagen": "https://ciarene.up.railway.app/fotos/pijama2.jpeg",
        "categoria": "Pijamas",
        "tallas": ["Única"],
        "colores": ["Estampado"]
    }
]

@app.route('/api/productos', methods=['GET'])
def get_productos():
    return jsonify({
        "status": "success",
        "tienda": "Ciarené",
        "data": CATALOGO_ROPA
    })

if __name__ == '__main__':
    # Railway usa la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)



