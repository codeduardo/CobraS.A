from .database import db,Usuario

def create_db():
    db.drop_all()
    db.create_all()
    
def init_db():
    create_db()
    
    usuario = Usuario(
        nombre = 'Cobra S.A',
        username = 'admin',
        is_admin = True
    )
    
    usuario.set_password('admin')
    
    db.session.add(usuario)
    db.session.commit()
    