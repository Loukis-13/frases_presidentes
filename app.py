from flask import Flask, render_template
from flask_restplus import Api, Resource
from random import choice

app = Flask(__name__)

presidentes = ["dilma", "lula", "bolsonaro", "temer"]

@app.route("/")
def indice():
    return render_template('index.html', presidentes=presidentes, escolhido=choice(presidentes)), 200

@app.route("/aleatorio")
def aleatorio_html():
    presidente = choice(presidentes)
    with open(f'presidentes/{presidente}.txt', 'rt') as frases:
        return render_template('frase.html', frase=choice(frases.readlines()), presidente=presidente), 200

@app.route("/<string:presidente>")
def frase_html(presidente):
    if presidente.lower() in presidentes:
        with open(f'presidentes/{presidente}.txt', 'rt') as frases:
            return render_template('frase.html', frase=choice(frases.readlines()), presidente=presidente), 200
    else:
        return "<p>Presidente não encontrado</p>", 404


api = Api(
    app,
    doc= '/docs',
    title="Frases cômicas dos presidentes",
    description="Microserviço para servir as frases mais cômicas dos presidentes do Brasil"
)

@api.route('/frase/aleatorio')
class Aleatorio(Resource):
    def get(self):
        presidente = choice(presidentes)
        with open(f'presidentes/{presidente}.txt', 'rt') as frases:
            return f"{choice(frases.readlines())[:-1]} – {presidente.upper()}", 200

@api.route("/frase/<string:presidente>")
class Frase(Resource):
    def get(self, presidente):
        if presidente.lower() in presidentes:
            with open(f'presidentes/{presidente}.txt', 'rt') as frases:
                return f"{choice(frases.readlines())[:-1]} – {presidente.upper()}", 200
        else:
            return "Presidente não encontrado", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)