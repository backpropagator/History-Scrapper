import os

def parse(url):
	try:
		parsed_url_component = url.split('//')
		sublevel_split = parsed_url_component[1].split('/',1)
		domain = sublevel_split[0].replace("www.","")
		return domain
	except IndexError:
		return "URL format error!"