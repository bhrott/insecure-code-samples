#!/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>')
def home(username):
   return render_template('index.html', title='Home', user={'username': username})

if __name__ == '__main__':
   app.run()
