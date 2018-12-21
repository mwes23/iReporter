from flask import Flask,jsonify,request
from models import Redflag
import random


app = Flask(__name__)

redflag_list = []
	

@app.route('/')
def hello():
	return 'hello world'

@app.route('/v1/redflag', methods=['POST'])
def createdflag():
	values = request.get_json()	
	if not values:
		response = {
		"status": 400,
		"error":"No Input",
		}
		return jsonify(response),400

	requestedvalues = ['title','desc']
	if not all(item in values for item in requestedvalues):
		response = {
		"status": 404,
		"error": "missing parameters"
		}
		return jsonify(response),400
	redflag = Redflag(values['title'],values['desc'])
	redflag_list.append(redflag)
	flagers=[i.__dict__ for i in redflag_list]
	response = {
	"status":"200",
	"data": flagers
	}
	return jsonify(response),201

@app.route('/v1/allflags', methods=['GET'])
def allflags():
	flags = []
		
	if len(redflag_list) < 1:
		response = {
		"message": "There no red flags",
		}
		return jsonify(response),400
	if len(redflag_list) >= 1:
		for flag in redflag_list:
			flags.append(flag.to_json())
		response = {
		"status":200,
		"data": flags	
		}

@app.route('/v1/oneflag', methods=['GET'])
def oneflags():
	if len(redflag_list) < 1:
		response = {
		"status": 404,
		"error": "There are no red flags"
		}
		return jsonify(response),400
	if len(redflag_list) >= 1:
		redflagid = random.randint(1,len(redflag_list))
		flag = redflag_list[redflagid]
		response = {
		"status":200,
		"data":flag
		}
		return jsonify(response),200


if __name__ == '__main__':
	app.run(debug=True)