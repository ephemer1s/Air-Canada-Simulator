# import flask
from app import webapp

if __name__ == "__main__":
    # webapp = flask.Flask(__name__)
    webapp.run(
        host='0.0.0.0',
        port=8080,
        debug=True,
    )