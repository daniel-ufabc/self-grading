#!/usr/bin/env python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import inquiry 
import re
import pickle


def create_app():
	app = Flask(__name__)
	Bootstrap(app)

	return app

app = create_app()


@app.route('/')
def index():
    return render_template('start.html')


@app.route('/start/<iid>')
def start(iid):
	"""
	From request, obtain:
	* RA
	* CÓDIGO (da prova do aluno)
	Carrega o script de 
	"""
	
	i = inquiry.load(iid)
	
	# discover what the next inquiry is
    # discover what is the next test-code is
    # render template

	
@app.route('/next')
def next_inquiry():
    # save answers 
    # discover what the next inquiry is
    # discover what is the next test-code is
    # render template
    





if __name__ == '__main__':
    app.run(debug=True)
