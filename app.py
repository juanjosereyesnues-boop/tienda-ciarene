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

# Catálogo con sistema de ofertas para Ciarené
CATALOGO_ROPA = [
    {
        "id": 1,
        "nombre": "Pijama Dama",
        "precio": 50000,
        "precio_viejo": 85000,
        "imagen": "https://ciarene.up.railway.app/fotos/pijama.png", # URL pública
        "categoria": "Pijamas"
    },
    {
        "id": 2,
        "nombre": "Conjunto Deportivo",
        "precio": 65000,
        "precio_viejo": None,
        "imagen": "https://ciarene.up.railway.app/fotos/sudadera.png",
        "categoria": "Deportivo"
    },
    {
        "id": 3,
        "nombre": "Camisas Tela Fria",
        "precio": 30000,
        "precio_viejo": 48000,
        "imagen": "https://ciarene.up.railway.app/fotos/camisetas.png",
        "categoria": "Camisas"
    },
    {
        "id": 4,
        "nombre": "Pantalon Tache Bota Ancha",
        "precio": 85000,
        "precio_viejo": 105000,
        "imagen": "https://ciarene.up.railway.app/fotos/pantalon.png",
        "categoria": "Pantalones"
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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)



