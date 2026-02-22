from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_FOTOS = os.path.join(BASE_DIR, 'imagenes')

# --- "EL CUADERNO" (Base de Datos en memoria) ---
DB_USUARIOS = {} # Estructura: {"correo": {"pass": "123", "carrito": []}}

@app.route('/')
def login_page():
    return send_from_directory('.', 'login.html')

@app.route('/tienda')
def tienda_page():
    return send_from_directory('.', 'index.html')

@app.route('/carrito.html')
def carrito_page():
    return send_from_directory('.', 'carrito.html')

@app.route('/fotos/<path:filename>')
def servir_foto(filename):
    return send_from_directory(CARPETA_FOTOS, filename)

# --- API DE USUARIOS ---
@app.route('/api/auth', methods=['POST'])
def auth():
    datos = request.json
    email, password, tipo = datos.get('email'), datos.get('password'), datos.get('tipo')
    if tipo == 'registro':
        if email in DB_USUARIOS: return jsonify({"status":"error", "message":"Ya existes"}), 400
        DB_USUARIOS[email] = {"password": password, "carrito": []}
        return jsonify({"status": "success"})
    else:
        user = DB_USUARIOS.get(email)
        if user and user['password'] == password: return jsonify({"status": "success"})
        return jsonify({"status": "error", "message": "Datos incorrectos"}), 401

# --- CATÁLOGO COMPLETO ---
CATALOGO_ROPA = [
    {
        "id": 1, "nombre": "Pijama Satin", "precio": 50000, "precio_viejo": 85000,
        "imagen": "https://ciarene.up.railway.app/fotos/pijama.png",
        "tallas": ["S", "M", "L"], "colores": ["Rosado", "Negro"],
        "descripcion": "Seda satinada premium, suave y fresca."
    },
    {
        "id": 2, "nombre": "Conjunto Deportivo", "precio": 65000, "precio_viejo": None,
        "imagen": "https://ciarene.up.railway.app/fotos/sudadera.png",
        "tallas": ["M", "L", "XL"], "colores": ["Gris", "Verde"],
        "descripcion": "Licra de alta compresión para deporte."
    },
    {
        "id": 3, "nombre": "Camisas Tela Fria", "precio": 30000, "precio_viejo": 48000,
        "imagen": "https://ciarene.up.railway.app/fotos/camisetas.png",
        "tallas": ["S", "M", "L"], "colores": ["Blanco", "Negro"],
        "descripcion": "Tela fría ideal para climas cálidos."
    },
    {
        "id": 4, "nombre": "Pantalon Tache Bota Ancha", "precio": 85000, "precio_viejo": 105000,
        "imagen": "https://ciarene.up.railway.app/fotos/pantalon.png",
        "tallas": ["6", "8", "10"], "colores": ["Azul", "Negro"],
        "descripcion": "Tendencia bota ancha con detalles de taches."
    }
]

@app.route('/api/productos')
def get_productos():
    return jsonify({"status": "success", "data": CATALOGO_ROPA})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
