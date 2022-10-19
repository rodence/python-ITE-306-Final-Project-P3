#Title: Space World
#Description: This website is information about our solar system 
#Programmers:
#1. Rodence D. Atacador
#2. Mark Joshua E. De Dios
#3. Kenneth Perez
#4. Marvin Caventa
#Date Submitted: 10/20/2022
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def main():
    return render_template("index2.html")


@app.route("/info")
def info():
    return render_template("aass.html")


@app.route("/planets")
def planets():
    return render_template("apam.html")

@app.route("/view")
def view():
    return render_template("vtss.html")

@app.route("/images")
def images():
    return render_template("sai.html")

@app.route("/quiz")
def quiz():
    return render_template("pq.html")


@app.route("/facts")
def facts():
    return render_template("if.html")


if __name__ == "__main__":
    app.run(debug=True)
