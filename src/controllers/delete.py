from .imports import *


@app.delete('/sms/<int:id>')
@jwt_required()
def sms_delete(id):
    try:
        sms_ = SMS.query.filter_by(id=id).first()
        sms_.apague_se()
        if sms_:
            code, resposta = 200 , True
        else: code, resposta = 300 , False
        return make_response(jsonify({'sms':resposta}),code)
    except:
        return make_response(jsonify({'sms':False}),500)

@app.delete('/sms_user/<int:usuario>')
@jwt_required()
def sms_user_delete(usuario):
    try:
        for sms_ in SMS.query.filter_by(usuario=usuario).all():
            sms_.apague_se()
        return make_response(jsonify({'sms':True}),200)
    except:
        return make_response(jsonify({'sms':False}),500)