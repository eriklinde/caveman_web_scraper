import sqlite3
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
	con = sqlite3.connect('nytimes.db')
	results = con.execute("SELECT * FROM articles;")
	return render_template('articles.html', my_results=results)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

def extract_data():
	con = sqlite3.connect('nytimes.db')
	results = con.execute("SELECT * FROM articles;")

