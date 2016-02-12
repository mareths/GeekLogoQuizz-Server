from bottle import Bottle, run, response
import json

app = Bottle()

@app.route('/classement', method='GET')
def get_classement():
	classement = {
		'num_results': 5,
		'total_pages': 1,
		'page': 1,
		'concurents': [
			{'place': 1, 'nom': "Titou"},
			{'place': 2, 'nom': "Fanou"},
			{'place': 3, 'nom': "Nana"},
			{'place': 4, 'nom': "Emy"},
			{'place': 5, 'nom': "Bloublou"}
		]
	}
	response.content_type = 'application/json'
	return json.dumps(classement)

if __name__ == '__main__':
	run(app, host='localhost', port=8080, debug=True)