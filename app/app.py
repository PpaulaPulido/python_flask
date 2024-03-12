from flask import Flask, request,render_template, redirect, url_for,flash,session
from werkzeug.security import generate_password_hash,check_password_hash
import bcrypt
import mysql.connector

app = Flask (__name__)
app.secret_key = '123456789'

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'agenda'
)
cursor = db.cursor()

@app.route('/password/<contrasenaEncrip>')
def encriptarContra(contrasenaEncrip):
    #generar un hash de la contraseña 
    #encriptar = bcrypt.hashpw(contrasenaEncrip.encode('utf-8'),bcrypt.gensalt())
    encriptar = generate_password_hash(contrasenaEncrip)
    valor = check_password_hash(encriptar,contrasenaEncrip)
    return "Encriptado:{0} | coincide:{1}".format(encriptar,valor)

#Para ejecutar
@app.route('/')
def lista():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM personas')
    personas = cursor.fetchall()
    cursor.close()
    return render_template('index.html', personas = personas)

@app.route('/usuario_existente')
def usuario_existente():
    return render_template('usuario_existente.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        #VERIFIAR CREDENCIALES DEL USUARIO
        username = request.form.get('txtcorreo')
        password = request.form.get('txtcontrasena')
        cursor = db.cursor()
        #cursor.execute('SELECT email,contrasena FROM personas where email = %s',(username,))
        #resultado = cursor.fetchone()

        cursor.execute('SELECT * FROM personas WHERE email = %s ',(username,))
        resultado = cursor.fetchone()
        
        if resultado and encriptarContra(password) == resultado[1]:
            print("corecto")
            session['usuario'] = username
            return redirect(url_for('lista'))
        else:
            print("error")
            error = 'credenciales invalidas, por favor intentarlo de nuevo'
            return render_template('sesion.html',error = error)


    return render_template('sesion.html')


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
        contrasenaEncriptada = encriptarContra(contrasena)
        #correo = 'SELECT * FROM personas WHERE email = %s'
        cursor.execute('SELECT * FROM personas WHERE email = %s',(Email,))
        resultado = cursor.fetchall()
        print(resultado)

        if len(resultado) > 0:
            flash('El correo electrónico ya está registrado', 'error')
            return redirect(url_for('usuario_existente'))

        else:
            print("no existe")
            #insertar datos a la tabla
            cursor.execute(
                "INSERT INTO personas(nombre_persona,apellido_persona,email,direccion,telefono,user_persona,contrasena)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,direccion,telefono,usuario,contrasenaEncriptada))
            db.commit()
            flash('usuario creado correctamente','success')
            #redirigir a la misma pagina 
            return redirect(url_for("registrar_usuario"))
    return render_template('Registrar.html')

@app.route('/editar/<int:id>',methods = ['POST','GET'])
def editar_usuario(id):
    cursor = db.cursor()
    if request.method == 'POST':
        #el nombre dentro del get es tomado del formulario editar y debe ser diferente al formulario de registro
        nombrePer = request.form.get('nombrePer')
        apellidoPer = request.form.get('apellidoPer')
        emailPer = request.form.get('emailPer')
        direccionPer = request.form.get('direccionPer')
        telefonoPer = request.form.get('telefonoPer')
        usuarioPer = request.form.get('usuarioPer')
        contrasenaPer = request.form.get('contrasenaPer')
        
        #sentencia para actualizar los datos
        #son las variables de la base de datos
        sql = "UPDATE personas SET nombre_persona = %s, apellido_persona = %s, email = %s, direccion = %s, telefono = %s, user_persona = %s, contrasena = %s WHERE id_persona = %s"
        cursor.execute(sql, (nombrePer, apellidoPer, emailPer, direccionPer, telefonoPer, usuarioPer, contrasenaPer, id))

        db.commit()
        flash('Datos actualizados correctamente', 'success')
        #retorna a una url}
        return redirect(url_for("lista"))
        
    else:
        #obtener los datos de la persona que se va editar
        cursor = db.cursor()
        cursor.execute('SELECT * FROM personas WHERE id_persona = %s',(id,))
        data = cursor.fetchall()
        cursor.close()
        #el render tempalte re direcicona a un html
        return render_template('editar.html', personas = data[0])
        



@app.route('/eliminar/<int:id>',methods = ['GET'])
def eliminar_usuario(id):
    cursor = db.cursor()
    if request.method == "GET":
       cursor.execute('DELETE FROM personas WHERE id_persona=%s',(id,))
       db.commit()
    return redirect(url_for("lista"))

if __name__ == '__main__':
    app.add_url_rule('/', view_func=lista)
    app.run(debug = True, port=3000)
#Rutas
