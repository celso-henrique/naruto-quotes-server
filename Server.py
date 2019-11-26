import random
from flask import jsonify,request,Flask
import numpy as np
import pandas as pd
NarutoApi = Flask(__name__)
df = pd.read_csv('finalQuotes.csv', names=['Speakers', 'Quotes'])

def get_random_quote():
    rq = random.randint(0, len(df))
    speaking = df.values[rq][0]
    quote = df.values[rq][1]
    x = {"Speaker": speaking, "Quote": quote}
    return x

def char_quotes(character):
    df2 = df
    df2 = df2[df2.Speakers.str.contains(character)]
    print(df2)
    rq = random.randint(0, len(df2))
    speaking = df2.values[rq][0]
    quote = df2.values[rq][1]
    x = {"Speaker": speaking, "Quote": quote}
    return x

@NarutoApi.route('/NarutoQuotes/Random', methods=['GET'])
def first_method():
    x = get_random_quote()
    return jsonify(x)

@NarutoApi.route('/NarutoQuotes', methods=['GET'])
def dashboard():
    if request.method == 'GET':
        shinobi = request.args.get('character', '')
    x = char_quotes(shinobi)
    return jsonify(x)

if __name__ == '__main__':
    NarutoApi.run(host= '127.0.0.1',port=5000)