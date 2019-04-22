#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import inquiry 


def create_app():
	app = Flask(__name__)
	Bootstrap(app)

	return app

app = create_app()


@app.route('/')
def index():
    return render_template('start.html')


@app.route('/<iid>/start', methods=['POST'])
def start(iid):
	data = request.form

	if 'student_id' not in data or 'test_code' not in data:
		return jsonify({'status': 'error', 'message': 'missing fields'}), 400
	
	student_id = data['student_id']
	test_code = data['test_code']
	
	i = inquiry.load(iid)
	poll = i.first_poll()         # logic
	subject = i.next_subject()    # data
	
	return render_template('inquiry.html', student_id=student_id,
						   test_code=test_code, poll=poll,
						   subject=subject)

	
@app.route('/<iid>/next')
def next_inquiry():
    # save answers
	data = request.form

	if 'registro' not in data or 'test_code' not in data
	or 'answers' not in data or 'poll_id' not in data:
		return jsonify({'status': 'error', 'message': 'missing fields'}), 400

	answers = 
	student_id = data['registro']
	test_code = data['test_code']

	i = inquiry.load(iid)
	i.save_answers(poll_id, answers)
	s = inquiry.next_subject()    # data
	
	return render_template('inquiry.html', student_id=student_id,
						   test_code=test_code, inquiry=i, subject=s)
	
    





if __name__ == '__main__':
    app.run(debug=True)
