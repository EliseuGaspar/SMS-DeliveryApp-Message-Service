from ..app import ma
from .mensagem import SMS


class SMSSchemma(ma.SQLAlchemySchema):
    class Meta:
        model = SMS
    
    id = ma.auto_field()
    usuario = ma.auto_field()
    mensagem = ma.auto_field()
    destinatario = ma.auto_field()
    data = ma.auto_field()
    hora = ma.auto_field()

sms = SMSSchemma()
smss = SMSSchemma(many=True)