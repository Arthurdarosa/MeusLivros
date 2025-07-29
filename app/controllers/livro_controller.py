from flask import Blueprint, request, jsonify, render_template
from app.models.livro import Livro
from flask_jwt_extended import jwt_required, get_jwt_identity

livro_bp = Blueprint('livro', __name__)

@livro_bp.route('/livros', methods=['GET'])
@jwt_required()
def pagina_livros():
    usuario_email = get_jwt_identity()
    livros = Livro.objects(usuario=usuario_email)
    return render_template('livros.html', livros=livros, email=usuario_email)

@livro_bp.route('/api/livros', methods=['POST'])
@jwt_required()
def adicionar_ou_atualizar_livro():
    usuario_email = get_jwt_identity()
    data = request.json
    nome = data.get('nome')
    pagina = data.get('pagina')
    if not nome or pagina is None:
        return jsonify({'erro': 'Nome e página são obrigatórios'}), 400
    livro = Livro.objects(nome=nome, usuario=usuario_email).first()
    if livro:
        livro.pagina = pagina
        livro.save()
        return jsonify({'mensagem': 'Página atualizada!'})
    else:
        Livro(nome=nome, pagina=pagina, usuario=usuario_email).save()
        return jsonify({'mensagem': 'Livro adicionado!'})

@livro_bp.route('/api/livros', methods=['GET'])
@jwt_required()
def listar_livros():
    usuario_email = get_jwt_identity()
    livros = Livro.objects(usuario=usuario_email)
    return jsonify([{'nome': l.nome, 'pagina': l.pagina} for l in livros])

@livro_bp.route('/api/livros/<nome>', methods=['DELETE'])
@jwt_required()
def remover_livro(nome):
    usuario_email = get_jwt_identity()
    livro = Livro.objects(nome=nome, usuario=usuario_email).first()
    if livro:
        livro.delete()
        return jsonify({'mensagem': 'Livro removido!'})
    return jsonify({'erro': 'Livro não encontrado'}), 404

