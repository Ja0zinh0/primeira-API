from flask import Flask,jsonify, request

app = Flask(__name__) #cria um aplicativo 
postagens = [
    {
        'titulo': 'Minha Historia ',
        'autor': 'Amanda Dias  ',
    },
    {
        'titulo': 'Nova Distivo Sony',
        'autor': 'Amanda Dias  ',
    },
    {
        'titulo': 'Lançamento do Ano',
        'autor': 'Jeff Bezos ',
    }
]

#rota padarao - GET http://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens) 

app.run(port=5000, host='localhost',debug=True)