from .database import Usuario


def get_user_by_username(username):
    return Usuario.query.filter_by(username = username).first()
