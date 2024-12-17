from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, matricula, email, password):
        self.id = id
        self.matricula = matricula
        self.email = email
        self.password = password

