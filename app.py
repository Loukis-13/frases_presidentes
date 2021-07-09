from flask import Flask, render_template
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
        return "<p>Presidente não encontrado</p>"

@app.route("/frase/aleatorio")
def aleatorio():
    presidente = choice(presidentes)
    with open(f'presidentes/{presidente}.txt', 'rt') as frases:
        return f"{choice(frases.readlines())} – {presidente.upper()}"

@app.route("/frase/<string:presidente>")
def frase(presidente):
    if presidente.lower() in presidentes:
        with open(f'presidentes/{presidente}.txt', 'rt') as frases:
            return f"{choice(frases.readlines())} – {presidente.upper()}"
    else:
        return "<p>Presidente não encontrado</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')