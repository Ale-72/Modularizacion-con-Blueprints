from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager # Flask-Login para sesiones
from flask_bcrypt import Bcrypt # Bcrypt para contraseñas

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager() # Manejador de login
bcrypt = Bcrypt() # Cifrador de contraseñas

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'clave_secreta_equipo_2026' # Clave para sesiones
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_equipo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app) # Inicializar login
    bcrypt.init_app(app) # Inicializar bcrypt
    
    # Configurar redirección de login
    login_manager.login_view = 'bp_auth.login'
    login_manager.login_message = 'Por favor inicia sesión para acceder.'
    login_manager.login_message_category = 'warning'
    
    # Cargador de usuario para Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from blueprintapp.auth.models import Usuario
        return Usuario.query.get(int(user_id))
    
    # 1. Importación del blueprint (Para cada modulo)
    from blueprintapp.miembros.routes import bp_miembro
    from blueprintapp.core.routes import bp_core
    from blueprintapp.tareas.routes import bp_tarea
    from blueprintapp.auth.routes import bp_auth # Blueprint de autenticacion
    
    # 2. Registrar el blueprint (Para cada modulo)
    app.register_blueprint(bp_miembro,url_prefix="/miembros")
    app.register_blueprint(bp_core,url_prefix="/")
    app.register_blueprint(bp_tarea,url_prefix="/tareas")
    app.register_blueprint(bp_auth,url_prefix="/auth") # Prefijo /auth
    
    return app