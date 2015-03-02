from flask import Flask
app = Flask(__name__)
import json

@app.route("/<disease>")
def hello(disease):
	data = []
	with open("1.txt") as f:
		count = 0
		for line in f:
			arr = line.split("\t")
			if disease in arr[4].lower():
				data.append({'date': arr[0], 'zipcode': arr[2]})
	return json.dumps(data)
if __name__ == "__main__":
    app.run()
