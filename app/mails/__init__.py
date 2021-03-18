from flask import Blueprint


mails = Blueprint('mails', __name__, url_prefix='/mails', template_folder='templates')

from . import views