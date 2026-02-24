from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# --- TU CATÁLOGO DE PRODUCTOS ---
# Para que salga el precio tachado, añade "precio_antes"
CATALOGO = [
    {
        "id": 1, 
        "nombre": "Camiseta Ciarené Luxury", 
        "precio": 45000, 
        "precio_antes": 75000, # <--- Esto activa la etiqueta de OFERTA
        "imagen": "camisetas.png", 
        "categoria": "Camisas"
    },
    {
        "id": 2, 
        "nombre": "Pantalón Premium Gala", 
        "precio": 95000, 
        "precio_antes": 120000, 
        "imagen": "pantalon.png", 
        "categoria": "Pantalones"
    },
    {
        "id": 3, 
        "nombre": "Pijama Seda Relax", 
        "precio": 65000, 
        "imagen": "pijama.png", # Sin precio_antes, sale normal
        "categoria": "Casual"
    },
    {
        "id": 4, 
        "nombre": "Sudadera Sport Urbano", 
        "precio": 80000, 
        "precio_antes": 110000,
        "imagen": "sudadera.png", 
        "categoria": "Deportivo"
    },
    {
        "id": 5, 
        "nombre": "Pijama Estilo", 
        "precio": 35000, 
        "precio_antes": 60000,
        "imagen": "estilo.jpeg", 
        "categoria": "Deportivo"
    }
]

# RUTA PARA MOSTRAR EL INDEX
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# RUTA PARA MOSTRAR EL CARRITO
@app.route('/carrito')
def cart_page():
    return send_from_directory('.', 'carrito.html')

# API QUE ENVÍA LOS PRODUCTOS AL HTML
@app.route('/api/productos')
def api_productos():
    return jsonify(CATALOGO)

# RUTA PARA QUE LAS FOTOS DE LA BARRA LATERAL SE VEAN
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Esto es para que funcione en Railway o localmente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

