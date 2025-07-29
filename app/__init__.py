import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.controllers import livro_bp, usuario_bp

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicialização das extensões
mongo = MongoEngine()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/weblivros'),
        'connect': False,  # Evita conexão automática
        'maxPoolSize': 10,
        'serverSelectionTimeoutMS': 5000
    }
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'sua_chave_secreta_aqui')  # Use variável de ambiente em produção
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'

    # Inicialização do MongoDB com tratamento de erro
    try:
        mongo.init_app(app)
        print(f"Conectando ao MongoDB: {os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/weblivros')}")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        print("Verifique se o MongoDB está rodando ou se a URI está correta no arquivo .env")
    
    jwt.init_app(app)
    
    # Configuração CORS comentada para teste
    CORS(app, origins=["http://localhost:5000", "http://127.0.0.1:5000"], supports_credentials=True)

    # Registro dos blueprints
    app.register_blueprint(livro_bp)
    app.register_blueprint(usuario_bp)
    
    # Rota da página inicial
    @app.route('/')
    def home():
        return render_template('home.html')

    return app
