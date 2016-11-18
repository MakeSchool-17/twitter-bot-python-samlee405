from flask import Flask
import sample
import wordFrequency
import os

app = Flask(__name__)

@app.route('/')

def getSentence():
    return sample.sample()

if (__name__) == ('__main__'):
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host = '0.0.0.0', port=port)
