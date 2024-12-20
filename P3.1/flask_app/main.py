# Add to this file for the sample app lab
from flask import Flask
from flask import render_template

sample = Flask(__name__)


@sample.route("/")
def main():
    return render_template("index.html")


@sample.route("/feature")
def feature():
    return "This is a feature"


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5000)
