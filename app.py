import os
from flask import Flask
from flask import request
from flask import url_for, render_template, make_response
from autodebate import Corpus

obama = Corpus('obama.txt')
romney = Corpus('romney.txt')

app = Flask(__name__)
"""
from werkzeug import SharedDataMiddleware
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
 '/':os.path.join(os.path.dirname(__file__), 'static')
 })

"""

@app.route('/')
def index():
    return open('static/index.html').read()

@app.route('/romneySay')
def romneySay():
    topic = request.args.get('topic', 'America')
    return romney.generate(topic)
    
@app.route('/obamaSay')
def obamaSay():
    topic = request.args.get('topic', 'America')
    return obama.generate(topic)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)