from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder='.')
CORS(app)

DB_FILE = 'usuarios_db.json'

def cargar_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as f:
        try: return json.load(f)
        except: return {}

def guardar_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f)

# --- RUTAS DE PÁGINAS ---
@app.route('/')
def login_p(): return send_from_directory('.', 'login.html')

@app.route('/tienda')
def tienda_p(): return send_from_directory('.', 'index.html')

@app.route('/carrito')
def carrito_p(): return send_from_directory('.', 'carrito.html')

@app.route('/fotos/<path:filename>')
def fotos(filename): return send_from_directory('imagenes', filename)

# --- API DE AUTENTICACIÓN ---
@app.route('/api/auth', methods=['POST'])
def auth():
    datos = request.json
    email = datos.get('email').lower().strip()
    password = datos.get('password')
    tipo = datos.get('tipo')
    db = cargar_db()
    if tipo == 'registro':
        if email in db: return jsonify({"status":"error","message":"Ya tienes cuenta"}), 400
        db[email] = {"password": password, "nombre": email.split('@')[0]}
        guardar_db(db)
        return jsonify({"status":"success"})
    else:
        if email in db and db[email]['password'] == password:
            return jsonify({"status":"success", "user": db[email]})
        return jsonify({"status":"error","message":"Correo o clave incorrectos"}), 401

# --- CATALOGO ---
CATALOGO_ROPA = [
    {"id": 1, "nombre": "Pijama Satin Luxe", "precio": 55000, "precio_viejo": 85000, "imagen": "/fotos/pijama.png", "categoria": "Pijamas", "tallas": ["S","M","L"], "colores": ["Rosa","Perla"], "desc": "Seda satinada de alta calidad."},
    {"id": 2, "nombre": "Conjunto Power Gym", "precio": 70000, "precio_viejo": 95000, "imagen": "/fotos/sudadera.png", "categoria": "Deportivo", "tallas": ["M","L"], "colores": ["Negro","Gris"], "desc": "Licra premium moldeadora."},
    {"id": 3, "nombre": "Pantalon Taches Pro", "precio": 89000, "precio_viejo": 110000, "imagen": "/fotos/pantalon.png", "categoria": "Pantalones", "tallas": ["6","8","10"], "colores": ["Azul Luxe"], "desc": "Bota ancha con taches de lujo."}
]

@app.route('/api/productos')
def get_p(): return jsonify({"status":"success", "data": CATALOGO_ROPA})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
