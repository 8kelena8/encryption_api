# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=False)

from routes import *

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

