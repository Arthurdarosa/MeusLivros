from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, current_app
from app.models.usuario import Usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/registro', methods=['GET'])
def registro_page():
    return render_template('registro.html')

@usuario_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    email = request.form.get('email')
    senha = request.form.get('senha')
    if not email or not senha:
        return render_template('registro.html', erro='Email e senha são obrigatórios')
    if Usuario.objects(email=email).first():
        return render_template('registro.html', erro='Email já cadastrado')
    usuario = Usuario(email=email)
    usuario.set_senha(senha)
    usuario.save()
    return render_template('registro.html', sucesso='Usuário registrado com sucesso! Redirecionando para login em 1 segundo...')

@usuario_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    email = request.form.get('email')
    senha = request.form.get('senha')
    if not email or not senha:
        return render_template('login.html', erro='Email e senha são obrigatórios')
    usuario = Usuario.objects(email=email).first()
    if not usuario or not usuario.verificar_senha(senha):
        return render_template('login.html', erro='Email ou senha inválidos')
    
    # Gerar token JWT e redirecionar para livros
    response = redirect(url_for('livro.pagina_livros'))
    set_access_cookies(response, create_access_token(identity=email))
    return response

@usuario_bp.route('/logout', methods=['GET'])
def logout():
    response = redirect('/')
    unset_jwt_cookies(response)
    return response

# API endpoints seguros
@usuario_bp.route('/api/usuario/perfil', methods=['GET'])
@jwt_required()
def get_perfil():
    """Endpoint seguro para obter perfil do usuário"""
    try:
        usuario_email = get_jwt_identity()
        usuario = Usuario.objects(email=usuario_email).first()
        
        if not usuario:
            return jsonify({'erro': 'Usuário não encontrado'}), 404
        
        return jsonify({
            'email': usuario.email,
            'data_criacao': usuario.id.generation_time.isoformat() if usuario.id else None
        })
    
    except Exception as e:
        print(f"Erro ao obter perfil: {str(e)}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@usuario_bp.route('/api/usuario/alterar-senha', methods=['POST'])
@jwt_required()
def alterar_senha():
    """Endpoint seguro para alterar senha"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'erro': 'Dados não fornecidos'}), 400
        
        # Validação dos dados
        senha_atual = data.get('senha_atual')
        nova_senha = data.get('nova_senha')
        
        if not senha_atual or not nova_senha:
            return jsonify({'erro': 'Senha atual e nova senha são obrigatórias'}), 400
        
        # Validação básica
        if not senha_atual or not nova_senha:
            return jsonify({'erro': 'Dados inválidos'}), 400
        
        # Validação básica da nova senha (mínimo 6 caracteres)
        if len(nova_senha) < 6:
            return jsonify({'erro': 'Nova senha deve ter pelo menos 6 caracteres'}), 400
        
        usuario_email = get_jwt_identity()
        usuario = Usuario.objects(email=usuario_email).first()
        
        if not usuario:
            return jsonify({'erro': 'Usuário não encontrado'}), 404
        
        # Verifica senha atual
        if not usuario.verificar_senha(senha_atual):
            return jsonify({'erro': 'Senha atual incorreta'}), 400
        
        # Altera a senha
        usuario.set_senha(nova_senha)
        usuario.save()
        
        print(f"Senha alterada com sucesso para: {usuario_email}")
        return jsonify({'mensagem': 'Senha alterada com sucesso'})
    
    except Exception as e:
        print(f"Erro ao alterar senha: {str(e)}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500 