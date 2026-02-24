from flask import Flask, jsonify, send_from_directory, abort
import os

app = Flask(__name__, static_folder='.')

# Catálogo actualizado con estilo.jpeg
CATALOGO = [
    {"id": 1, "nombre": "Camiseta Ciarené", "precio": 45000, "precio_antes": 62000, "imagen": "camisetas.png", "categoria": "Camisas"},
    {"id": 2, "nombre": "Pantalón Premium", "precio": 85000, "imagen": "pantalon.png", "categoria": "Pantalones"},
    {"id": 3, "nombre": "Pijama Seda", "precio": 65000, "imagen": "pijama.png", "categoria": "Casual"},
    {"id": 4, "nombre": "Sudadera Sport", "precio": 75000, "imagen": "sudadera.png", "categoria": "Deportivo"},
    {"id": 5, "nombre": "Pijama Estilo", "precio": 35000, "imagen": "estilo.jpeg", "categoria": "Casual"}
]

---

### Rutas de Navegación

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/carrito')
def cart_page():
    return send_from_directory('.', 'carrito.html')

---

### API y Recursos

@app.route('/api/productos')
def api_productos():
    """Retorna todos los productos en formato JSON."""
    return jsonify(CATALOGO)

@app.route('/api/productos/<int:id>')
def api_producto_detalle(id):
    """Permite obtener un solo producto por su ID."""
    producto = next((p for p in CATALOGO if p["id"] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/<path:filename>')
def serve_static(filename):
    """
    Sirve imágenes (como estilo.jpeg) y otros archivos estáticos.
    Es más seguro que la implementación anterior.
    """
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory('.', filename)

---

if __name__ == '__main__':
    # Corregido: 'name' -> '__main__' para evitar errores de ejecución
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
