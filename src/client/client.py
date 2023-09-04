from socketio import Client

client = Client()


def enviar(resposta) -> bool:
    if not client.connected:
        client.connect('http://localhost:2020')
    client.emit('confirmation-r',{'R':resposta})


