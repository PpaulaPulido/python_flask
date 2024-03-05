from flask import Flask, request,render_template, redirect, url_for,flash
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
def lista():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM personas')
    personas = cursor.fetchall()
    return render_template('index.html', personas = personas)

@app.route('/registrar', methods = ['GET','POST'])
def registrar_usuario():
    
    if request.method == 'POST':
        Nombres = request.form.get('nombre')
        Apellidos = request.form.get('apellido')
        Email = request.form.get('email')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')
    
        #insertar datos a la tabla
        cursor.execute(
            "INSERT INTO personas(nombre_persona,apellido_persona,email,direccion,telefono,user_persona,contrasena)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,direccion,telefono,usuario,contrasena))
    
        db.commit()
        flash('usuario creado correctamente','success')
        #redirigir a la misma pagina 
        return redirect(url_for("registrar_usuario"))
    return render_template('Registrar.html')




if __name__ == '__main__':
    app.add_url_rule('/', view_func=lista)
    app.run(debug = True, port=3000)
#Rutas
