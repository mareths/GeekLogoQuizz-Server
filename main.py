from bottle import Bottle, run, request, response
import json

app = Bottle()

classement = {}
classement['num_results'] = 2
classement['total_pages'] = 1
classement['total_pages'] = 1
classement['concurents'] = []
classement['concurents'].append({'place': 1, 'nom': "Titou"})
classement['concurents'].append({'place': 2, 'nom': "Fanou"})

@app.route('/classement', method='GET')
def get_classement():
	response.content_type = 'application/json'
	return json.dumps(classement)

@app.route('/classement', method='POST')
def add_classement():
	try:
		postdata = request.body.read().decode('utf-8')
		symbol_request = json.loads(postdata)
		classement['concurents'].append({'place': symbol_request['place'], 'nom': symbol_request['nom']})
	except TypeError:
		return (500, "Le contenu est invalide")

if __name__ == '__main__':
	run(app, host='localhost', port=8080, debug=True)