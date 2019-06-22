import flask
from flask import request, jsonify, render_template
import sqlite3
import url_utils
import collections 
import operator
import os
from django import db
import json
import itertools
from connection_utils import *
from sorting_apis import *

'''
TODO: Add ML API to predict the future probable searches
'''


app = flask.Flask(__name__)
app.config["DEBUG"] = True

'''
Change the Username according to your laptop
TODO: Make functionality to take user input and set the user_name automatically
'''
user_name = "aquarius31"

'''
This path is only for Linux Version, we can later extend it to Windows also
TODO: Add same functionality for Windows and detect the OS automatically
'''
path_to_history = "/home/"+user_name+"/.config/google-chrome/Default/History"
path_to_top_sites = "/home/"+user_name+"/.config/google-chrome/Default/Top Sites"

'''
Prototype Page to give error if an unreachable call is made
TODO: Make a page to display this error
'''
@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The sorting criteria could not be found.</p>", 404

'''
Implementation of /sort api
Format: localhost:5000/sort?by={frequency/time_spent}
Location: These APIs are implemented in sorting_apis.py file
parameter: by
	if by = "frequency"
		return list sorted by number of visits on the site
	if by = "time_spent"
		return list sorted by time spent by the user on various sites
	if by is not present
		return Page Not Found Error
TODO: 1. Add other sorting criteria like recent visits, etc
	  2. Add frontend to present the results
'''
@app.route('/sort', methods=['GET'])
def counter():

	sort_parameters = request.args
	by = sort_parameters.get('by')

	if by == "frequency":
		results = return_db(path_to_history)
		return sort_by_frequency(results)

	if by == "time_spent":
		results = return_top_sites(path_to_top_sites)
		return sort_by_recently_spent_time(results)

	if not by:
		results = return_last_visited_time(path_to_history)
		return last_visited(results)
'''
Main Index page
'''
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


app.run()