# 📚 WebLivros - Sistema de Gerenciamento de Biblioteca Pessoal

Um sistema web completo para gerenciar sua biblioteca pessoal, desenvolvido com Flask, MongoDB e JWT.

## 🚀 Funcionalidades

- **👤 Sistema de Usuários**: Registro e login seguro com JWT
- **📖 CRUD de Livros**: Criar, visualizar, editar e deletar livros
- **📄 Controle de Páginas**: Acompanhe sua progressão de leitura
- **🎨 Interface Moderna**: UI responsiva e intuitiva
- **🔒 Segurança**: Proteção contra XSS, NoSQL injection e CORS
- **🌐 API REST**: Endpoints para integração com outros sistemas

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Banco de Dados**: MongoDB com MongoEngine
- **Autenticação**: JWT (JSON Web Tokens)
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja2
- **Segurança**: CORS, validação de tipos, escape HTML

## 📋 Pré-requisitos

- Python 3.8+
- MongoDB (local ou Atlas)
- pip

## 🔧 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/weblivros.git
cd weblivros
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
# Windows PowerShell
$env:JWT_SECRET_KEY="sua_chave_secreta_aqui"
$env:MONGODB_URI="sua_uri_mongodb"

# Linux/Mac
export JWT_SECRET_KEY="sua_chave_secreta_aqui"
export MONGODB_URI="sua_uri_mongodb"
```

5. **Execute a aplicação**
```bash
python run.py
```

6. **Acesse no navegador**
```
http://localhost:5000
```

## 🔐 Configuração de Segurança

### Variáveis de Ambiente (Produção)
```
JWT_SECRET_KEY=sua_chave_super_secreta
MONGODB_URI=mongodb+srv://usuario:senha@servidor.com
FRONTEND_URL=https://seusite.com
```

## 📁 Estrutura do Projeto

```
weblivros/
├── app/
│   ├── __init__.py          # Configuração da aplicação
│   ├── controllers/         # Controladores (rotas)
│   │   ├── livro_controller.py
│   │   └── usuario_controller.py
│   ├── models/             # Modelos de dados
│   │   ├── livro.py
│   │   └── usuario.py
│   └── templates/          # Templates HTML
│       ├── home.html
│       ├── livros.html
│       ├── login.html
│       └── registro.html
├── run.py                  # Arquivo de execução
├── requirements.txt        # Dependências Python
├── Procfile               # Configuração para deploy
└── README.md              # Este arquivo
```

## 🔒 Medidas de Segurança Implementadas

- **✅ XSS Protection**: Jinja2 escapa HTML automaticamente
- **✅ NoSQL Injection Protection**: MongoEngine previne injeção
- **✅ JWT Authentication**: Tokens seguros para autenticação
- **✅ CORS Configuration**: Controle de acesso cross-origin
- **✅ Input Validation**: Validação de tipos e dados
- **✅ Environment Variables**: Configurações sensíveis protegidas

## 🚀 Deploy

### Render (Recomendado)
1. Conecte seu repositório GitHub
2. Configure as variáveis de ambiente
3. Deploy automático a cada push

### Outras opções
- Railway
- Fly.io
- Heroku

## 📱 API Endpoints

### Autenticação
- `POST /registro` - Registrar novo usuário
- `POST /login` - Fazer login
- `GET /logout` - Fazer logout

### Livros
- `GET /livros` - Página de livros (interface)
- `GET /api/livros` - Listar livros (JSON)
- `POST /api/livros` - Criar/atualizar livro
- `DELETE /api/livros/<nome>` - Deletar livro

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [seu-linkedin](https://linkedin.com/in/seu-perfil)

## 🙏 Agradecimentos

- Flask pela excelente documentação
- MongoDB Atlas pelo banco de dados gratuito
- Comunidade Python por todas as bibliotecas incríveis

---

⭐ Se este projeto te ajudou, deixe uma estrela no repositório! 