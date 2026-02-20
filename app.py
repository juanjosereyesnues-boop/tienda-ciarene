from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuración de carpetas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_FOTOS = os.path.join(BASE_DIR, 'imagenes')

# Servir imágenes locales de forma profesional
@app.route('/fotos/<path:filename>')
def servir_foto(filename):
    return send_from_directory(CARPETA_FOTOS, filename)

# Catálogo con sistema de ofertas para Ciarené
# Si precio_viejo es None, no sale oferta. Si tiene número, sale tachado.
CATALOGO_ROPA = [
    {
        "id": 1,
        "nombre": "Pijama Dama",
        "precio": 50000,
        "precio_viejo": 85000,
        "imagen": "http://192.168.1.15:5000/fotos/pijama.png",
        "categoria": "Vestidos"
    },
    {
        "id": 2,
        "nombre": "Conjunto Deportivo",
        "precio": 65000,
        "precio_viejo": None,
        "imagen": "http://192.168.1.15:5000/fotos/sudadera.png",
        "categoria": "Blusas"
    },
    {
        "id": 3,
        "nombre": "Camisas Tela Fria",
        "precio": 30000,
        "precio_viejo": 48000,
        "imagen": "http://192.168.1.15:5000/fotos/camisetas.png",
        "categoria": "Chaquetas"
    },
    {
        "id": 3,
        "nombre": "Pantalon Tache Bota Ancha",
        "precio": 30000,
        "precio_viejo": 48000,
        "imagen": "http://192.168.1.15:5000/fotos/pantalon.png",
        "categoria": "Chaquetas"
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
    # Railway asigna el puerto mediante una variable de entorno
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)