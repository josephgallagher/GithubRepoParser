import sys
import json

"""
##Sifts through the ' commit_json.txt ' file and exports the day index and the 
corresponding number of commits to output.
##Must pass ' commit_json.txt ' as an argument to the script.

##To export to file, for example, run:
	python export_points.py commit_json.txt > points_data.txt

##Then use gnuplot, or something similar, to read through ' points_data.txt '
and plot the points.
"""


def export_points():
  points_file = open(sys.argv[1])
  stats = json.load(points_file)
  for stat in stats:
    for index, point in enumerate(stat['days']):
      print index, point



def main():
	export_points()



main()
