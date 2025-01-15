from flask_login import LoginManager
from core.models import User
from database.init_db import *

login_manager = LoginManager()
session = Session(bind=engine)

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()