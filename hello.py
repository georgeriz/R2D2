from flask import Flask, render_template, redirect
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("hello_world.html")

@app.route('/my_input')
def my_input():
    return redirect("/")
	
@app.route('/api')
def get_results():
	return json.dumps({"name":"jack", "city":"los angeles"})
	
if __name__ == "__main__":
	app.run(debug=True)