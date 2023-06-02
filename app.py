import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome Weclouddata! v0.6"


@app.route('/courses')
def courses():
    return 'DevOps'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
