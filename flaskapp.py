import os
import cgi
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    butts = "Butts are awesome"    
    return render_template('index.html',butts=butts)

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])


#form = cgi.FieldStorage()
#if form is not None
#    seachterm =  form.getvalue('searchbox')
#    butts = searchterm
#    render_template('index.html',butts=butts)
    
