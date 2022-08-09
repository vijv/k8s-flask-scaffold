from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello Flask Changed!"


@app.route("/name/<name>")
def echo_name(name):
    return jsonify({"name": name})


if __name__ == "__main__":
    app.run("0.0.0.0", 3000)
