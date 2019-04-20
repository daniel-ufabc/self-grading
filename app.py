#!/usr/bin/env python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pickle


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()


@app.route('/')
def index():
    return render_template('start.html')


@app.route('/next')
def next_inquiry():
    # discover what the next inquiry is
    # discover what is the next test-code 
    





if __name__ == '__main__':
    app.run(debug=True)
