import sqlite3

'''
Utility functions to return Sqlite3 database files given the path
'''

def return_db(path):
	connection = sqlite3.connect(path, timeout=5)
	c = connection.cursor()
	query = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
	#c.execute("title from urls")
	c.execute(query)
	results = c.fetchall()
	c.close()
	return results

def return_top_sites(path):
	connection = sqlite3.connect(path,timeout=5)
	c = connection.cursor()
	query = "SELECT top_sites.url, top_sites.url_rank FROM top_sites"
	c.execute(query)
	results = c.fetchall()
	c.close()
	return results

def return_last_visited_time(path):
	connection = sqlite3.connect(path,timeout=5)
	c = connection.cursor()
	query = "SELECT urls.url, urls.last_visit_time FROM urls"
	c.execute(query)
	results = c.fetchall()
	c.close()
	return results