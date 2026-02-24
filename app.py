from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# --- CATALOGO CON MÚLTIPLES IMÁGENES ---
CATALOGO = [
    {
        "id": 1, 
        "nombre": "Camiseta Ciarené Luxury", 
        "precio": 45000, 
        "precio_antes": 75000,
        # Ahora usamos una lista [] con varios nombres de archivos
        "imagenes": ["camisetas.png", "pijama.png", "sudadera.png"], 
        "categoria": "Camisas"
    },
    {
        "id": 2, 
        "nombre": "Pantalón Premium Gala", 
        "precio": 95000, 
        "precio_antes": 120000, 
        "imagenes": ["pantalon.png", "alto.jpeg"], 
        "categoria": "Pantalones"
    },
    {
        "id": 3, 
        "nombre": "Pijama Seda Relax", 
        "precio": 65000, 
        "imagenes": ["pijama.png"], 
        "categoria": "Casual"
    },
    # Agrega el resto de tus productos igual usando "imagenes": [...]
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

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
