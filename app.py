from flask import Flask, render_template, request
import requests
from PIL import Image

app = Flask(__name__, static_url_path='/static')


# # Conexión a la base de datos (comentar o eliminar mientras no tengas acceso)
# def create_db_connection():
#     server = '(localdb)\CHMBT'
#     database = 'Chambitas'
#     username = 'Admin'
#     password = '12345'
# 
#     conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
#     return conn
#
# cursor = conn.cursor()


# # Ruta para la API que estaba conectada a la base de datos (comentada por ahora)
# @app.route('/api/a', methods=['GET'])
# def obtener_todos_los_registros():
#     try:
#         query_result = execute_query('SELECT * FROM Productos')
#         return jsonify({'data': query_result})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        # Autenticación simple para pruebas
        if username == 'admin@admin.com' and password == 'password123':
            return render_template('login/success.html', username=username)
        else:
            return render_template('login/login.html', error='Invalid credentials')

    # Renderizar la plantilla de inicio de sesión si es un GET request
    return render_template('login/login.html')


@app.route('/home')
def home():
    return render_template('home/home.html')

@app.route('/category')
def category():
    return render_template('category/category.html')

@app.route('/details')
def details():
    return render_template('details/details.html')

@app.route('/elements')
def elements():
    return render_template('elements/elements.html')

@app.route('/product_details')
def product_details():
    return render_template('product_details/product_details.html')

@app.route('/signin')
def signin():
    return render_template('login/index.html')

@app.route('/hirings')
def hirings():
    return render_template('hirings/Hirings.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout/checkout.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores/proveedores.html')

@app.route('/servicios_ubicacion')
def servicios_ubicacion():
    return render_template('servicios_ubicacion/servicios_ubicacion.html')

@app.route('/personas')
def personas():
    return render_template('personas/personas.html')

@app.route('/complyments')
def complyments():
    return render_template('Complyments/complyments.html')

@app.route('/contact')
def contact():
    return render_template('Contact/contact.html')

if __name__ =='__main__':
    app.run(debug=True)

# Configurar Pillow para manejar imágenes PNG
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)
