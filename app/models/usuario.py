from mongoengine import Document, StringField
import bcrypt

class Usuario(Document):
    email = StringField(required=True, unique=True)
    senha = StringField(required=True)

    def set_senha(self, senha_plana):
        self.senha = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verificar_senha(self, senha_plana):
        return bcrypt.checkpw(senha_plana.encode('utf-8'), self.senha.encode('utf-8')) 