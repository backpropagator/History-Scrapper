import url_utils
import collections 
import operator
import json
import itertools
from flask import jsonify

'''
API to sort sites by number of visits
'''
def sort_by_frequency(results):
	sites_count = {}
	#results = stats()
	for url, count in results:
		url = url_utils.parse(url)
		if url in sites_count:
			sites_count[url] += 1
		else:
			sites_count[url] = 1

	sites_count_sorted = collections.OrderedDict(sorted(sites_count.items(), key=lambda kv: kv[1], reverse=True))
	numberOfElementsToDisplay = 3
	top3_sorted_dict = {k: sites_count_sorted[k] for k in list(sites_count_sorted.keys())[:numberOfElementsToDisplay]}
	# with open("data_file.json", "w") as write_file:
	# 	json.dump(top3_sorted_dict, write_file)

	return jsonify(top3_sorted_dict)


'''
API to sort sites by time spent on each site
'''
def sort_by_recently_spent_time(results):
	sites_rank = {}

	for url, rank in results:
		url = url_utils.parse(url)
		#sites_rank[url] = rank+1
		if rank == 0:
			sites_rank[1] = url
		elif rank == 1:
			sites_rank[2] = url
		elif rank == 2:
			sites_rank[3] = url

	#sites_rank_sorted = collections.OrderedDict(sorted(sites_rank.items(), key=lambda kv: kv[1], reverse=False))
	#numberOfElementsToDisplay = 3
	#top3_ranked_dict = {k: sites_rank_sorted[k] for k in list(sites_rank_sorted.keys())[:numberOfElementsToDisplay]}

	return jsonify(sites_rank)