import os
import requests
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template("my-form.html")
    #butts = "Butts are awesome"
    #return render_template('index.html',butts=butts)
@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    params3 = {'apikey': 'd8894db2dd60aed653e7bd91ea854ce91f46ec85', 'text': text, 'outputMode': 'json'}
    analyzedString = requests.get('https://access.alchemyapi.com/calls/text/TextGetTextSentiment',params=params3).json()
    return analyzedString['language']

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])


