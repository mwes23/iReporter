from flask import Flask,jsonify,request


app = Flask(__name__)
redflags = []
	

@app.route('/')
def hello():
	return 'hello world'

@app.route('/v1/redflag', methods=['POST'])
def createdflag():
	values = request.get_json()	
	if not values:
		response = {
		"status": 400,
		"message":"No Input",
		}
		return jsonify(response),400

	requestedvalues = ['title','description']
	if not all(item in values for item in requestedvalues):
		response = {
		"message":"missing parameter",
		}
	return jsonify(response),400
	redflag = model(values['title'],values['description'])
	redflags.append(redflag)
	response = {
	"message":"Success"
	}
	return jsonify(response),201

@app.route('/v1/allflags', methods=['GET'])
def allflags():
	flags = []
		
	if len(redflags) < 1:
		response = {
		"message": "There no red flags",
		}
		return jsonify(response),400
	if len(redflags) >= 1:
		Flags.append()
		response = {
			"message":"success",
			}
		return jsonify(response),200


if __name__ == '__main__':
	app.run(debug=True)