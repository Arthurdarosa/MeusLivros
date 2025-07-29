from mongoengine import Document, StringField, IntField

class Livro(Document):
    nome = StringField(required=True)
    pagina = IntField(required=True)
    usuario = StringField(required=True)  # email do usuário dono do livro