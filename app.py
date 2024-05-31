from flask import Flask,jsonify,request

app = Flask(__name__)

musicas = [{
    'cantor': 'mc ig',
    'musicas': 'Faz completo',
},
{
    'cantor': 'mc kevin',
    'musicas': 'blusa do timão ',
},
{
    'cantor': 'mc Ryan',
    'musicas': 'perfeita'
}
]

#rota padrao - GET http://localhost:5000

@app.route('/musicas',methods = ['GET'])
def obter_musicas():
    return jsonify(musicas)

#obter musicas por id - rota padrao http://localhost:5000/musicas/1
 
@app.route('/musicas/<int:indice>',methods = ['GET'])
def obter_musicas_por_indice(indice):
    return jsonify(musicas[indice]) 

#Criar uma nova postagem - POST  http://localhost:5000/musicas
@app.route('/musicas/',methods=['POST'])
def criar_musicas():
    musicas = request.get_json()
    musicas.append(musicas)
  
    return jsonify(musicas,200)

#atualizar musicas - PUT http://localhost:5000/musicas/1
@app.route('/musicas/<int:indice>',methods=['PUT'])
def atualizar_musicas(indice):
    musicas_alterada = request.get_json()
    musicas[indice].update(musicas_alterada)

    return jsonify(musicas[indice],200)

#Excluir musicas - delete 
@app.route('/musicas/<int:indice>',methods=['DELETE'])
def excluir_musicas(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Sua musicas foi excluida {musicas[indice]}',200 )
    except:
        return jsonify(f'Erro ao excluir musicas {musicas[indice]}',400)

app.run(port=5000,host='localhost',debug= True)