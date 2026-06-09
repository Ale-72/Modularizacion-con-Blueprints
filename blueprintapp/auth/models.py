from blueprintapp.app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False) # Hash bcrypt de la contraseña
    
    def __repr__(self):
        return f"<USUARIO: {self.username}>"
