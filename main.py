# Session notes -
# 1/3/24: Barebones project preparation. Decided on libraries and laid out a development plan

from flask import Flask

app = Flask(__name__)

@app.route("/")
def heloWorld():
    return "<p>Hello, World!</p>"