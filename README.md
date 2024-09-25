
# Proyecto Chambitas 
### Autor - [@Esteban Barrios](https://github.com/tebareinyu/) 
#### Institución: Universidad Regional - Ing. Luis Felipe Figueroa Molina

### Descripción del Proyecto
El proyecto Chambitas es una plataforma web que facilita la búsqueda de oportunidades laborales para diferentes categorías profesionales. La aplicación está construida utilizando Python y Flask como framework principal.


### 1. Clonar el repositorio:

```bash
git clone https://github.com/tebareinyu/chambitas.git
```

### 2. Cambiar a la carpeta de instalacion chambitas
```bash
cd chambitas
```

### 3. Crear un entorno virtual de python
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
.\venv\Scripts\activate   # En Windows
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicacion
```bash
python app.py
```
### Cambios recientes:
- **Entorno virtual:** Se eliminó el entorno virtual mal configurado previamente en la carpeta `chambitas`.
- **Módulos de Python:** El entorno de Python no estaba bien configurado y no se sabía qué módulos estaban siendo utilizados. Se creó el archivo `requirements.txt` para gestionar las dependencias de Python.
- **Base de datos:** No hay una base de datos disponible. Se implementó un bypass temporal para que la aplicación funcione sin la base de datos.
- **Dependencias de Node.js:** Se eliminaron los archivos `package.json` y `package-lock.json`, ya que no se estaban utilizando dependencias de Node.js ni librerías gestionadas por npm.



### Optimizaciones

- No tiene buena documentacion
- se elimino la carpeta chambitas (donde estaba configurado el entorno virtual)
- El entorno de pyton chambitas no esta bien configurado
- No se sabe que modulos pip de pyton estan usando, se hara manual
- se creo la carpeta Requeriments para poder instalarlo
- La app no tiene una base de datos para poder instalar
- se creo un byppas para poder usar la app
- se elimino el package y lock porque no esa haciendo uso de node ni de las librerias.




## Soporte

Para seguimiento y soporte, email teba.mompiano@gmail.com.


## Estructura del Proyecto

```bash
chambitas
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
├── static
│   ├── Cards-Category
│   │   ├── c1-pintor.png
│   │   ├── constructor.jpg
│   │   ├── electricista.jpg
│   │   ├── electrico2.jpg
│   │   ├── enfermero.png
│   │   ├── estilistaservicio.jpg
│   │   ├── florista.jpg
│   │   ├── jardinero.jpg
│   │   ├── Limpieza.jpg
│   │   ├── maestroprivado.jpg
│   │   ├── mecanicaadomi.png
│   │   ├── panadero.png
│   │   ├── veterinario.jpg
│   │   └── zyro-image.png
│   ├── Chambitas.png
│   ├── css
│   │   ├── estilosCat.css
│   │   └── main.css
│   ├── juan.jpg
│   ├── luis.jpg
│   ├── pedro.jpg
│   ├── trabajadores.jpg
│   ├── trabajadores2.jpg
│   └── trabajadores3.jpg
├── templates
│   ├── Cart
│   │   ├── Cart.html
│   │   └── estilos.css
│   ├── category
│   │   └── category.html
│   ├── checkout
│   │   └── checkout.html
│   ├── Complyments
│   │   └── complyments.html
│   ├── Contact
│   │   └── contact.html
│   ├── details
│   │   └── details.html
│   ├── elements
│   │   ├── images
│   │   │   ├── bandera.svg
│   │   │   └── success.png
│   │   ├── nav_footer.html
│   │   └── style.css
│   ├── hirings
│   │   └── Hirings.html
│   ├── home
│   │   └── home.html
│   ├── icons
│   │   └── Chambitas.png
│   ├── login
│   │   ├── index.html
│   │   ├── login.html
│   │   └── style.css
│   ├── personas
│   │   └── personas.html
│   ├── product_details
│   │   ├── css
│   │   │   ├── ajax-loader.gif
│   │   │   ├── bootstrap.min.css
│   │   │   ├── font-awesome.min.css
│   │   │   ├── nouislider.min.css
│   │   │   ├── slick-theme.css
│   │   │   ├── slick.css
│   │   │   └── style.css
│   │   ├── fonts
│   │   │   ├── fontawesome-webfont.eot
│   │   │   ├── fontawesome-webfont.svg
│   │   │   ├── fontawesome-webfont.ttf
│   │   │   ├── fontawesome-webfont.woff
│   │   │   ├── fontawesome-webfont.woff2
│   │   │   ├── FontAwesome.otf
│   │   │   ├── slick.eot
│   │   │   ├── slick.svg
│   │   │   ├── slick.ttf
│   │   │   └── slick.woff
│   │   ├── img
│   │   │   ├── AuriGamer.png
│   │   │   ├── aurisony.png
│   │   │   ├── camara01.png
│   │   │   ├── logo.png
│   │   │   ├── product01.png
│   │   │   ├── product02.png
│   │   │   ├── product03.png
│   │   │   ├── product04.png
│   │   │   ├── product05.png
│   │   │   ├── product06.png
│   │   │   ├── product07.png
│   │   │   ├── product08.png
│   │   │   ├── product09.png
│   │   │   └── QR APP.png
│   │   ├── js
│   │   │   ├── bootstrap.min.js
│   │   │   ├── jquery.min.js
│   │   │   ├── jquery.zoom.min.js
│   │   │   ├── main.js
│   │   │   ├── nouislider.min.js
│   │   │   └── slick.min.js
│   │   └── product_detail.html
│   ├── proveedores
│   │   └── proveedores.html
│   ├── servicios_ubicacion
│   │   └── servicios_ubicacion.html
│   ├── signin
│   │   └── signin.html
│   └── styles
│       └── styles.css
```


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

