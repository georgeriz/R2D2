from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("hello_world.html")

@app.route('/my_input')
def my_input():
    return redirect("/")