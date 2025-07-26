from banco import bdPetMatch
from flask_login import UserMixin

class Usuario(bdPetMatch.Model, UserMixin):
    __tablename__ = 'usuario'
    id = bdPetMatch.Column(bdPetMatch.Integer, primary_key=True)
    role = bdPetMatch.Column(bdPetMatch.String(30), nullable=False)
    nome = bdPetMatch.Column(bdPetMatch.String(150), nullable=False)
    cpf = bdPetMatch.Column(bdPetMatch.String(14), nullable=False, unique=True)
    telefone = bdPetMatch.Column(bdPetMatch.String(15), nullable=False)
    endereco = bdPetMatch.Column(bdPetMatch.String(150), nullable=False)
    data_nascimento = bdPetMatch.Column(bdPetMatch.Date, nullable=False)
    email = bdPetMatch.Column(bdPetMatch.String(150), nullable=False)
    senha = bdPetMatch.Column(bdPetMatch.String(), nullable=False)

class Animal(bdPetMatch.Model):
    __tablename__ = 'animal'
    id = bdPetMatch.Column(bdPetMatch.Integer, primary_key=True)
    nome = bdPetMatch.Column(bdPetMatch.String(150), nullable=False)
    imagem = bdPetMatch.Column(bdPetMatch.String(500), nullable=False)
    descricao = bdPetMatch.Column(bdPetMatch.String(500), nullable=False)  # <-- Adiciona a coluna descrição
    vacinacao = bdPetMatch.Column(bdPetMatch.String(200), nullable=False)
    localizacao = bdPetMatch.Column(bdPetMatch.String(150), nullable=False)
    status = bdPetMatch.Column(bdPetMatch.String(80), default="Disponível")
    doador_id = bdPetMatch.Column(bdPetMatch.Integer, bdPetMatch.ForeignKey('usuario.id'), nullable=False)