from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# Catálogo simple para probar
CATALOGO = [
    {"id": 1, "nombre": "Camiseta Ciarené", "precio": 45000, "imagen": "camisetas.png"},
    {"id": 2, "nombre": "Pantalón Premium", "precio": 85000, "imagen": "pantalon.png"}
]

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/productos')
def api_productos():
    return jsonify(CATALOGO)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
