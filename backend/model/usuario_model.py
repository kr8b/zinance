from util.db import db


class UsuarioModel(db.Model):
    __tablename__ = 'tb_usuario'


    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    senha = db.Column(db.String(32))


    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


 # API Methods:


    def get_all():
        if UsuarioModel.find_all() == []:
            return {}
        return UsuarioModel.find_all()


    def get_by_id(id):
        found = UsuarioModel.find_by_id(id)
        if found:
            return found.json()
        return {}



    def post(self):
        UsuarioModel.add()


    def put(self, id):
        if UsuarioModel.find_by_id(id):
            UsuarioModel.update(id)
        else:
            return id_not_found


    def delete(self):
        UsuarioModel.find_by_id(id)
        UsuarioModel.delete()


# Class methods:


    @classmethod
    def find_all(cls):
        return [found.json() for found in cls.query.all()]


    @classmethod
    def find_by_id(cls, id):
        return UsuarioModel.query.filter_by(id=id).first()


    def add(self):
        db.session.add(self)
        db.session.commit()


    def remove(self):
        db.session.delete(self)
        db.session.commit


    def update(self, **dados):
        UsuarioModel.find_by_id(id).update(dict(**dados))
        db.session.commit()


    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }


    def __repr__(self):
        return '<Usuario %r>' % self.id


# Kind of constants for repetitive returns:


id_not_found = {'msg': 'id not found'}
