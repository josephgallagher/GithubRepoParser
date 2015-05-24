#github_repo_parser.py
import sys
import json
from datetime import date

"""
Example:

##Run ' curl https://api.github.com/repos/mbostock/d3/stats/commit_activity > commit_json.txt ' 
to get the required JSON file.

##Use ' commit_json.txt ' as the single argument to this script. Run:
	python github_repo_parser.py commit_json.txt

##The output will be the max number of commits along with the corresponding week, 
and the most committed day overall, spanning the entire year.
"""

def find_max_commits():
	commit_file = open(sys.argv[1]) 
	max_commits = 0 #Stores the maximum of the total commits each week.
	week = ""
	stats = json.load(commit_file) #Load the JSON file into stats as a list of hashes.
	for stat in stats: #For each hash in the list.. 
		if int(stat['total']) > max_commits: #If the total value is greater than the current max, make it the new max.
			max_commits = stat['total']
			week =  date.fromtimestamp(stat['week'])
	return "There were %d commits the week of %s" % (max_commits, week)
	


def max_days():
	commit_file = open(sys.argv[1])
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] #For output formatting.
	per_day = [0]*7 #Initialize the commits per day to 0, for each of the 7 days of the week.
	stats = json.load(commit_file)
	for stat in stats:
		for index, commits in enumerate(stat['days']):
			per_day[index] += stat['days'][index]#Increment the corresponding day by the number of commits the same day that week.
	return "%s was the most frequently committed day." % days[per_day.index(max(per_day))]



def main():
	print find_max_commits()
	print max_days()



main()


