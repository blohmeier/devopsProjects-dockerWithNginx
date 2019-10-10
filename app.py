#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/works/')
def works():
    return 'works\n'

@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello {}!\n'.format(username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)     # open for everyone