from flask import Flask, request, render_template, redirect, url_for,flash,send_from_directory,session,jsonify
from flask_login import  LoginManager,login_required, login_user,logout_user, current_user
from banco import bdPetMatch
from models import Usuario, Animal
from datetime import datetime
import hashlib
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'petmatch'
lm = LoginManager(app)
lm.login_view = 'index'
lm.login_message = "Você precisa estar logado para acessar esta página!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdPet.db'
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

bdPetMatch.init_app(app)

@lm.user_loader
def user_loader(id):
    usuario = bdPetMatch.session.query(Usuario).filter_by(id=id).first()
    return usuario

def hash(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email, senha=hash(senha)).first()
        if usuario:
            perfil = usuario.role
            if perfil == 'adotante':
                login_user(usuario)
                return redirect(url_for('adotante'))
            else:
                login_user(usuario)
                return redirect(url_for('doador'))
        else:
            flash('Usuário ou senha inválidos')
            return redirect(url_for('index'))

@app.route('/cadastroAnimal', methods=['GET', 'POST'])
@login_required
def cadastroAnimal():
    if request.method == 'GET':
        return render_template('cadastroAnimais.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        vacinacao = request.form.getlist('vacinacao')  # Pega todas as vacinas marcadas
        vacinacao = ', '.join(vacinacao) if vacinacao else 'Nenhuma'  # Junta as vacinas em uma string
        localizacao = request.form['localizacao']

        if 'imagem' not in request.files:
            return 'Nenhum arquivo enviado.'
        file = request.files['imagem']
        if file.filename == '':
            return 'Nenhum arquivo selecionado.'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            imagem_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            novo_pet = Animal(nome=nome, imagem = imagem_path, descricao=descricao,vacinacao=vacinacao,localizacao=localizacao, doador_id=current_user.id)
            bdPetMatch.session.add(novo_pet)
            bdPetMatch.session.commit()

            return redirect(url_for('doador'))

@app.route('/adotante')
@login_required
def adotante():
    animais = Animal.query.filter_by().all()
    return render_template('adotante.html', nome=current_user.nome, email=current_user.email, telefone = current_user.telefone, role=current_user.role, animais=animais)

@app.route('/doador')
@login_required
def doador():
    animais = Animal.query.filter_by(doador_id=current_user.id).all()
    return render_template('doador.html', nome=current_user.nome, email=current_user.email, role=current_user.role, animais=animais)

@app.route('/adotar/<int:animal_id>', methods=['POST'])
@login_required
def adotar(animal_id):
    # Busca o animal pelo id
    animal = Animal.query.get(animal_id)
    
    if animal:
        # Atualiza o status do animal para 'Adotado'
        animal.status = 'Adotado'
        bdPetMatch.session.commit()  # Salva no banco de dados
        
        return jsonify({'status': 'sucesso', 'message': 'Pet adotado com sucesso!'})
    else:
        return jsonify({'status': 'erro', 'message': 'Animal não encontrado!'}), 404


@app.route('/formulario')
@login_required
def formulario():
    return render_template('formulario.html')

@app.route('/resposta_gato_adulto')
@login_required
def resposta_gato_adulto():
    return render_template('resposta_gato_adulto.html')

@app.route('/resposta_gato_filhote')
def resposta_gato_filhote():
    return render_template('resposta_gato_filhote.html')

@app.route('/resposta_cao_pequeno')
@login_required
def resposta_cao_pequeno():
    return render_template('resposta_cao_pequeno.html')

@app.route('/resposta_cao_medio')
@login_required
def resposta_cao_medio():
    return render_template('resposta_cao_medio.html')

@app.route('/resposta_cao_grande')
@login_required
def resposta_cao_grande():
    return render_template('resposta_cao_grande.html')

@app.route('/cadastroFinalizado')
def cadastroFinalizado():
    return render_template('cadastroFinalizado.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastroUsuario.html')
    elif request.method == 'POST':
        role = request.form.get('role')
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        data_nascimento_str = request.form['dataNascimento']
        email = request.form['email']
        senha = request.form['senha']

        try:
            data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
        except ValueError:
            return "Data de nascimento inválida", 400
        
        usuario = Usuario(role=role, nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, data_nascimento=data_nascimento, email=email, senha=hash(senha))
        bdPetMatch.session.add(usuario)
        bdPetMatch.session.commit()
        return redirect(url_for('cadastroFinalizado'))

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        bdPetMatch.create_all()
    app.run(debug=True)