from bson import json_util
import psycopg2
from flask import Flask, render_template
app = Flask(__name__)
import json
conn = psycopg2.connect(
	database = "hackillinois",
	host = "imo-dw.ca3jydeuspcr.us-east-1.redshift.amazonaws.com",
	password = "IM0Hacker",
	user = "hackillinoisuser",
	port = 5439
)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/<disease>")
def hello(disease):
    cursor = conn.cursor()
    str = "SELECT COUNT(*) as total, rl_zipcode, to_char(rl_datetime, 'MM') as banana FROM requestlog WHERE rl_firstresult LIKE '%"+disease+"%' GROUP BY banana, rl_zipcode;"
    cursor.execute(str)
    data = []
    for x in cursor.fetchall():
        data.append({'date': x[2], 'zip': x[1], 'count': x[0]})
    return json.dumps(data, default=json_util.default)

if __name__ == "__main__":
    app.run()
