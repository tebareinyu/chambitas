from flask import Flask
from flask import render_template, jsonify
import pyodbc
import requests
from PIL import Image

app = Flask(__name__, static_url_path='/static')


app=Flask(__name__)

def create_db_connection():
    server = '(localdb)\CHMBT'   # Replace with your SQL Server instance name or IP address
    database = 'Chambitas'  # Replace with your database name
    username = 'Admin'  # Replace with your SQL Server username
    password = '12345'  # Replace with your SQL Server password

    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    return conn

cursor = conn.cursor()


# Configuraci�n de la conexi�n a la base de datos
# connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NOVA;DATABASE=proyectoBD;UID=proyecto;PWD=1234;TrustServerCertificate=yes')

# # Funci�n para ejecutar consultas en la base de datos
# def execute_query(query):
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         columns = [column[0] for column in cursor.description]
#         rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
#     return rows

# Ruta para la aplicaci�n web

# @app.route('/')
# def inicio():
#     # Consumir la API
#     api_url = 'http://127.0.0.1:5000/api/a' 
#     response = requests.get(api_url)
    
#     if response.status_code == 200:
#         data = response.json()['data']
#         return render_template('login/login.html', data=data)
#     else:
#         return render_template('error.html', message=f'Error al obtener datos de la API: {response.status_code}')

# # Ruta para la API
# @app.route('/api/a', methods=['GET'])
# def obtener_todos_los_registros():
#     try:
#         query_result = execute_query('SELECT * FROM Productos')
#         return jsonify({'data': query_result})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500  # Error de servidor
#     #return render_template('login/login.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    # Realizar la verificación del usuario (puedes usar el código de verificación del usuario de la respuesta anterior)

    if user:
        return render_template('login/success.html', username=username)
    else:
        return render_template('login/login.html', error='Invalid credentials')

    # Renderizar la plantilla de inicio de sesión
    return render_template('login/login.html')

# @app.route('/logout')
# def logout():

#     return render_template('login/index.html')


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