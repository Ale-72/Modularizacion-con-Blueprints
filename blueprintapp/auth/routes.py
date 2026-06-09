# Librerias a usar en el modulo
from flask import request, render_template, redirect, url_for, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user

# Referencia a la base de datos y cifrado
from blueprintapp.app import db, bcrypt
# Modelos con los que interactura el modulo
from blueprintapp.auth.models import Usuario

bp_auth = Blueprint('bp_auth', __name__, template_folder='templates')

@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('bp_core.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verificar si el usuario ya existe
        usuario_existente = Usuario.query.filter_by(username=username).first()
        if usuario_existente:
            flash('El nombre de usuario ya está registrado.', 'danger')
            return redirect(url_for('bp_auth.register'))
        
        # Encriptar contraseña e insertar nuevo usuario
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        nuevo_usuario = Usuario(username=username, password=pw_hash)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('bp_auth.login'))
        
    return render_template('auth/register.html')

@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bp_core.index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Buscar usuario y comprobar contraseña
        usuario = Usuario.query.filter_by(username=username).first()
        if usuario and bcrypt.check_password_hash(usuario.password, password):
            login_user(usuario)
            flash(f'¡Bienvenido de nuevo, {username}!', 'success')
            return redirect(url_for('bp_core.index'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('bp_auth.login'))
            
    return render_template('auth/login.html')

@bp_auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('bp_core.index'))
