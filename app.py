from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html", title= "This is my Home Page!")

@app.route("/contact")
def body():
    return render_template("body.html", title = "Pls Contact Me!")

@app.route("/about")
def about():
    return render_template("aboutMe.html", title = "This is About Me!")

if __name__ == "__main__":
    app.run(port= 4000, debug=True)