import random
from flask import jsonify,request,Flask
import pandas as pd

NarutoApi = Flask(__name__)
df = pd.read_csv('finalQuotes.csv', names=['Speakers', 'Quotes'])

def get_random_quote():
    rq = random.randint(0, len(df))
    speaking = df.values[rq][0]
    quote = df.values[rq][1]
    quote_obj = {"Speaker": speaking, "Quote": quote}
    return quote_obj

@NarutoApi.route('/', methods=['GET'])
def dashboard():
    return jsonify(get_random_quote())

if __name__ == '__main__':
    NarutoApi.run(host= '127.0.0.1',port=5000)
