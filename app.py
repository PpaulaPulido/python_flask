from flask import Flask, request,render_template, redirect, url_for
import mysql.connector

app = Flask (__name__)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'agenda'
)
cursor = db.cursor()

#Para ejecutar
@app.route('/')
def index():
    return render_template('index.html')




@app.route('/Registrar', methods = ['POST'])
def registrar_usuario():
    Nombres = request.form['nombre']
    Apellidos = request.form['apellido']
    Email = request.form['email']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    
    #insertar datos a la tabla
    cursor.execute(
        "INSERT INTO personas((nombre_persona,apellido_persona,email,direccion,telefono,user_persona,contrasena)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,direccion,telefono,usuario,contrasena))
    
    db.commit()
    return redirect(url_for("Registrar"))



if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug = True, port=5005)
#Rutas
