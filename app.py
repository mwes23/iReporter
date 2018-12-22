from flask import Flask,jsonify,request
from models import Incident
import random


app = Flask(__name__)

redflag_list = []
object_id = 0
	

@app.route('/')
def hello():
	return 'hello world'

@app.route('/v1/red-flags', methods=['POST'])
def createredflag():
	values = request.get_json()	
	if not values:
		response = {
		"status": 400,
		"error":"No Input",
		}
		return jsonify(response),400

	requestedvalues = ["title","created_on","created_by","incident_type","location","status","images","video","comment"]
	if not all(item in values for item in requestedvalues):
		response = {
		"status": 404,
		"error": "missing parameters"
		}
		return jsonify(response),400
	redflag = Incident(abject_id, values['title'],values['created_on'],values["created_by"],values["incident_type"],values["location"],values["status"],values["images"],values["video"],values["comment"])
	redflag_list.append(redflag)
	object_id +=1
	response = {
	"status":"200",
	"data": redflag.to_json(),
	"id": object_id,
	"message":"Created red-flag record",
	}
	return jsonify(response),201

@app.route('/v1/red-flags', methods=['GET'])
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
		return jsonify(response),200

@app.route('/v1/red-flags/<red-flag-id>', methods=['GET'])
def oneflag():
	if len(redflag_list) < 1:
		response = {
		"status": 404,
		"error": "There are no red flags"
		}
		return jsonify(response),400
	if len(redflag_list) >= 1:
		redflagid = object_id += 1
		flag = redflag_list[redflagid]
		response = {
		"status":200,
		"data":flag
		}
		return jsonify(response),200

@app.route('/v1/red-flags/<red-flag-id>/location', methods=['PATCH'])
def editflaglocation(redflagid):
	if redflagid == '' or redflagid == None:
		response = {
		"status":404,
		"error": 'No ID given'
		}
		return jsonify(response),404
	if len(redflag_list) >= 1:
		redflagobj = redflag_list[int(redflagid)]
		values = request.get_json()
		requestedvalues = ["location"]
			if requestedvalues not in value :
				response = {
				"status": 404,
				"error": "missing parameters"
				}
				return jsonify(response),404
		redflag_dict = redflagobj.to_json()
		redflag_dict['location'] = values["location"]
		response = {
		"status":200,
		"data":redflag_dict,
		"Id":redflagid,
		"message":"Updated red-flag record’s location"
		}
		return jsonify(response),200

@app.route('/v1/red-flags/<red-flag-id>/location', methods=['PATCH'])
def editflagcomments(redflagid):
	if redflagid == '' or redflagid == None:
		response = {
		"status":404,
		"error": 'No ID given'
		}
		return jsonify(response),404

	if len(redflag_list) >= 1:
		redflagobj = redflag_list[int(redflagid)]
		values = request.get_json()
		requestedvalues = ["comment"]
			if requestedvalues not in value:
				response = {
				"status": 404,
				"error": "missing parameters"
				}
				return jsonify(response),404
		redflag_dict = redflagobj.to_json()
		redflag_dict['comment'] = values["comment"]
		response = {
		"status":200,
		"data":redflag_dict,
		"Id":redflagid,
		"message":"Updated red-flag record’s comment"
		}
		return jsonify(response),200



@app.route('/v1/red-flags/<red-flag-id>', methods=['DELETE'])
def delflag():
	if len(redflag_list) < 1:
		response = {
		"status": 404,
		"error": "There are no red flags"
		}
		return jsonify(response),400
	if len(redflag_list) >= 1:
		redflagid = random.randint(1,len(redflag_list))
		deleted = redflag_list.pop(redflagid)
		response = {
		"status": 200,
		"data":deleted,
		"Id":redflagid
		"message":"red-flag record has been deleted"
		}
		return jsonify(response),200


if __name__ == '__main__':
	app.run(debug=True)