from ..app import db
from datetime import datetime as dt

class SMS(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key = True, autoincrement = True)
    usuario = db.Column(db.String(12))
    mensagem = db.Column(db.String(2000))
    destinatario = db.Column(db.String(13))
    data = db.Column(db.String(120))
    hora = db.Column(db.String(120))
    estado = db.Column(db.Integer)
    data_atualizacao = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self) -> str:
        return f"SMS Nº {self.id}"
    
    def __init__(self,
                usuario : int, mensagem : str,
                destinatario : str, data : str = str(dt.now())[:10],
                hora : str = str(dt.now())[11:16]
    ) -> None:
        self.usuario = usuario
        self.mensagem = mensagem
        self.destinatario = destinatario
        self.data = data
        self.hora = hora
        self.estado = 1
    
    def cadastre_se(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def apague_se(self) -> None:
        db.session.delete(self)
        db.session.commit()