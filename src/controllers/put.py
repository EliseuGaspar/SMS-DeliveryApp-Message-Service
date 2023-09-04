from .imports import *


@app.put('/sms/<int:id>')
@jwt_required()
def sms_put(id):
    data = request.json
    try:
        sms_ = SMS.query.filter_by(id=id).first()
        sms_.usuario = data['usuario']
        sms_.mensagem = data['mensagem']
        sms_.destinatario = data['destinatario']
        sms_.data = data['data']
        sms_.hora = data['hora']
        sms_.cadastre_se()
        return make_response(jsonify({'msg':sms.dumps(SMS.query.filter_by(id=id).first())}),200)
    except:
        return make_response(jsonify({'msg':False}),400)

@app.put('/sms_user/<int:usuario>')
@jwt_required()
def user_put(usuario):
    data = request.json
    try:
        for sms_ in SMS.query.filter_by(usuario=usuario).all():
            sms_.usuario = data['telefone']
            sms_.cadastre_se()
        return make_response(jsonify({'msg':sms.dumps(SMS.query.filter_by(id=id).first())}),200)
    except:
        return make_response(jsonify({'msg':False}),400)