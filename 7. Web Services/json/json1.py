import json

data = '''{
	"name": "Galib",
	"phone": {
		"type": "GrammenPhone",
		"number": "01701080021"
	},
	"email":{
		"hide": "yes"
	}
}'''

info =  json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])