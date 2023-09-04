from .imports import *


@app.post('/sms')
@jwt_required()
def sms_post():
    data = request.json
    try:
        new_sms = SMS(data['usuario'],data['mensagem'],data['destinatario'],data['data'],data['hora'])
        new_sms.cadastre_se()
        return make_response(jsonify({'msg':sms.dumps(SMS.query.filter_by(usuario=data['usuario']).first())}),200)
    except:
        return make_response(jsonify({'msg':False}),400)

@app.post('/enviar_codigo')
@jwt_required()
def enviar_codigo():
    data = request.json
    try:
        print(data)
        return make_response(jsonify({'resposta':True}),200)
    except:
        return make_response(jsonify({'resposta':True}),404)

