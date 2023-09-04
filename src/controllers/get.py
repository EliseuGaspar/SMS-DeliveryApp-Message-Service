from .imports import *


@app.get('/')
async def index():
    return jsonify(
        {'msg':'DeliveryApp => SMS Service'}
    )

@app.before_request
def criar_tebela():
    db.create_all()


@app.get('/token')
def token():
    dados = request.json
    if dados['key'] == getenv('key'):
        return make_response(jsonify({'token':create_access_token(dados['key'],expires_delta=timedelta(minutes=60))}),200)
    else:
        return make_response(jsonify({'token':''}),401)


@app.get('/sms/<int:id_usuario>')
@jwt_required()
def sms_get(id_usuario):
        response = json.loads(smss.dumps(SMS.query.filter_by(usuario=id_usuario).all()))
        if response != []:
            return make_response(jsonify({'sms':response}),200)
        else:
            return make_response(jsonify({'sms':[]}),404)
        return make_response(jsonify({'sms':None}),400)
