from ..app import io
from ..client import client, enviar
from ..packages.connection import db


@io.on('confirmation-p')
def enviar_codigo(data):
    print(data)
    enviar(True)

@io.on('atualizar_dados_usuario')
def atualizar_dados(data):
    cursor = db.cursor()
    linhas = cursor.execute(F''' SELECT * FROM `sms` WHERE usuario = '{data["telefone_antigo"]}' ''')
    if linhas > 0:
        resposta = cursor.execute(F""" UPDATE `sms` SET usuario = '{data["telefone"]}' WHERE usuario = '{data['telefone_antigo']}'""")
        db.commit()
        if resposta and resposta > 0:
            io.emit('atualizar_dados_usuario-r',{
                'resposta':True,
                'dados': data
            })
            return 0
    else:
        io.emit('atualizar_dados_usuario-r',{
                'resposta':True,
                'dados': data
            })
        return 0
    io.emit('atualizar_dados_usuario-r',{
                'resposta':False,
                'dados': data
            })
    return 0


