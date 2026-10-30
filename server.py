from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', titulo='flask', mensaje='Bienvenido a la website de la UDL-ICO', contactos='Contacto', servicios='Servicios', productos='Productos')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', mensaje='Estos son los servicios que ofrecemos.'   )

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', mensaje='Contáctanos para más información.')

@app.route('/productos')
def productos():
    return render_template('productos.html', mensaje='Estos son los productos que ofrecemos.'   )


if __name__ == '__main__':
    app.run(debug=True,port=5050) 