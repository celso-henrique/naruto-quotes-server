import random
from flask import jsonify,request,Flask
import numpy as np
import pandas as pd

NarutoApi = Flask(__name__)

def loadquotes():
    df = pd.read_csv('Scraper/ScrapedQuotes/narutoquotes.csv', names =['Speakers','Quotes'])
    df = df.drop_duplicates()
    return df

@NarutoApi.route('/Naruto/Random', methods=['GET'])
def add_message():
    quotes = loadquotes()
    speaking = ''
    quote = ''
    while(quote == ''):
        rq = random.randint(1,len(quotes))
        speaking = quotes.values[rq][0]
        quote = quotes.values[rq][1]
        x = {"Speaker": speaking, "Quote": quote}
    return jsonify(x)

if __name__ == '__main__':
    NarutoApi.run(host= '127.0.0.1',port=5000)