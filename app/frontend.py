import os, time, datetime
import math
import json
import flask
import requests

from app import webapp


@webapp.route('/')
def mainpage():
    return flask.render_template('mainpage.html')

