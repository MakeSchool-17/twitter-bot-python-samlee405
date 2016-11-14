from flask import Flask
import sample
import wordFrequency

app = Flask(__name__)

@app.route('/')

def getSentence():
    return sample.sample()

if (__name__) == ('__main__'):
    app.run()
